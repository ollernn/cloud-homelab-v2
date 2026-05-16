# 06 - Monitoring

## Overview

Monitoring was added to the Cloud Homelab v2 project to verify that the Azure-hosted API is reachable and healthy after deployment.

The monitoring setup connects the local homelab environment from Secure Homelab v1 with the cloud deployment in Azure.

This creates a simple hybrid monitoring setup:

```text
Secure Homelab v1
│
└── Uptime Kuma
    │
    └── Monitors Azure Container App
        │
        └── Cloud Homelab v2 API /health
```

## Purpose

The purpose of monitoring is to make sure that the deployed API is available and responding correctly.

This step demonstrates practical skills in:

- Service monitoring
- Health check endpoints
- Hybrid infrastructure monitoring
- Cloud service availability checks
- Basic operational thinking
- Documentation of deployed services

## Monitored Service

The monitored service is the FastAPI application deployed to Azure Container Apps.

Azure Container App:

```text
ca-cloud-homelab-v2-api
```

Health check endpoint:

```text
/health
```

Full monitored URL:

```text
https://ca-cloud-homelab-v2-api.redfield-6ff1553c.northeurope.azurecontainerapps.io/health
```

## Why `/health` Is Used

The `/health` endpoint is used because it provides a simple and reliable way to check if the API is running.

Expected response:

```json
{
  "status": "healthy",
  "environment": "azure"
}
```

This confirms that:

- the Azure Container App is reachable
- the FastAPI application is running
- the correct cloud environment variable is being used
- the service can respond to HTTP requests

## Monitoring Tool

Monitoring is performed using:

```text
Uptime Kuma
```

Uptime Kuma was already part of the local Secure Homelab v1 environment.

This means the local homelab is now used to monitor a cloud-hosted service.

## Uptime Kuma Configuration

A new monitor was created with the following configuration:

| Setting | Value |
|---|---|
| Monitor type | `HTTP(s)` |
| Friendly name | `Cloud Homelab v2 API` |
| URL | `https://ca-cloud-homelab-v2-api.redfield-6ff1553c.northeurope.azurecontainerapps.io/health` |
| Method | `GET` |
| Heartbeat interval | `60 seconds` |
| Accepted status code | `200` |

## Monitoring Result

The monitor successfully reached the Azure-hosted API and reported the service as up.

Result:

```text
Status: Up
Response: 200 OK
Uptime: 100%
```

The response time was also shown in Uptime Kuma, confirming that the service was reachable from the homelab monitoring environment.

## Screenshot

The monitoring result was documented with a screenshot stored in:

```text
screenshots/monitoring-uptime-kuma-overview.png
```

The screenshot shows:

- the monitored Azure `/health` endpoint
- status as `Up`
- response time
- uptime percentage
- Uptime Kuma running as part of the homelab monitoring setup

## Hybrid Cloud Connection

This step is important because it connects the previous local homelab project with the new Azure cloud deployment.

The setup can be described as:

```text
Local homelab monitoring
        ↓
Azure-hosted containerized API
        ↓
Public health endpoint
        ↓
Operational visibility
```

This makes the project more than just a cloud deployment. It also shows basic operational monitoring across local and cloud environments.

## Notes About Cold Starts

Azure Container Apps may scale down when not in use, depending on the scaling configuration.

If the service has scaled down, the first request may take longer because the container needs to start again.

This is known as a cold start.

For this project, Uptime Kuma checks the `/health` endpoint every 60 seconds, which helps verify that the service remains reachable.

## Security Considerations

Only the `/health` endpoint is monitored.

The protected `/secure-info` endpoint still requires an API key and is not used for public uptime monitoring.

This keeps the monitoring simple while avoiding unnecessary exposure of protected endpoint behavior.

## Final Result

Monitoring was successfully added to the project.

The project now includes:

- a FastAPI API running in Azure
- a public health endpoint
- Uptime Kuma monitoring from the local homelab
- successful uptime status
- screenshot documentation
- a clear hybrid cloud monitoring connection

## Next Step

The next steps are:

- update the main `README.md`
- create a final project summary
- optionally add GitHub Actions CD
- improve secrets handling
