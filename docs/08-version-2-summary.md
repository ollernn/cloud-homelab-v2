# 08 - Version 2 Summary

## Overview

Cloud Homelab v2 is a secure hybrid cloud deployment project where a small FastAPI API was built, tested, containerized, deployed to Azure and monitored from a local homelab environment.

The project builds on Secure Homelab v1, where a local Ubuntu Server-based homelab was created with SSH, firewall protection, fail2ban, Docker, Portainer, Uptime Kuma, Homepage and Nginx.

Version 2 extends that local foundation into the cloud by deploying a containerized API to Azure Container Apps and monitoring it from the local homelab.

## Purpose

The purpose of Cloud Homelab v2 was to practice and demonstrate a complete small-scale cloud deployment workflow.

The project was designed to improve practical skills in:

- Python FastAPI
- Docker and Docker Compose
- Environment-based configuration
- API key-based access control
- Automated testing with pytest
- GitHub Actions CI
- Azure Container Registry
- Azure Container Apps
- Public HTTP ingress
- Uptime Kuma monitoring
- Azure log stream verification
- Technical troubleshooting
- Technical documentation
- Portfolio project presentation

## Final Version 2 Architecture

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
│   └── Log Analytics / Log Stream
│
└── Secure Homelab v1
    └── Uptime Kuma
        └── Monitors Azure /health endpoint
```

## Main Components

| Component | Role |
|---|---|
| FastAPI | API framework |
| Python | Application language |
| Docker | Containerization |
| Docker Compose | Local container execution |
| pytest | Automated testing |
| GitHub Actions | Continuous integration |
| Azure Container Registry | Stores the Docker image |
| Azure Container Apps | Runs the API in Azure |
| Uptime Kuma | Monitors the Azure API |
| Azure Log Stream | Shows runtime logs and requests |
| Markdown documentation | Documents the full project |

## API Functionality

The API includes the following endpoints:

| Endpoint | Purpose |
|---|---|
| `/` | Returns a basic project message |
| `/health` | Health check endpoint used for monitoring |
| `/version` | Shows service version and runtime environment |
| `/secure-info` | Protected endpoint requiring an API key |
| `/docs` | FastAPI Swagger documentation |

## Security Features

The project includes basic security practices:

- Configuration is handled through environment variables.
- The real `.env` file is excluded from Git.
- `.env.example` is used as a safe template.
- `/secure-info` requires an API key.
- API keys are not hardcoded directly in the source code.
- Documentation uses placeholders instead of real secret values.
- Screenshots with API keys are masked or redacted.

The project currently uses a development test API key. A future improvement would be to use a more secure secret management solution such as Azure Key Vault or GitHub Actions secrets for deployment automation.

## Local Development

The API was first built and tested locally using FastAPI and Uvicorn.

Local development confirmed that:

- the API could start successfully
- `/health` returned a healthy status
- `/version` returned service information
- `/secure-info` blocked unauthorized requests
- `/secure-info` allowed requests with a valid API key
- Swagger documentation was available through `/docs`

## Dockerization

The application was then containerized using Docker.

Dockerization confirmed that:

- the API could run inside a container
- environment variables could be passed into the container
- the same application could run locally and later in Azure
- the project was ready for cloud deployment

The Docker setup includes:

```text
Dockerfile
docker-compose.yml
.dockerignore
```

## Testing and CI

Automated tests were added with pytest.

The tests verify that:

- `/health` returns status code 200
- `/health` returns a healthy response
- `/version` returns service information
- `/secure-info` blocks requests without an API key
- `/secure-info` allows requests with a valid API key

GitHub Actions CI was added to run tests automatically on:

- push to `main`
- pull requests to `main`

The CI workflow completed successfully and remained green after later documentation updates.

## Azure Deployment

The Docker image was pushed to Azure Container Registry and deployed to Azure Container Apps.

Main Azure resources:

| Resource | Name |
|---|---|
| Resource Group | `rg-cloud-homelab-v2` |
| Azure Container Registry | `acrcloudhomelabv2olle` |
| Container App Environment | `cae-cloud-homelab-v2-ne` |
| Azure Container App | `ca-cloud-homelab-v2-api` |
| Region | `North Europe` |

The final Azure deployment used:

```text
acrcloudhomelabv2olle.azurecr.io/cloud-homelab-v2-api:1.0.0
```

The Container App was configured with:

| Setting | Value |
|---|---|
| Ingress | Enabled |
| Ingress traffic | Allow traffic from anywhere |
| Ingress type | HTTP |
| Target port | `8000` |
| CPU | `0.5` |
| Memory | `1 Gi` |
| Workload profile | Consumption |

## Azure Deployment Result

The deployed Azure API was tested successfully.

Confirmed working endpoints:

| Endpoint | Result |
|---|---|
| `/` | Returned the project startup message |
| `/health` | Returned healthy status and Azure environment |
| `/version` | Returned service version and Azure environment |
| `/docs` | Opened FastAPI Swagger documentation |
| `/secure-info` | Returned protected response with valid API key |

## Monitoring

Monitoring was added with Uptime Kuma from the local Secure Homelab v1 environment.

The monitored endpoint is:

```text
/health
```

This created a hybrid monitoring setup:

```text
Local Uptime Kuma
        ↓
Azure Container App
        ↓
/health endpoint
        ↓
Status: Up
```

Uptime Kuma confirmed that the Azure-hosted API was reachable and returned `200 OK`.

## Azure Logs

Azure Log Stream was used to verify runtime behavior.

The logs showed:

- successful connection to the container log stream
- repeated `/health` requests
- `/version` requests
- `200 OK` responses
- monitoring activity from Uptime Kuma

This confirmed that the API was running and receiving HTTP requests inside Azure.

## Screenshots

Screenshots were saved in the `screenshots/` folder.

The screenshots document:

- Azure Container App overview
- root endpoint
- health endpoint
- version endpoint
- Swagger documentation
- protected endpoint with masked API key
- Uptime Kuma monitoring
- Azure log stream

Recommended screenshot files:

```text
azure-container-app-overview.png
azure-root-endpoint.png
azure-health-endpoint.png
azure-version-endpoint.png
azure-swagger-docs.png
azure-secure-info-endpoint.png
monitoring-uptime-kuma-overview.png
azure-log-stream.png
```

## Problems Encountered and Solved

Several realistic cloud deployment issues were encountered.

### Azure region limitations

The first deployment attempts in Sweden Central and West Europe had issues related to subscription limitations and regional capacity.

The final successful deployment was completed in North Europe.

### Failed Container App Environment

A failed Container Apps Environment had to be removed before continuing with a new environment name and region.

### Ingress configuration error

Azure Portal validation failed because the ingress target port was not correctly set.

The issue was solved by:

- setting the main ingress target port to `8000`
- leaving additional TCP port mappings empty

### Secret exposure risk

A test API key appeared in early screenshots and documentation.

This was fixed by:

- masking the API key in screenshots
- replacing real-looking values with placeholders in documentation
- documenting that real secrets should not be committed or exposed

## Final Result

Cloud Homelab v2 successfully demonstrates a complete small-scale hybrid cloud deployment.

The final workflow is:

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
        ↓
Azure log verification
```

## What This Project Demonstrates

This project demonstrates practical knowledge in:

- building an API
- securing an endpoint with API key logic
- separating configuration from source code
- containerizing an application
- testing endpoints automatically
- setting up CI with GitHub Actions
- deploying a containerized app to Azure
- configuring public ingress
- monitoring a cloud service from a local homelab
- reviewing cloud logs
- documenting a technical project professionally

## Current Limitations

The current version is intentionally small and focused.

Current limitations:

- API key handling is basic
- deployment is not fully automated yet
- no database is connected
- no custom domain is configured
- no HTTPS certificate management beyond Azure’s default endpoint
- no infrastructure as code is used yet
- no Azure Key Vault integration is used yet

## Future Improvements

Possible next improvements:

- Add GitHub Actions CD for automatic Azure deployment
- Store production secrets using Azure Key Vault
- Use GitHub Actions secrets for deployment credentials
- Add a custom domain
- Add a more advanced monitoring dashboard
- Add alerts for downtime
- Add Infrastructure as Code with Terraform or Bicep
- Add a small database-backed feature
- Add authentication with OAuth or JWT
- Add a final portfolio-focused architecture diagram

## Portfolio Summary

Short portfolio description:

```text
A secure hybrid cloud deployment project where I built a FastAPI service, containerized it with Docker, tested it with pytest, deployed it to Azure Container Apps, and monitored it from my local homelab using Uptime Kuma.
```

## Final Status

Version 2 is complete as a functional cloud deployment milestone.

The project now includes:

- working source code
- local development setup
- Docker support
- automated tests
- GitHub Actions CI
- Azure deployment
- public API endpoint
- Uptime Kuma monitoring
- Azure log verification
- screenshots
- documentation
- portfolio-ready project material
