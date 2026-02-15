# API Reference

This document provides comprehensive details about the API endpoints available in the PromptLab application, including requests, responses, error formats, and authentication notes.

## Overview

- Base URL: `http://localhost:8000`
- Authentication: None required

## Endpoints

### Health Check

#### `GET /health`
- **Description**: Check API health status.
- **Response**:
  - **Status Code**: `200 OK`
  - **Body**:
    ```json
    {
      "status": "healthy"
    }
    ```

### Prompts

#### `GET /prompts`
- **Description**: Retrieve a list of all prompts.
- **Response**:
  - **Status Code**: `200 OK`
  - **Body**:
    ```json
    [
      {
        "id": "prompt_id",
        "name": "Prompt Name",
        "template": "Hello, {{name}}!"
      }
    ]
    ```

#### `GET /prompts/{id}`
- **Description**: Retrieve details of a specific prompt.
- **Response**:
  - **Status Code**: `200 OK`
  - **Body** (example):
    ```json
    {
      "id": "prompt_id",
      "name": "Prompt Name",
      "template": "Hello, {{name}}!"
    }
    ```
  - **Status Code**: `404 Not Found` if prompt does not exist

#### `POST /prompts`
- **Description**: Create a new prompt.
- **Request**:
  - **Body**:
    ```json
    {
      "name": "New Prompt",
      "template": "Example template"
    }
    ```
- **Response**:
  - **Status Code**: `201 Created`
  - **Body**:
    ```json
    {
      "id": "new_prompt_id",
      "name": "New Prompt",
      "template": "Example template"
    }
    ```

#### `PUT /prompts/{id}`
- **Description**: Update an existing prompt.
- **Request**:
  - **Body** (example):
    ```json
    {
      "name": "Updated Prompt",
      "template": "Updated template"
    }
    ```
- **Response**:
  - **Status Code**: `200 OK`
  - **Body** (example):
    ```json
    {
      "id": "prompt_id",
      "name": "Updated Prompt",
      "template": "Updated template"
    }
    ```

#### `DELETE /prompts/{id}`
- **Description**: Delete a specific prompt.
- **Response**:
  - **Status Code**: `204 No Content`

### Collections

#### `GET /collections`
- **Description**: Retrieve a list of all collections.
- **Response**:
  - **Status Code**: `200 OK`
  - **Body**:
    ```json
    [{
      "id": "collection_id",
      "name": "Collection Name"
    }]
    ```

#### `GET /collections/{id}`
- **Description**: Retrieve details of a specific collection.
- **Response**:
  - **Status Code**: `200 OK`
  - **Body** (example):
    ```json
    {
      "id": "collection_id",
      "name": "Collection Name"
    }
    ```
  - **Status Code**: `404 Not Found` if collection does not exist

#### `POST /collections`
- **Description**: Create a new collection.
- **Request**:
  - **Body**:
    ```json
    {
      "name": "New Collection"
    }
    ```
- **Response**:
  - **Status Code**: `201 Created`
  - **Body**:
    ```json
    {
      "id": "new_collection_id",
      "name": "New Collection"
    }
    ```

#### `DELETE /collections/{id}`
- **Description**: Delete a specific collection.
- **Response**:
  - **Status Code**: `204 No Content`

## Error Response Format

All error responses follow this format:

```json
{
  "detail": "Error message describing what went wrong."
}
```

## Authentication

- **Current Status**: No authentication is required for accessing any endpoints. This may change as the platform evolves.
