"""Pydantic models for PromptLab"""

from datetime import datetime
from typing import Optional, List
from pydantic import BaseModel, Field
from uuid import uuid4


def generate_id() -> str:
    return str(uuid4())


def get_current_time() -> datetime:
    return datetime.utcnow()


# ============== Prompt Models ==============

class PromptBase(BaseModel):
    """Base model for Prompts.

    Attributes:
        title (str): The title of the prompt. Must be between 1 and 200 characters.
        content (str): The main content of the prompt. Must be at least 1 character.
        description (Optional[str]): An optional description for the prompt, maximum 500 characters.
        collection_id (Optional[str]): An optional collection identifier for the prompt.
    """
    title: str = Field(..., min_length=1, max_length=200)
    content: str = Field(..., min_length=1)
    description: Optional[str] = Field(None, max_length=500)
    collection_id: Optional[str] = None


class PromptCreate(PromptBase):
    """Model for creating a new prompt based on PromptBase."""
    pass


class PromptUpdate(PromptBase):
    """Model for updating an existing prompt based on PromptBase."""
    pass


class Prompt(PromptBase):
    """Model that represents a complete Prompt with additional metadata.

    Attributes:
        id (str): Unique identifier for the prompt, auto-generated.
        created_at (datetime): Timestamp when the prompt was created, auto-generated.
        updated_at (datetime): Timestamp for the last update of the prompt, auto-generated.
    """
    id: str = Field(default_factory=generate_id)
    created_at: datetime = Field(default_factory=get_current_time)
    updated_at: datetime = Field(default_factory=get_current_time)

    class Config:
        from_attributes = True


# ============== Collection Models ==============

class CollectionBase(BaseModel):
    """Base model for Collections.

    Attributes:
        name (str): The name of the collection. Must be between 1 and 100 characters.
        description (Optional[str]): An optional description for the collection, maximum 500 characters.
    """
    name: str = Field(..., min_length=1, max_length=100)
    description: Optional[str] = Field(None, max_length=500)


class CollectionCreate(CollectionBase):
    """Model for creating a new collection based on CollectionBase."""
    pass


class Collection(CollectionBase):
    """Model that represents a complete Collection with additional metadata.

    Attributes:
        id (str): Unique identifier for the collection, auto-generated.
        created_at (datetime): Timestamp when the collection was created, auto-generated.
    """
    id: str = Field(default_factory=generate_id)
    created_at: datetime = Field(default_factory=get_current_time)

    class Config:
        from_attributes = True


# ============== Response Models ==============

class PromptList(BaseModel):
    """Response model for a list of Prompts.

    Attributes:
        prompts (List[Prompt]): A list of Prompt objects.
        total (int): Total number of prompts available.
    """
    prompts: List[Prompt]
    total: int


class CollectionList(BaseModel):
    """Response model for a list of Collections.

    Attributes:
        collections (List[Collection]): A list of Collection objects.
        total (int): Total number of collections available.
    """
    collections: List[Collection]
    total: int


class HealthResponse(BaseModel):
    """Model for representing the health status of the service.

    Attributes:
        status (str): The health status, usually indicating if the service is running.
        version (str): The version of the service.
    """
    status: str
    version: str

