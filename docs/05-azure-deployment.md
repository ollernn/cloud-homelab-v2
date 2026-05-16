# 05 - Azure Deployment

## Overview

The FastAPI application has been deployed to Azure using Azure Container Registry and Azure Container Apps.

This step moves the project from local development and Docker-based execution into a real cloud environment.

## Purpose

The purpose of this deployment is to demonstrate how a locally developed and containerized API can be deployed as a cloud service.

This deployment shows practical skills in:

- Azure resource management
- Azure Container Registry
- Azure Container Apps
- container-based cloud deployment
- public HTTP ingress
- environment variables in cloud environments
- basic cloud security considerations
- troubleshooting Azure deployment issues
- technical documentation

## Azure Resources

The deployment uses the following Azure resources:

| Resource | Name | Purpose |
|---|---|---|
| Resource Group | `rg-cloud-homelab-v2` | Groups all Azure resources for the project |
| Azure Container Registry | `acrcloudhomelabv2olle` | Stores the Docker image |
| Container App Environment | `cae-cloud-homelab-v2-ne` | Runtime environment for the Container App |
| Azure Container App | `ca-cloud-homelab-v2-api` | Runs the FastAPI container |
| Log Analytics Workspace | Automatically generated | Stores logs and monitoring data |

## Deployment Region

The final deployment was created in:

```text
North Europe
```

Earlier attempts were made in Sweden Central and West Europe, but the student Azure subscription and regional capacity caused provisioning issues.

The successful deployment was completed using North Europe.

## Container Image

The Docker image was built locally and pushed to Azure Container Registry.

Image:

```text
acrcloudhomelabv2olle.azurecr.io/cloud-homelab-v2-api:1.0.0
```

## Build and Push Process

The image was built with:

```powershell
docker build -t acrcloudhomelabv2olle.azurecr.io/cloud-homelab-v2-api:1.0.0 .
```

The image was pushed to Azure Container Registry with:

```powershell
docker push acrcloudhomelabv2olle.azurecr.io/cloud-homelab-v2-api:1.0.0
```

The repository and tag were verified with:

```powershell
az acr repository list --name acrcloudhomelabv2olle --output table
```

```powershell
az acr repository show-tags --name acrcloudhomelabv2olle --repository cloud-homelab-v2-api --output table
```

## Container App Configuration

The Container App was configured with:

| Setting | Value |
|---|---|
| App name | `ca-cloud-homelab-v2-api` |
| Image source | Azure Container Registry |
| Image | `cloud-homelab-v2-api` |
| Tag | `1.0.0` |
| Ingress | Enabled |
| Ingress traffic | Allow traffic from anywhere |
| Ingress type | HTTP |
| Transport | Auto |
| Target port | `8000` |
| CPU | `0.5` |
| Memory | `1 Gi` |
| Workload profile | Consumption |

## Environment Variables

The Azure Container App uses environment variables to configure the application.

| Variable | Purpose |
|---|---|
| `APP_NAME` | Sets the application name |
| `APP_VERSION` | Sets the application version |
| `APP_ENV` | Identifies the runtime environment |
| `API_KEY` | Used by the protected endpoint |

Example structure:

```env
APP_NAME=Cloud Homelab v2 API
APP_VERSION=1.0.0
APP_ENV=azure
API_KEY=<your-api-key>
```

The local `.env` file is not committed to GitHub.

The API key used during deployment was a development test value. In documentation and screenshots, secrets should be masked or redacted.

## Public API URL

The deployed API is available through the Azure Container Apps public URL.

Example format:

```text
https://ca-cloud-homelab-v2-api.<generated-id>.northeurope.azurecontainerapps.io
```

## Tested Endpoints

The following endpoints were tested successfully in Azure:

| Endpoint | Result |
|---|---|
| `/` | Returned project startup message |
| `/health` | Returned healthy status |
| `/version` | Returned service version and Azure environment |
| `/docs` | Opened FastAPI Swagger documentation |
| `/secure-info` | Returned protected response when an API key was provided |

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

## Protected Endpoint Testing

The protected endpoint was tested through FastAPI Swagger documentation.

Endpoint:

```text
GET /secure-info
```

Header used:

```text
x-api-key: <your-api-key>
```

The value must match the `API_KEY` environment variable configured in the Azure Container App.

For documentation purposes, the actual API key should not be shown.

## Screenshots

Screenshots were saved in the `screenshots/` folder.

Recommended screenshot files:

```text
azure-container-app-overview.png
azure-root-endpoint.png
azure-health-endpoint.png
azure-version-endpoint.png
azure-swagger-docs.png
azure-secure-info-endpoint.png
```

The screenshot for the protected endpoint should have the API key masked or redacted.

## Issues Encountered

During deployment, several Azure-specific issues occurred.

### Sweden Central limitation

The first attempt used Sweden Central, but the subscription could not create a Container App Environment in that region.

### West Europe capacity issue

A later attempt in West Europe resulted in a managed environment capacity error.

### Failed environment cleanup

A failed Container App Environment was created and had to be removed before retrying with a new environment name and region.

### Ingress validation error

A validation error occurred because the target port was not correctly set.

The error was related to additional port mappings being configured without a valid ingress target port.

The issue was fixed by:

- setting the main ingress target port to `8000`
- leaving additional TCP port mappings empty

## Final Result

The Azure deployment was successful.

The project now includes:

- a FastAPI API running locally
- environment-based configuration
- API key protection
- Docker containerization
- Azure Container Registry image storage
- Azure Container Apps deployment
- public HTTP ingress
- successful Azure endpoint testing
- screenshots for documentation and portfolio use

## Security Notes

This deployment uses a development API key for testing.

For a production-like setup, the API key should be handled through a more secure secret management approach.

Future improvements may include:

- storing secrets in GitHub Actions secrets
- using Azure Key Vault
- using managed identity where appropriate
- rotating API keys
- separating test, local and production configuration

## Next Step

The next step is to add monitoring for the Azure-hosted API.

The planned monitoring setup is:

- monitor `/health` using Uptime Kuma from the local homelab
- review Azure logs through the Azure Portal
- document the monitoring setup in `docs/06-monitoring.md`
