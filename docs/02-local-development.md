# 02 - Local Development

## Overview

The API is built with FastAPI and can be run locally during development.

Local development is used to build and test the application before running it in Docker or deploying it to Azure.

## Local Requirements

- Python
- pip
- Python virtual environment
- FastAPI
- Uvicorn

## Setup

Create a virtual environment:

```powershell
python -m venv .venv
```

Activate the virtual environment:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## Running the API Locally

Start the API with:

```powershell
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## Available Endpoints

| Endpoint | Description |
|---|---|
| `/` | Root endpoint |
| `/health` | Health check endpoint |
| `/version` | Shows service version and environment |
| `/secure-info` | Protected endpoint requiring an API key |
| `/docs` | FastAPI Swagger documentation |

## Environment Variables

The application uses environment variables for configuration.

Example:

```env
APP_NAME=Cloud Homelab v2 API
APP_VERSION=1.0.0
APP_ENV=local
API_KEY=change-me
```

The real `.env` file is not committed to GitHub.

Instead, `.env.example` is included to show which variables are required.

## Local Security Note

The `/secure-info` endpoint requires an API key sent through the `x-api-key` header.

Example local development API key:

```text
dev-secret-key
```

This key is only used for local development and testing.
