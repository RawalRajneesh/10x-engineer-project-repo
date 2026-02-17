# Overview of Tagging Feature
The tagging feature allows users to categorize and organize prompts using descriptive labels. It helps users to easily retrieve, filter, and manage prompts based on common themes or characteristics defined by the tags.

## User Stories with Acceptance Criteria

**User Story 1:**
- **As a** user, **I want** to add tags to a prompt, **so that** I can categorize it for easy retrieval later.
  - **Acceptance Criteria:**
    - Users can add multiple tags to a prompt.
    - Tags can be created if they do not exist in the current tag list.

**User Story 2:**
- **As a** user, **I want** to filter prompts by tags, **so that** I can find prompts related to a specific topic or category quickly.
  - **Acceptance Criteria:**
    - Users can select one or more tags to filter the list of prompts.
    - Filtering results update dynamically based on selected tags.

**User Story 3:**
- **As a** user, **I want** to remove tags from a prompt, **so that** I can update or correct its categorization.
  - **Acceptance Criteria:**
    - Users can view existing tags on a prompt and remove them as needed.

## Data Model Changes Needed
- Add a new table `Tags` with the following fields:
  - `id`: Primary key
  - `name`: Name of the tag
- Add a join table `PromptTags` to associate tags with prompts:
  - `promptId`: Foreign key referring to the prompt
  - `tagId`: Foreign key referring to the tag

## API Endpoint Specifications
- `POST /tags`
  - Creates a new tag.
- `GET /tags`
  - Returns a list of all available tags.
- `POST /prompts/{promptId}/tags`
  - Adds a tag to a specific prompt.
- `DELETE /prompts/{promptId}/tags/{tagId}`
  - Removes a specific tag from a prompt.

## Search/Filter Requirements
- **Text Search**: Users should be able to search tags by name when applying them to a prompt.
- **Tag Filtering**: Allow filtering prompts by selecting multiple tags.
- **Pagination and Sorting**: Support pagination and sorting for tag lists to ensure usability with large numbers of tags.