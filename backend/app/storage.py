"""In-memory storage for PromptLab

This module provides simple in-memory storage for prompts and collections.
In a production environment, this would be replaced with a database.
"""

from typing import Dict, List, Optional
from app.models import Prompt, Collection


class Storage:
    def __init__(self):
        self._prompts: Dict[str, Prompt] = {}
        self._collections: Dict[str, Collection] = {}
    
    # ============== Prompt Operations ==============
    
    def create_prompt(self, prompt: Prompt) -> Prompt:
        """
        Create a new prompt and store it in memory.

        Args:
            prompt (Prompt): The prompt object to be stored.

        Returns:
            Prompt: The stored prompt object.

        Example:
            >>> storage.create_prompt(Prompt(id='1', content='Example Prompt'))
            Prompt(id='1', content='Example Prompt')
        """
        self._prompts[prompt.id] = prompt
        return prompt
    
    def get_prompt(self, prompt_id: str) -> Optional[Prompt]:
        """
        Retrieve a prompt by its ID.

        Args:
            prompt_id (str): The unique identifier of the prompt.

        Returns:
            Optional[Prompt]: The prompt object if found, otherwise None.

        Example:
            >>> storage.get_prompt('1')
            Prompt(id='1', content='Example Prompt')
        """
        return self._prompts.get(prompt_id)
    
    def get_all_prompts(self) -> List[Prompt]:
        """
        Retrieve all stored prompts.

        Returns:
            List[Prompt]: A list of all stored prompt objects.

        Example:
            >>> storage.get_all_prompts()
            [Prompt(id='1', content='Example Prompt')]
        """
        return list(self._prompts.values())
    
    def update_prompt(self, prompt_id: str, prompt: Prompt) -> Optional[Prompt]:
        """
        Update an existing prompt.

        Args:
            prompt_id (str): The unique identifier of the prompt to update.
            prompt (Prompt): The new prompt object.

        Returns:
            Optional[Prompt]: The updated prompt object if the update is successful, otherwise None.

        Example:
            >>> storage.update_prompt('1', Prompt(id='1', content='Updated Prompt'))
            Prompt(id='1', content='Updated Prompt')
        """
        if prompt_id not in self._prompts:
            return None
        self._prompts[prompt_id] = prompt
        return prompt
    
    def delete_prompt(self, prompt_id: str) -> bool:
        """
        Delete a prompt by its ID.

        Args:
            prompt_id (str): The unique identifier of the prompt to delete.

        Returns:
            bool: True if the prompt was successfully deleted, False otherwise.

        Example:
            >>> storage.delete_prompt('1')
            True
        """
        if prompt_id in self._prompts:
            del self._prompts[prompt_id]
            return True
        return False
    
    # ============== Collection Operations ==============
    
    def create_collection(self, collection: Collection) -> Collection:
        """
        Create a new collection and store it in memory.

        Args:
            collection (Collection): The collection object to be stored.

        Returns:
            Collection: The stored collection object.

        Example:
            >>> storage.create_collection(Collection(id='1', name='Example Collection'))
            Collection(id='1', name='Example Collection')
        """
        self._collections[collection.id] = collection
        return collection
    
    def get_collection(self, collection_id: str) -> Optional[Collection]:
        """
        Retrieve a collection by its ID.

        Args:
            collection_id (str): The unique identifier of the collection.

        Returns:
            Optional[Collection]: The collection object if found, otherwise None.

        Example:
            >>> storage.get_collection('1')
            Collection(id='1', name='Example Collection')
        """
        return self._collections.get(collection_id)
    
    def get_all_collections(self) -> List[Collection]:
        """
        Retrieve all stored collections.

        Returns:
            List[Collection]: A list of all stored collection objects.

        Example:
            >>> storage.get_all_collections()
            [Collection(id='1', name='Example Collection')]
        """
        return list(self._collections.values())
    
    def delete_collection(self, collection_id: str) -> bool:
        """
        Delete a collection by its ID.

        Args:
            collection_id (str): The unique identifier of the collection to delete.

        Returns:
            bool: True if the collection was successfully deleted, False otherwise.

        Example:
            >>> storage.delete_collection('1')
            True
        """
        if collection_id in self._collections:
            del self._collections[collection_id]
            return True
        return False
    
    def get_prompts_by_collection(self, collection_id: str) -> List[Prompt]:
        """
        Retrieve all prompts associated with a specific collection ID.

        Args:
            collection_id (str): The unique identifier of the collection.

        Returns:
            List[Prompt]: A list of prompts associated with the collection.

        Example:
            >>> storage.get_prompts_by_collection('1')
            [Prompt(id='2', content='Prompt in Collection 1')]
        """
        return [p for p in self._prompts.values() if p.collection_id == collection_id]
    
    def update_prompts_collection_to_none(self, collection_id: str):
        """
        Update all prompts in the specified collection to have their collection_id set to None.

        Args:
            collection_id (str): The unique identifier of the collection whose prompts should be updated.

        Example:
            >>> storage.update_prompts_collection_to_none('1')
        """
        for prompt in self._prompts.values():
            if prompt.collection_id == collection_id:
                prompt.collection_id = None

    def clear(self):
        """
        Clear all stored prompts and collections.

        Example:
            >>> storage.clear()
        """
        self._prompts.clear()
        self._collections.clear()


# Global storage instance
storage = Storage()

