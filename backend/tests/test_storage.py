# test_storage.py

import pytest
from app.storage import Storage
from app.models import Prompt

@pytest.fixture
def storage():
    return Storage()

def test_create_prompt(storage):
    # Create a Prompt object
    prompt = Prompt(id='1', title='Example title', content='Example Prompt')
    
    # Use the `create_prompt` method
    result = storage.create_prompt(prompt)
    
    # Assertions
    assert result == prompt
    assert storage._prompts[prompt.id] == prompt

    # Test with another prompt
    prompt2 = Prompt(id='2', title='Another title', content='Another Prompt')
    result2 = storage.create_prompt(prompt2)
    
    # Assertions for the second prompt
    assert result2 == prompt2
    assert storage._prompts[prompt2.id] == prompt2

def test_get_prompt_existing(storage):
    # Arrange: Set up the storage with a known state
    prompt_id = '1'
    prompt_content = 'Example Prompt'
    prompt_title = 'Example Title'
    storage._prompts = {prompt_id: Prompt(id=prompt_id, content=prompt_content, title=prompt_title)}

    # Act: Call the function with an existing prompt_id
    result = storage.get_prompt(prompt_id)

    # Assert: Check that the result is as expected
    assert result is not None
    assert result.id == prompt_id
    assert result.content == prompt_content
    assert result.title == prompt_title

def test_get_prompt_non_existing(storage):
    # Arrange: Set up the storage with a known state
    storage._prompts = {}  # Empty prompts

    # Act: Call the function with a non-existing prompt_id
    result = storage.get_prompt('non_existing_id')

    # Assert: Check that the result is None
    assert result is None

def test_get_all_prompts(storage):
    # Assuming 'Prompt' is a data class or similar object
    prompt1 = Prompt(id='1', title='Example Title 1', content='Example Prompt 1')
    prompt2 = Prompt(id='2', title='Example Title 2', content='Example Prompt 2')

    # Arrange: Set up the storage with known prompts
    storage._prompts = {
        '1': prompt1,
        '2': prompt2
    }

    # Act: Execute the method
    result = storage.get_all_prompts()

    # Assert: Verify the result is as expected
    assert result == [prompt1, prompt2]

def test_delete_prompt_success(storage):
    """
    Test that a prompt is successfully deleted when it exists.
    """
    # Arrange: Create a prompt and add it to storage
    prompt_id = '1'
    prompt = Prompt(id=prompt_id, title='Example Title', content='Example Content')
    storage._prompts = {prompt_id: prompt}

    # Act: Try to delete the existing prompt
    result = storage.delete_prompt(prompt_id)

    # Assert: The prompt should be deleted successfully
    assert result is True
    assert prompt_id not in storage._prompts

def test_delete_prompt_non_existing(storage):
    """
    Test that deleting a non-existing prompt returns False.
    """
    # Arrange: Ensure there are no prompts in storage
    storage._prompts = {}

    # Act: Attempt to delete a prompt that doesn't exist
    result = storage.delete_prompt('non_existing_id')

    # Assert: The result should be False
    assert result is False

class TestStorage:

    def setup_method(self):
        """Set up a test environment with some initial prompt data."""
        self.storage = Storage()
        self.storage._prompts = {
            '1': Prompt(id='1', title='Original Title 1', content='Original Content 1'),
            '2': Prompt(id='2', title='Original Title 2', content='Original Content 2'),
        }

    def test_update_prompt_success(self):
        """Test updating an existing prompt is successful."""
        new_prompt = Prompt(id='1', title='Updated Title 1', content='Updated Content 1')
        result = self.storage.update_prompt('1', new_prompt)
        assert result == new_prompt
        assert self.storage._prompts['1'].content == 'Updated Content 1'
        assert self.storage._prompts['1'].title == 'Updated Title 1'

    def test_update_prompt_id_not_found(self):
        """Test updating a prompt fails if the prompt_id is not found."""
        new_prompt = Prompt(id='3', title='Updated Title 3', content='Updated Content 3')
        result = self.storage.update_prompt('3', new_prompt)
        assert result is None

