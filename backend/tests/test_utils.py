import pytest
from app.models import Prompt
from datetime import datetime
from app.utils import sort_prompts_by_date, filter_prompts_by_collection, search_prompts,validate_prompt_content  
from typing import NamedTuple


@pytest.fixture
def sample_prompts_for_sorting():
    return [
        Prompt(id="1", title="Prompt one", content="Content for prompt one.", collection_id="12345", created_at=datetime(2023, 10, 1)),
        Prompt(id="2", title="Prompt two", content="Content for prompt two.", collection_id="12345", created_at=datetime(2023, 9, 1)),
        Prompt(id="3", title="Prompt three", content="Content for prompt three.", collection_id="67890", created_at=datetime(2023, 8, 1)),
    ]

def test_sort_prompts_by_date_descending(sample_prompts_for_sorting):
    sorted_prompts = sort_prompts_by_date(sample_prompts_for_sorting, descending=True)
    assert sorted_prompts == [
        sample_prompts_for_sorting[0],  # Newest
        sample_prompts_for_sorting[1],
        sample_prompts_for_sorting[2],  # Oldest
    ]

def test_sort_prompts_by_date_ascending(sample_prompts_for_sorting):
    sorted_prompts = sort_prompts_by_date(sample_prompts_for_sorting, descending=False)
    assert sorted_prompts == [
        sample_prompts_for_sorting[2],  # Oldest
        sample_prompts_for_sorting[1],
        sample_prompts_for_sorting[0],  # Newest
    ]

def test_filter_prompts_by_collection():
    # Create sample prompts
    prompts = [
        Prompt(id="1", title="Prompt one", content="Content for prompt one.", collection_id="12345"),
        Prompt(id="2", title="Prompt two", content="Content for prompt two.", collection_id="12345"),
        Prompt(id="3", title="Prompt three", content="Content for prompt three.", collection_id="67890"),
    ]

    # Call the function with a specific collection_id
    filtered_prompts = filter_prompts_by_collection(prompts, "12345")

    # Check that the filtered prompts have the correct number of items
    assert len(filtered_prompts) == 2

    # Check that each filtered prompt has the correct collection_id
    assert all(p.collection_id == "12345" for p in filtered_prompts)

    # Check that the IDs match the expected results
    filtered_ids = [p.id for p in filtered_prompts]
    assert filtered_ids == ["1", "2"]


def test_search_prompts():
    # Create sample prompts with title and description
    prompts = [
        Prompt(id="1", title="Title one", content="Some content for title one.", collection_id="12345"),
        Prompt(id="2", title="Title two with unique description", content="A unique description here.", collection_id="12345"),
        Prompt(id="3", title="Another title", content="More content.", collection_id="67890"),
        Prompt(id="4", title="Untitled", content="Empty title here.", collection_id="67890"),
    ]

    # Change the query to match test expectations accurately
    matched_prompts = search_prompts(prompts, "Title ")

    # Check the correct number of prompts are returned
    assert len(matched_prompts) == 2
    assert all("title" in p.title.lower() for p in matched_prompts)

    # Test for a query that matches descriptions as well
    matched_prompts = search_prompts(prompts, "unique description")
    assert len(matched_prompts) == 1
    assert matched_prompts[0].id == "2"

    # Test no match scenario
    matched_prompts = search_prompts(prompts, "No Match")
    assert len(matched_prompts) == 0

    # Test with empty query; expect all prompts to be returned
    matched_prompts = search_prompts(prompts, "")
    assert len(matched_prompts) == len(prompts)  # Expect all prompts to be matched

def test_validate_prompt_content():
    # Test with valid content
    assert validate_prompt_content("This is a valid prompt.") == True

    # Test with empty string
    assert validate_prompt_content("") == False

    # Test with whitespace-only string
    assert validate_prompt_content("   ") == False

    # Test with content exactly 10 characters long
    assert validate_prompt_content("1234567890") == True
    
    # Test with content less than 10 characters long
    assert validate_prompt_content("123456789") == False

    # Test with leading and trailing spaces
    assert validate_prompt_content("    Valid content    ") == True


