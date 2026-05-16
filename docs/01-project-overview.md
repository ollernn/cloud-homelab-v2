# 01 - Project Overview

## Overview

Cloud Homelab v2 is a secure hybrid cloud deployment project where a small FastAPI application is built, tested, containerized, deployed to Azure, and monitored from a local homelab environment.

The project builds on Secure Homelab v1, where a local Ubuntu Server-based homelab was created with SSH, firewall protection, fail2ban, Docker, Portainer, Uptime Kuma, Homepage and Nginx.

Cloud Homelab v2 takes the next step by moving from a local-only homelab setup into a hybrid cloud setup.

## Purpose

The purpose of this project is to demonstrate how a local application can be developed, secured, containerized, deployed to Azure, and monitored as a cloud-hosted service.

The project demonstrates practical skills in:

- Python FastAPI
- Environment-based configuration
- API key protection
- Docker and Docker Compose
- Automated testing with pytest
- GitHub Actions CI
- Azure Container Registry
- Azure Container Apps
- Public HTTP ingress
- Uptime Kuma monitoring
- Technical troubleshooting
- Technical documentation

## Project Goal

The goal of the project is to build a small but realistic cloud deployment workflow.

The workflow includes:

```text
Local FastAPI development
        ↓
Docker containerization
        ↓
Automated testing
        ↓
GitHub Actions CI
        ↓
Azure Container Registry
        ↓
Azure Container Apps
        ↓
Uptime Kuma monitoring
```

## Architecture

```text
Developer PC
│
├── FastAPI application
├── .env configuration
├── Dockerfile
├── docker-compose.yml
├── pytest tests
│
├── GitHub repository
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

## Main Components

| Component | Purpose |
|---|---|
| FastAPI | Provides the API service |
| Docker | Packages the API as a container |
| Docker Compose | Runs the container locally |
| pytest | Tests the API endpoints |
| GitHub Actions | Runs CI automatically |
| Azure Container Registry | Stores the Docker image |
| Azure Container Apps | Runs the API in Azure |
| Uptime Kuma | Monitors the Azure `/health` endpoint |
| Markdown documentation | Documents the full project process |

## API Endpoints

| Endpoint | Purpose |
|---|---|
| `/` | Root endpoint with project message |
| `/health` | Health check endpoint used for monitoring |
| `/version` | Shows service version and runtime environment |
| `/secure-info` | Protected endpoint requiring an API key |
| `/docs` | FastAPI Swagger documentation |

## Current Status

The project currently includes:

- A working FastAPI application
- Local development setup with a Python virtual environment
- Environment-based configuration using `.env`
- A protected API endpoint using an API key
- Docker and Docker Compose support
- Automated tests using pytest
- A working GitHub Actions CI workflow
- Docker image pushed to Azure Container Registry
- Azure Container App deployment
- Public API URL hosted in Azure
- Successful Azure endpoint testing
- Uptime Kuma monitoring from the local homelab
- Screenshots for documentation and portfolio use
- Azure log stream verification

## Azure Deployment

The application has been deployed to Azure using:

```text
Azure Container Registry
Azure Container Apps
```

The deployed application runs as a containerized FastAPI service with public HTTP ingress enabled on port `8000`.

The Azure deployment uses the following main resources:

| Resource | Name |
|---|---|
| Resource Group | `rg-cloud-homelab-v2` |
| Azure Container Registry | `acrcloudhomelabv2olle` |
| Container App Environment | `cae-cloud-homelab-v2-ne` |
| Azure Container App | `ca-cloud-homelab-v2-api` |
| Region | `North Europe` |

## Monitoring

Monitoring has been added using Uptime Kuma from the local Secure Homelab v1 environment.

The monitored endpoint is:

```text
/health
```

This creates a hybrid cloud connection where the local homelab monitors the Azure-hosted API.

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

The project includes basic security practices:

- Configuration is handled through environment variables.
- The real `.env` file is excluded from Git.
- `.env.example` is included as a safe template.
- `/secure-info` requires an API key.
- API keys are not hardcoded directly in the source code.
- Screenshots with API keys should have secrets masked or redacted.

## Documentation Structure

The project documentation is divided into separate files:

| File | Description |
|---|---|
| `docs/01-project-overview.md` | Project overview and architecture |
| `docs/02-local-development.md` | Local FastAPI setup |
| `docs/03-dockerization.md` | Docker and Docker Compose setup |
| `docs/04-testing-and-ci.md` | pytest and GitHub Actions CI |
| `docs/05-azure-deployment.md` | Azure deployment process |
| `docs/06-monitoring.md` | Uptime Kuma monitoring setup |
| `docs/07-azure-logs.md` | Azure log stream verification |

## Result

Cloud Homelab v2 now demonstrates a complete small-scale hybrid cloud deployment.

The project connects:

```text
Local development
Docker
GitHub Actions CI
Azure cloud deployment
Local homelab monitoring
```

This makes the project relevant for learning and demonstrating skills in cloud security, platform engineering, DevOps, hybrid infrastructure and technical documentation.

## Planned Next Steps

The next planned steps are:

- Improve deployment automation
- Add GitHub Actions CD
- Improve secrets handling
- Add a final project summary
- Continue updating the portfolio and learning log

