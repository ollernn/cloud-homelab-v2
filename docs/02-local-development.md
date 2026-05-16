# 02 - Local Development

## Overview

The API is built with FastAPI and can be run locally during development.

Local development is used to build and test the application before running it in Docker or deploying it to Azure.

This step verifies that the application works correctly before it is packaged as a container and deployed to the cloud.

## Purpose

The purpose of the local development setup is to create a simple and reliable development workflow.

This includes:

- creating a Python virtual environment
- installing dependencies
- running the FastAPI application locally
- testing API endpoints in the browser
- verifying environment-based configuration
- testing the protected API endpoint before Docker and Azure deployment

## Local Requirements

- Python
- pip
- Python virtual environment
- FastAPI
- Uvicorn

## Project Structure

The main local application files are:

```text
app/
├── __init__.py
├── main.py
├── config.py
└── security.py
```

| File | Purpose |
|---|---|
| `app/main.py` | Defines the FastAPI application and API endpoints |
| `app/config.py` | Loads configuration from environment variables |
| `app/security.py` | Handles API key verification |
| `.env` | Local environment variables, not committed to Git |
| `.env.example` | Example environment file committed to Git |

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

## Environment Variables

The application uses environment variables for configuration.

Create a local `.env` file based on `.env.example`.

Example local `.env` file:

```env
APP_NAME=Cloud Homelab v2 API
APP_VERSION=1.0.0
APP_ENV=local
API_KEY=change-me
```

The real `.env` file is not committed to GitHub.

Instead, `.env.example` is included to show which variables are required.

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
| `/` | Root endpoint with project message |
| `/health` | Health check endpoint |
| `/version` | Shows service version and environment |
| `/secure-info` | Protected endpoint requiring an API key |
| `/docs` | FastAPI Swagger documentation |

## Testing Endpoints Locally

The following endpoints can be tested directly in the browser:

```text
http://127.0.0.1:8000/
http://127.0.0.1:8000/health
http://127.0.0.1:8000/version
http://127.0.0.1:8000/docs
```

The protected endpoint can be tested through Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

In Swagger, open:

```text
GET /secure-info
```

Then use:

```text
x-api-key: <your-api-key>
```

## Example Local Responses

### Health endpoint

```json
{
  "status": "healthy",
  "environment": "local"
}
```

### Version endpoint

```json
{
  "service": "cloud-homelab-v2-api",
  "version": "1.0.0",
  "environment": "local"
}
```

### Protected endpoint

```json
{
  "message": "This endpoint is protected with an API key.",
  "environment": "local",
  "security": "API key authentication enabled"
}
```

## Local Security Note

The `/secure-info` endpoint requires an API key sent through the `x-api-key` header.

The API key is loaded from the local `.env` file.

This shows a basic example of environment-based secret handling.

The development key is only used for local testing and should not be used as a production secret.

## Result

The local development setup was completed successfully.

The FastAPI application can run locally, load environment variables, expose public endpoints, and protect `/secure-info` with an API key.

This local setup was later used as the foundation for:

- Dockerization
- automated testing
- GitHub Actions CI
- Azure deployment
- Uptime Kuma monitoring
