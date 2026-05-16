# 03 - Dockerization

## Overview

The FastAPI application can be run inside a Docker container.

This makes the application easier to run consistently across local development, servers and cloud environments.

Dockerization is an important step because the same container image can be used locally and later deployed to Azure.

## Purpose

Dockerization is used in this project to package the application together with its runtime environment.

This helps ensure that the same application can run:

- locally on the developer machine
- inside Docker Compose
- later in Azure as a containerized cloud service

## Files

The Docker setup uses the following files:

| File | Purpose |
|---|---|
| `Dockerfile` | Defines how the application image is built |
| `docker-compose.yml` | Defines how the container is started locally |
| `.dockerignore` | Excludes unnecessary or sensitive files from the Docker image |
| `.env` | Provides local environment variables to Docker Compose |
| `.env.example` | Shows which environment variables are required |

## Dockerfile

The `Dockerfile` uses a slim Python image, installs the project dependencies and starts the FastAPI application with Uvicorn.

Main steps:

```text
Use Python base image
Set working directory
Copy requirements.txt
Install Python dependencies
Copy application code
Expose port 8000
Start Uvicorn
```

The application listens on port:

```text
8000
```

## Docker Compose

Docker Compose is used to run the application locally in a container.

The Docker Compose service is named:

```text
cloud-homelab-api
```

The container is named:

```text
cloud-homelab-v2-api
```

## Environment Variables

Docker Compose loads environment variables from:

```text
.env
```

Example `.env.example` structure:

```env
APP_NAME=Cloud Homelab v2 API
APP_VERSION=1.0.0
APP_ENV=local
API_KEY=change-me
```

The real `.env` file is excluded from Git using `.gitignore`.

This means that sensitive or local-only values should not be committed to GitHub.

## Docker Ignore

The `.dockerignore` file prevents unnecessary or sensitive files from being copied into the Docker image.

Examples of excluded files and folders:

```text
.venv
__pycache__
.pytest_cache
.git
.env
.vscode
.idea
*.log
```

This helps keep the Docker image smaller and avoids copying local secrets into the image.

## Build and Run

Start the application with Docker Compose:

```powershell
docker compose up --build
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## Available Endpoints

After starting the container, the following endpoints can be tested:

| Endpoint | Description |
|---|---|
| `/` | Root endpoint with project message |
| `/health` | Health check endpoint |
| `/version` | Shows service version and environment |
| `/secure-info` | Protected endpoint requiring an API key |
| `/docs` | FastAPI Swagger documentation |

## Testing the Protected Endpoint

The protected endpoint can be tested through the Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

Open:

```text
GET /secure-info
```

Then provide the API key through the `x-api-key` header.

Example:

```text
x-api-key: <your-api-key>
```

The value must match the `API_KEY` value in the local `.env` file.

## Stop the Container

Stop the running container with:

```powershell
CTRL + C
```

Then remove the container network with:

```powershell
docker compose down
```

## Result

The FastAPI application now runs successfully inside Docker.

This confirms that:

- the application can be containerized
- Docker Compose can start the API locally
- environment variables can be passed into the container
- the `/health`, `/version` and `/docs` endpoints work inside Docker
- the protected `/secure-info` endpoint works when a valid API key is provided

## Next Step

After Dockerization, the project was ready for:

- automated testing with pytest
- GitHub Actions CI
- Azure Container Registry
- Azure Container Apps deployment
