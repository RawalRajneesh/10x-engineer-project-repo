from fastapi.testclient import TestClient
from unittest.mock import MagicMock
from pydantic import BaseModel

# Import the app and storage module correctly
from app.api import app
from app.api import storage
from app.models import TagCreate

client = TestClient(app)

# Define a minimal Prompt mock model if not already defined for testing purposes.
# Adjust the model fields to match requirements in your actual `Prompt` response model
class Prompt(BaseModel):
    id: str
    tags: list
    title: str = "Sample Title"
    content: str = "Sample Content"

def test_create_tag():
    # Test creating a new tag
    response = client.post("/tags", json={"name": "Urgent"})
    assert response.status_code == 201
    data = response.json()
    assert data["name"] == "Urgent"
    
def test_get_tags():
    # Test retrieving all tags
    response = client.get("/tags")
    assert response.status_code == 200

    # Access the 'tags' key from the response JSON and check the structure
    result = response.json()

    # Check that 'tags' is a list
    assert isinstance(result['tags'], list)
    assert 'total' in result  # Verify that the total is present

   

def test_add_tag_to_prompt_prompt_not_found():
    # Mock storage methods for prompt not found
    storage.get_prompt = MagicMock(return_value=None)

    response = client.post("/prompts/999/tags?tag_id=123")

    assert response.status_code == 404
    assert response.json() == {"detail": "Prompt not found"}

def test_add_tag_to_prompt_tag_not_found():
    # Mock storage methods for tag not found
    storage.get_prompt = MagicMock(return_value={"id": "123", "tags": []})
    storage.get_tag = MagicMock(return_value=None)

    # Update the request to pass 'tag_id' as a query parameter instead of JSON
    response = client.post("/prompts/123/tags?tag_id=999")

    assert response.status_code == 404
    assert response.json() == {"detail": "Tag not found"}


