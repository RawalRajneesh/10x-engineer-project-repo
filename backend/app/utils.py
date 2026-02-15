"""Utility functions for PromptLab"""

from typing import List
from app.models import Prompt


def sort_prompts_by_date(prompts: List[Prompt], descending: bool = True) -> List[Prompt]:
    """
    Sort prompts by creation date.

    Args:
        prompts (List[Prompt]): List of Prompt objects to be sorted.
        descending (bool): If True, sorts prompts from newest to oldest. Defaults to True.

    Returns:
        List[Prompt]: Sorted list of prompts.

    Examples:
        >>> sort_prompts_by_date(prompts, descending=True)
        [Prompt(...), Prompt(...)]
    """
    # BUG #3: This sorts ascending (oldest first) when it should sort descending (newest first)
    # The 'descending' parameter is ignored!
    return sorted(prompts, key=lambda p: p.created_at, reverse=descending)


def filter_prompts_by_collection(prompts: List[Prompt], collection_id: str) -> List[Prompt]:
    """
    Filter prompts by a specific collection ID.

    Args:
        prompts (List[Prompt]): List of Prompt objects to filter.
        collection_id (str): The collection ID to filter prompts by.

    Returns:
        List[Prompt]: List of prompts belonging to the specified collection.

    Examples:
        >>> filter_prompts_by_collection(prompts, "12345")
        [Prompt(...)]
    """
    return [p for p in prompts if p.collection_id == collection_id]


def search_prompts(prompts: List[Prompt], query: str) -> List[Prompt]:
    """
    Search for prompts containing the query string in their title or description.

    Args:
        prompts (List[Prompt]): List of Prompt objects to search within.
        query (str): The search string to look for in prompts.

    Returns:
        List[Prompt]: List of prompts that match the search query.

    Examples:
        >>> search_prompts(prompts, "example")
        [Prompt(...)]
    """
    query_lower = query.lower()
    return [
        p for p in prompts
        if query_lower in p.title.lower() or
           (p.description and query_lower in p.description.lower())
    ]


def validate_prompt_content(content: str) -> bool:
    """
    Check if prompt content is valid.

    A valid prompt should:
    - Not be empty
    - Not be just whitespace
    - Be at least 10 characters

    Args:
        content (str): The content of the prompt to validate.

    Returns:
        bool: True if content is valid, False otherwise.

    Examples:
        >>> validate_prompt_content("This is a valid prompt.")
        True
        >>> validate_prompt_content("   ")
        False
    """
    if not content or not content.strip():
        return False
    return len(content.strip()) >= 10


def extract_variables(content: str) -> List[str]:
    """
    Extract template variables from prompt content.

    Variables are in the format {{variable_name}}.

    Args:
        content (str): The content from which to extract variables.

    Returns:
        List[str]: A list of variable names found in the content.

    Examples:
        >>> extract_variables("Hello, {{name}}!")
        ['name']
    """
    import re
    pattern = r'\{\{(\w+)\}\}'
    return re.findall(pattern, content)

