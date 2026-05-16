# Cloud Homelab v2 — Secure Hybrid Cloud Deployment

## Overview

Cloud Homelab v2 is a practical cloud security and platform engineering project where a small FastAPI application is built, tested, containerized, deployed to Azure, and monitored from a local homelab environment.

The project builds on my previous Secure Homelab v1 project, where I created a local Ubuntu Server-based homelab with SSH, UFW, fail2ban, Docker, Portainer, Uptime Kuma, Homepage and Nginx.

This project takes the next step by moving from a local-only homelab setup to a hybrid cloud deployment.

## Purpose

The purpose of this project is to demonstrate how a local application can be developed, secured, containerized, deployed to Azure, and monitored as a real cloud-hosted service.

The project focuses on practical skills in:

- Python FastAPI
- Docker and Docker Compose
- Environment-based configuration
- API key-based access control
- Automated testing with pytest
- GitHub Actions CI
- Azure Container Registry
- Azure Container Apps
- Public cloud deployment
- Uptime Kuma monitoring
- Technical documentation
- Portfolio-based project presentation

## Current Status

The project currently includes:

- A working FastAPI API
- Local development setup with Python virtual environment
- Environment-based configuration using `.env`
- A protected API endpoint using an API key
- Docker and Docker Compose support
- Automated tests with pytest
- GitHub Actions CI workflow
- Docker image pushed to Azure Container Registry
- Azure Container App deployment
- Public API URL hosted in Azure
- Uptime Kuma monitoring from the local homelab
- Screenshots and technical documentation

## Architecture

```text
Developer PC
│
├── FastAPI application
├── Dockerfile
├── docker-compose.yml
├── pytest tests
│
├── GitHub Repository
│   ├── Source code
│   ├── Documentation
│   ├── Screenshots
│   └── GitHub Actions CI
│
├── Azure
│   ├── Azure Container Registry
│   ├── Azure Container Apps Environment
│   ├── Azure Container App
│   └── Log Analytics
│
└── Secure Homelab v1
    └── Uptime Kuma
        └── Monitors Azure /health endpoint
```

## Tech Stack

| Area | Technology |
|---|---|
| API | FastAPI |
| Language | Python |
| Local server | Uvicorn |
| Containerization | Docker |
| Local container orchestration | Docker Compose |
| Testing | pytest |
| CI | GitHub Actions |
| Cloud registry | Azure Container Registry |
| Cloud runtime | Azure Container Apps |
| Monitoring | Uptime Kuma |
| Documentation | Markdown |
| Version control | Git and GitHub |

## API Endpoints

| Endpoint | Description |
|---|---|
| `/` | Root endpoint with project message |
| `/health` | Health check endpoint used for monitoring |
| `/version` | Shows service version and runtime environment |
| `/secure-info` | Protected endpoint requiring an API key |
| `/docs` | FastAPI Swagger documentation |

## Example Responses

### Root endpoint

```json
{
  "message": "Cloud Homelab v2 API is running",
  "project": "Secure Hybrid Cloud Deployment"
}
```

### Health endpoint

```json
{
  "status": "healthy",
  "environment": "azure"
}
```

### Version endpoint

```json
{
  "service": "cloud-homelab-v2-api",
  "version": "1.0.0",
  "environment": "azure"
}
```

### Protected endpoint

```json
{
  "message": "This endpoint is protected with an API key.",
  "environment": "azure",
  "security": "API key authentication enabled"
}
```

## Local Development

### 1. Clone the repository

```powershell
git clone https://github.com/ollernn/cloud-homelab-v2.git
cd cloud-homelab-v2
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

### 3. Activate the virtual environment

```powershell
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```powershell
pip install -r requirements.txt
```

### 5. Create a local `.env` file

Use `.env.example` as a template.

Example:

```env
APP_NAME=Cloud Homelab v2 API
APP_VERSION=1.0.0
APP_ENV=local
API_KEY=change-me
```

The real `.env` file is not committed to GitHub.

### 6. Run the API locally

```powershell
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

## Docker Usage

The application can also be run locally inside Docker.

### Build and run with Docker Compose

```powershell
docker compose up --build
```

The API will be available at:

```text
http://127.0.0.1:8000
```

### Stop the container

```powershell
docker compose down
```

## Testing

The project uses pytest for automated testing.

Run tests locally with:

```powershell
pytest
```

Current tests verify that:

- `/health` returns status code 200
- `/health` returns healthy status
- `/version` returns service information
- `/secure-info` blocks requests without an API key
- `/secure-info` allows requests with a valid API key

Expected result:

```text
4 passed
```

## GitHub Actions CI

GitHub Actions is used for continuous integration.

The workflow runs automatically on:

- push to `main`
- pull requests to `main`

The CI pipeline:

```text
Checkout repository
Set up Python
Install dependencies
Run pytest
```

Workflow file:

```text
.github/workflows/ci.yml
```

## Azure Deployment

The application has been deployed to Azure using Azure Container Registry and Azure Container Apps.

### Azure resources

| Resource | Name |
|---|---|
| Resource Group | `rg-cloud-homelab-v2` |
| Azure Container Registry | `acrcloudhomelabv2olle` |
| Container App Environment | `cae-cloud-homelab-v2-ne` |
| Azure Container App | `ca-cloud-homelab-v2-api` |
| Region | `North Europe` |

### Container image

```text
acrcloudhomelabv2olle.azurecr.io/cloud-homelab-v2-api:1.0.0
```

### Azure Container App configuration

| Setting | Value |
|---|---|
| Ingress | Enabled |
| Ingress traffic | Allow traffic from anywhere |
| Ingress type | HTTP |
| Target port | `8000` |
| CPU | `0.5` |
| Memory | `1 Gi` |
| Workload profile | Consumption |

## Monitoring

The Azure-hosted API is monitored using Uptime Kuma from the local Secure Homelab v1 environment.

Monitored endpoint:

```text
/health
```

Monitoring setup:

| Setting | Value |
|---|---|
| Monitor type | HTTP(s) |
| Friendly name | Cloud Homelab v2 API |
| Method | GET |
| Heartbeat interval | 60 seconds |
| Accepted status code | 200 |

This connects the local homelab to the Azure deployment and creates a simple hybrid monitoring setup.

```text
Local Uptime Kuma
        ↓
Azure Container App
        ↓
/health endpoint
        ↓
Status: Up
```

## Security Notes

This project includes basic security practices:

- Environment variables are used for configuration.
- The real `.env` file is excluded from Git.
- `.env.example` is used as a safe template.
- `/secure-info` requires an API key.
- API keys are not hardcoded directly in the source code.
- Screenshots with API keys should have secrets masked or redacted.

The API key used during development is a test value and should not be used as a production secret.

## Documentation

Detailed documentation is available in the `docs/` folder.

| File | Description |
|---|---|
| `docs/01-project-overview.md` | Project overview and purpose |
| `docs/02-local-development.md` | Local FastAPI development setup |
| `docs/03-dockerization.md` | Docker and Docker Compose setup |
| `docs/04-testing-and-ci.md` | pytest and GitHub Actions CI |
| `docs/05-azure-deployment.md` | Azure deployment process |
| `docs/06-monitoring.md` | Uptime Kuma monitoring setup |

## Screenshots

Screenshots are stored in the `screenshots/` folder.

Recommended screenshot files:

```text
azure-container-app-overview.png
azure-root-endpoint.png
azure-health-endpoint.png
azure-version-endpoint.png
azure-swagger-docs.png
azure-secure-info-endpoint.png
monitoring-uptime-kuma-overview.png
```

## Troubleshooting Notes

During deployment, several real-world issues were encountered and solved:

- Azure Container Apps Environment could not be created in Sweden Central.
- West Europe returned a managed environment capacity error.
- A failed Container Apps Environment had to be cleaned up.
- Azure Portal validation failed when the ingress target port was not set correctly.
- The correct ingress target port was `8000`.
- Additional TCP port mappings had to be left empty.

These issues were documented as part of the project because troubleshooting is an important part of cloud and platform engineering work.

## Project Result

The project successfully demonstrates a complete small-scale hybrid cloud deployment:

```text
Local FastAPI development
        ↓
Docker containerization
        ↓
Automated testing with pytest
        ↓
GitHub Actions CI
        ↓
Azure Container Registry
        ↓
Azure Container Apps
        ↓
Uptime Kuma monitoring
```

## Next Steps

Planned next steps:

- Review Azure logs
- Document Azure log usage
- Improve deployment automation
- Add GitHub Actions CD
- Replace development API key with a more secure secret handling approach
- Add final project summary
- Continue improving the portfolio project page

## Repository

```text
https://github.com/ollernn/cloud-homelab-v2
```
