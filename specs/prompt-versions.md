Prompt Versioning Feature Specification
 1.Overview
The Prompt Versioning feature enables tracking and managing multiple versions of a prompt over time.
Each time a prompt is updated:
A new immutable version is created.
Previous versions remain accessible.
The latest version is marked as current.

This enables:
Audit history
Rollbacks
Change comparison
Safe editing

 User Stories & Acceptance Criteria
User Story 1 – Create Version on Update

As a user,
When I update a prompt,
I want the system to create a new version automatically,
So that previous versions are preserved.

2.Acceptance Criteria

Updating a prompt creates a new version record.
Previous versions remain unchanged.
Version number increments sequentially.
Latest version is marked is_current = true.

User Story 2 – View Version History

As a user,
I want to see all versions of a prompt,
So that I can review its change history.

Acceptance Criteria

Endpoint returns all versions sorted by version number (descending).

Metadata includes:

version number

created_at

created_by (if applicable)

change summary (optional)

3. User Story 3 – Retrieve Specific Version

As a user,
I want to fetch a specific version of a prompt,
So that I can inspect or compare it.

Acceptance Criteria

Can fetch by version number.

Returns 404 if version does not exist.

Cannot modify historical versions.

4. User Story 4 – Rollback to Previous Version

As a user,
I want to rollback to an older version,
So that I can restore previous content.

Acceptance Criteria

Rollback creates a new version using old version’s content.

Version numbers remain strictly increasing.

No version is overwritten.

5. Data Model Changes
Current Model (Simplified)
Prompt
- id (str)
- title (str)
- content (text)
- created_at (datetime)
- updated_at (datetime)

Proposed Model
Prompt (Parent Entity)
Prompt
- id (str)
- title (str)
- created_at (datetime)

PromptVersion (New Table)
PromptVersion
- id (str or UUID)
- prompt_id (FK → Prompt)
- version_number (int)
- content (text)
- is_current (bool)
- created_at (datetime)
- created_by (optional)
- change_summary (optional)

Constraints

(prompt_id, version_number) must be unique.

Only one version per prompt may have is_current = true.

Version numbers must increment sequentially.

6. API Endpoint Specifications
🔹 Create Prompt
POST /prompts


Creates:

Prompt

Version 1

🔹 Update Prompt (Creates New Version)
PUT /prompts/{prompt_id}


Behavior:

Create new version

Increment version_number

Mark previous version is_current = false

Response:

200 OK

Returns new current version

🔹 Get Current Prompt
GET /prompts/{prompt_id}


Returns:
Current version only

🔹 Get All Versions
GET /prompts/{prompt_id}/versions


Response:

[
  {
    "version_number": 3,
    "is_current": true,
    "created_at": "..."
  }
]

🔹 Get Specific Version
GET /prompts/{prompt_id}/versions/{version_number}


Returns 404 if:
Prompt not found
Version not found

🔹 Rollback
POST /prompts/{prompt_id}/rollback/{version_number}


Behavior:
Creates new version using selected version content
Returns newly created version

6. Edge Cases to Handle

Updating a non-existent prompt → 404
Fetching version for non-existent prompt → 404
Fetching invalid version number → 404
Concurrent updates causing version conflict
Large content size
Rollback of already-current version
Attempting to modify historical version directly (forbidden)
Soft-deleted prompts