import pytest
from app.models import (
    PromptCreate, Prompt, CollectionCreate, Collection, 
    PromptList, CollectionList, HealthResponse
)
from datetime import datetime
from uuid import UUID

def test_prompt_create_validation():
    # Test valid prompt creation
    valid_prompt = PromptCreate(title="Test Prompt", content="This is the content.")
    assert valid_prompt.title == "Test Prompt"
    assert valid_prompt.content == "This is the content."

    # Test invalid prompt creation
    with pytest.raises(ValueError):
        # Title is too short
        PromptCreate(title="", content="This is the content.")

    with pytest.raises(ValueError):
        # Title is too long
        PromptCreate(title="T" * 201, content="This is the content.")

def test_prompt_default_values():
    # Test default values for a complete Prompt object
    prompt = Prompt(title="Sample", content="Sample content")
    assert isinstance(prompt.id, str) and UUID(prompt.id)
    assert isinstance(prompt.created_at, datetime)
    assert isinstance(prompt.updated_at, datetime)

def test_prompt_serialization():
    prompt = Prompt(title="Sample", content="Sample content")
    # Convert to dict
    prompt_dict = prompt.dict()
    assert isinstance(prompt_dict, dict)
    assert prompt_dict["title"] == "Sample"

def test_collection_create_validation():
    # Test valid collection creation
    valid_collection = CollectionCreate(name="Test Collection")
    assert valid_collection.name == "Test Collection"

    # Test invalid collection creation
    with pytest.raises(ValueError):
        # Name is too short
        CollectionCreate(name="")

    with pytest.raises(ValueError):
        # Name is too long
        CollectionCreate(name="N" * 101)

def test_collection_default_values():
    # Test default values for a complete Collection object
    collection = Collection(name="Sample Collection")
    assert isinstance(collection.id, str) and UUID(collection.id)
    assert isinstance(collection.created_at, datetime)

def test_prompt_list_response():
    prompts = [Prompt(title="P1", content="C1"), Prompt(title="P2", content="C2")]
    response = PromptList(prompts=prompts, total=2)
    assert response.total == 2
    assert len(response.prompts) == 2

def test_collection_list_response():
    collections = [Collection(name="C1"), Collection(name="C2")]
    response = CollectionList(collections=collections, total=2)
    assert response.total == 2
    assert len(response.collections) == 2

def test_health_response_serialization():
    health = HealthResponse(status="Healthy", version="1.0.0")
    health_dict = health.dict()
    assert health_dict["status"] == "Healthy"
    assert health_dict["version"] == "1.0.0"
