"""FastAPI routes for PromptLab"""

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional

from app.models import (
    Prompt, PromptCreate, PromptUpdate,
    Collection, CollectionCreate,
    PromptList, CollectionList, HealthResponse,
    get_current_time
)
from app.storage import storage
from app.utils import sort_prompts_by_date, filter_prompts_by_collection, search_prompts
from app import __version__


app = FastAPI(
    title="PromptLab API",
    description="AI Prompt Engineering Platform",
    version=__version__
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ============== Health Check ==============

@app.get("/health", response_model=HealthResponse)
def health_check():
    """
    Check the health status of the API.
    
    Returns:
        HealthResponse: An object containing the status and version of the API.
    """
    return HealthResponse(status="healthy", version=__version__)


# ============== Prompt Endpoints ==============

@app.get("/prompts", response_model=PromptList)
def list_prompts(
    collection_id: Optional[str] = None,
    search: Optional[str] = None
):
    """
    Retrieve a list of prompts, optionally filtering by collection or search query.

    Args:
        collection_id (Optional[str]): ID of the collection to filter prompts by.
        search (Optional[str]): Search query to filter prompts.

    Returns:
        PromptList: A list of prompts matching the given filters.
    """
    prompts = storage.get_all_prompts()
    
    # Filter by collection if specified
    if collection_id:
        prompts = filter_prompts_by_collection(prompts, collection_id)
    
    # Search if query provided
    if search:
        prompts = search_prompts(prompts, search)
    
    # Sort by date (newest first)
    prompts = sort_prompts_by_date(prompts, descending=True)
    
    return PromptList(prompts=prompts, total=len(prompts))


@app.get("/prompts/{prompt_id}", response_model=Prompt)
def get_prompt(prompt_id: str):
    """
    Retrieve a prompt by its ID.

    Args:
        prompt_id (str): The ID of the prompt to retrieve.

    Returns:
        Prompt: The prompt corresponding to the given ID.

    Raises:
        HTTPException: If the prompt is not found.
    """
    prompt = storage.get_prompt(prompt_id)
    
    # Fix: Check if prompt does not exist and raise 404
    if not prompt:
        raise HTTPException(status_code=404, detail="Prompt not found")
    
    return prompt


@app.post("/prompts", response_model=Prompt, status_code=201)
def create_prompt(prompt_data: PromptCreate):
    """
    Create a new prompt.

    Args:
        prompt_data (PromptCreate): The data for the new prompt.

    Returns:
        Prompt: The newly created prompt.

    Raises:
        HTTPException: If the provided collection ID is not found.
    """
    if prompt_data.collection_id:
        collection = storage.get_collection(prompt_data.collection_id)
        if not collection:
            raise HTTPException(status_code=400, detail="Collection not found")
    
    prompt = Prompt(**prompt_data.model_dump())
    return storage.create_prompt(prompt)


@app.put("/prompts/{prompt_id}", response_model=Prompt)
def update_prompt(prompt_id: str, prompt_data: PromptUpdate):
    """
    Update an existing prompt by its ID.

    Args:
        prompt_id (str): The ID of the prompt to update.
        prompt_data (PromptUpdate): The updated data for the prompt.

    Returns:
        Prompt: The updated prompt.

    Raises:
        HTTPException: If the prompt or collection is not found.
    """
    existing = storage.get_prompt(prompt_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Prompt not found")
    
    # Validate collection if provided
    if prompt_data.collection_id:
        collection = storage.get_collection(prompt_data.collection_id)
        if not collection:
            raise HTTPException(status_code=400, detail="Collection not found")
    
    # Bug Fix: Update the updated_at timestamp to current time
    updated_prompt = Prompt(
        id=existing.id,
        title=prompt_data.title,
        content=prompt_data.content,
        description=prompt_data.description,
        collection_id=prompt_data.collection_id,
        created_at=existing.created_at,
        updated_at=get_current_time()
    )
    
    return storage.update_prompt(prompt_id, updated_prompt)


@app.patch("/prompts/{prompt_id}", response_model=Prompt)
def patch_prompt(prompt_id: str, prompt_data: PromptUpdate):
    """
    Partially update a prompt by its ID.

    Args:
        prompt_id (str): The ID of the prompt to update.
        prompt_data (PromptUpdate): The updated data fields for the prompt.

    Returns:
        Prompt: The updated prompt with changes applied.

    Raises:
        HTTPException: If the prompt or collection is not found.
    """
    existing = storage.get_prompt(prompt_id)
    if not existing:
        raise HTTPException(status_code=404, detail="Prompt not found")

    updated_prompt_data = existing
    if prompt_data.title is not None:
        updated_prompt_data.title = prompt_data.title
    if prompt_data.content is not None:
        updated_prompt_data.content = prompt_data.content
    if prompt_data.description is not None:
        updated_prompt_data.description = prompt_data.description

    if prompt_data.collection_id:
        collection = storage.get_collection(prompt_data.collection_id)
        if not collection:
            raise HTTPException(status_code=400, detail="Collection not found")
        updated_prompt_data.collection_id = prompt_data.collection_id

    updated_prompt_data.updated_at = get_current_time()

    return storage.update_prompt(prompt_id, updated_prompt_data)


@app.delete("/prompts/{prompt_id}", status_code=204)
def delete_prompt(prompt_id: str):
    """
    Delete a prompt by its ID.

    Args:
        prompt_id (str): The ID of the prompt to delete.

    Returns:
        None

    Raises:
        HTTPException: If the prompt is not found.
    """
    if not storage.delete_prompt(prompt_id):
        raise HTTPException(status_code=404, detail="Prompt not found")
    return None


# ============== Collection Endpoints ==============
@app.get("/collections", response_model=CollectionList)
def list_collections():
    """
    Retrieve a list of all collections.

    Returns:
        CollectionList: A list of all collections.
    """
    collections = storage.get_all_collections()
    return CollectionList(collections=collections, total=len(collections))


@app.get("/collections/{collection_id}", response_model=Collection)
def get_collection(collection_id: str):
    """
    Retrieve a collection by its ID.

    Args:
        collection_id (str): The ID of the collection to retrieve.

    Returns:
        Collection: The collection corresponding to the given ID.

    Raises:
        HTTPException: If the collection is not found.
    """
    collection = storage.get_collection(collection_id)
    if not collection:
        raise HTTPException(status_code=404, detail="Collection not found")
    return collection
    

@app.post("/collections", response_model=Collection, status_code=201)
def create_collection(collection_data: CollectionCreate):
    """
    Create a new collection.

    Args:
        collection_data (CollectionCreate): The data for the new collection.

    Returns:
        Collection: The newly created collection.
    """
    collection = Collection(**collection_data.model_dump())
    return storage.create_collection(collection)


@app.delete("/collections/{collection_id}", status_code=204)
def delete_collection(collection_id: str):
    """
    Delete a collection by its ID and set the collection ID to None for all prompts in this collection.

    Args:
        collection_id (str): The ID of the collection to delete.

    Returns:
        None

    Raises:
        HTTPException: If the collection is not found.
    """
    if not storage.delete_collection(collection_id):
        raise HTTPException(status_code=404, detail="Collection not found")
    
    storage.update_prompts_collection_to_none(collection_id)
    return None
