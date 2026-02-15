# PromptLab

**Your AI Prompt Engineering Platform**

## Project Overview

PromptLab is an internal tool designed for AI engineers, enabling them to efficiently store, organize, and manage their prompts. It's akin to a "Postman for Prompts," providing a professional workspace with the following functionalities:

- Storage of prompt templates that include variables (`{{input}}`, `{{context}}`)
- Organization of prompts into collections
- Prompt tagging and search functionality
- Version history tracking
- Testing of prompts with sample inputs

## Features

- **Prompt Templates**: Store and manage prompt templates with support for variables.
- **Collections**: Group prompts into collections for better organization.
- **Tagging and Searching**: Tag prompts and perform searches.
- **Version Control**: Track changes and version history of prompts.
- **Testing Environment**: Test prompts using sample inputs.

## Setup Instructions

### Prerequisites

- Python 3.10+
- Node.js 18+ (to be used in later stages)
- Git

### Installation

1. **Clone the Repository:**

   ```bash
   git clone <your-repo-url>
   cd promptlab
   ```

2. **Backend Setup:**

   ```bash
   cd backend
   pip install -r requirements.txt
   python main.py
   ```

   - The API will be available at: [http://localhost:8000](http://localhost:8000)
   - API documentation is accessible at: [http://localhost:8000/docs](http://localhost:8000/docs)

### Running Tests

To execute tests, run the following:

```bash
cd backend
pytest tests/ -v
```

## API Reference Summary

### Current Endpoints

- **GET** `/health`: Check API health
- **GET** `/prompts`: List all prompts
- **GET** `/prompts/{id}`: Retrieve a single prompt (Currently has a bug)
- **POST** `/prompts`: Create a new prompt
- **PUT** `/prompts/{id}`: Update a prompt (Currently has issues)
- **DELETE** `/prompts/{id}`: Delete a prompt
- **GET** `/collections`: List all collections
- **GET** `/collections/{id}`: Retrieve a single collection
- **POST** `/collections`: Create a new collection
- **DELETE** `/collections/{id}`: Delete a collection (Currently has a bug)

## Usage Examples

### Creating a Prompt

To create a new prompt, send a POST request to `/prompts` with the prompt data:

```json
{
  "name": "Example Prompt",
  "template": "Hello, {{name}}!"
}
```

### Listing Prompts

GET requests to `/prompts` will return a list of all stored prompts.

## Contribution Guidelines

1. **Experimentation Encouraged**: Feel free to improve and innovate.
2. **Backend Fixes**: Focus on understanding and fixing bugs in the existing backend.
3. **Documentation**: Ensure all features and endpoints are well-documented.
4. **Testing**: Augment existing tests and implement new tests where necessary.
5. **CI/CD Integration**: Set up continuous integration and deployment.

## Tech Stack

- **Backend**: Python 3.10+, FastAPI, Pydantic
- **Frontend**: React (planned), Vite (planned)
- **Testing**: pytest
- **DevOps**: Docker, GitHub Actions (planned)

---

For further assistance, please refer to the `PROJECT_BRIEF.md` and `GRADING_RUBRIC.md` files, or reach out on the course forum.
