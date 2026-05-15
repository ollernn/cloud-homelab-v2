# 03 - Dockerization

## Overview

The FastAPI application can be run inside a Docker container.

This makes the application easier to run consistently across local development, servers and cloud environments.

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
| `/` | Root endpoint |
| `/health` | Health check endpoint |
| `/version` | Shows service version and environment |
| `/secure-info` | Protected endpoint requiring an API key |
| `/docs` | FastAPI Swagger documentation |

## Environment Variables

Docker Compose loads environment variables from:

```text
.env
```

The `.env` file contains local configuration such as:

```env
APP_NAME=Cloud Homelab v2 API
APP_VERSION=1.0.0
APP_ENV=local
API_KEY=dev-secret-key
```

The `.env` file is excluded from Git using `.gitignore`.

The `.env.example` file is committed to GitHub to show which variables are required.

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

This means the project is ready for the next steps:

- automated testing
- GitHub Actions CI
- Azure container deployment
