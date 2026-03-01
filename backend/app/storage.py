from typing import Dict, List, Optional
from app.models import Prompt, Collection, Tag  # Include Tag in imports

class Storage:
    def __init__(self):
        self._prompts: Dict[str, Prompt] = {}
        self._collections: Dict[str, Collection] = {}
        self._tags: Dict[str, Tag] = {}  # Add tags to storage
        self._prompt_tags: Dict[str, List[str]] = {}  # Mapping from prompt_id to list of tag_ids
    
    # ============== Prompt Operations ==============
    
    def create_prompt(self, prompt: Prompt) -> Prompt:
        self._prompts[prompt.id] = prompt
        return prompt
    
    def get_prompt(self, prompt_id: str) -> Optional[Prompt]:
        return self._prompts.get(prompt_id)
    
    def get_all_prompts(self) -> List[Prompt]:
        return list(self._prompts.values())
    
    def update_prompt(self, prompt_id: str, prompt: Prompt) -> Optional[Prompt]:
        if prompt_id not in self._prompts:
            return None
        self._prompts[prompt_id] = prompt
        return prompt
    
    def delete_prompt(self, prompt_id: str) -> bool:
        if prompt_id in self._prompts:
            del self._prompts[prompt_id]
            return True
        return False
    
    # ============== Collection Operations ==============
    
    def create_collection(self, collection: Collection) -> Collection:
        self._collections[collection.id] = collection
        return collection
    
    def get_collection(self, collection_id: str) -> Optional[Collection]:
        return self._collections.get(collection_id)
    
    def get_all_collections(self) -> List[Collection]:
        return list(self._collections.values())
    
    def delete_collection(self, collection_id: str) -> bool:
        if collection_id in self._collections:
            del self._collections[collection_id]
            return True
        return False
    
    def get_prompts_by_collection(self, collection_id: str) -> List[Prompt]:
        return [p for p in self._prompts.values() if p.collection_id == collection_id]
    
    def update_prompts_collection_to_none(self, collection_id: str):
        for prompt in self._prompts.values():
            if prompt.collection_id == collection_id:
                prompt.collection_id = None

    # ============== Tag Operations ==============

    def create_tag(self, tag: Tag) -> Tag:
        self._tags[tag.id] = tag
        return tag

    def get_tag(self, tag_id: str) -> Optional[Tag]:
        return self._tags.get(tag_id)

    def get_all_tags(self) -> List[Tag]:
        return list(self._tags.values())

    def add_tag_to_prompt(self, prompt_id: str, tag_id: str) -> Optional[Prompt]:
        if prompt_id not in self._prompts or tag_id not in self._tags:
            return None

        if prompt_id not in self._prompt_tags:
            self._prompt_tags[prompt_id] = []

        if tag_id not in self._prompt_tags[prompt_id]:
            self._prompt_tags[prompt_id].append(tag_id)

        return self.get_prompt(prompt_id)

    def remove_tag_from_prompt(self, prompt_id: str, tag_id: str) -> bool:
        if prompt_id in self._prompt_tags and tag_id in self._prompt_tags[prompt_id]:
            self._prompt_tags[prompt_id].remove(tag_id)
            return True
        return False

    def get_prompt_tags(self, prompt_id: str) -> List[Tag]:
        tag_ids = self._prompt_tags.get(prompt_id, [])
        return [self._tags[tag_id] for tag_id in tag_ids if tag_id in self._tags]

    def clear(self):
        self._prompts.clear()
        self._collections.clear()
        self._tags.clear()
        self._prompt_tags.clear()

# Global storage instance
storage = Storage()

