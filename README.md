# AI-Based Data Analyst

A Python service for uploading CSV datasets and returning dataset profiles through a FastAPI API.

## Current API

- GET /health — reports service health and the configured environment
- POST /upload — accepts a CSV upload and returns a dataset identifier
- GET /datasets/{data_uid}/profile — returns a profile for an uploaded dataset

Uploads are limited by the configured maximum size. The current API accepts CSV files.

## Technology and layout

- Python 3.10+
- FastAPI and Uvicorn
- Pydantic settings
- Pandas-based profiling

    src/analyst/api/          FastAPI application and routes
    src/analyst/analysis/     Dataset aggregation and profiling
    src/analyst/core/         Application configuration
    src/analyst/data/         Upload storage
    src/analyst/llm/          LLM client and planning modules
    tests/                    API and analysis tests
    docs/adr/                 Architecture decisions

## Run locally

Create an environment, install the project with its development extras, and copy the example configuration:

    python -m venv .venv
    # Windows PowerShell
    .venv\Scripts\Activate.ps1
    # macOS or Linux
    source .venv/bin/activate
    python -m pip install -e ".[dev]"
    cp .env.example .env

On Windows, copy the environment file with:

    Copy-Item .env.example .env

Set any required credentials in the local .env file. Do not commit populated credentials.

Start the API from the repository root:

    uvicorn analyst.api.main:app --reload --app-dir src

Open the interactive API documentation at /docs on the local server.

## Tests

Run the test suite with:

    pytest
