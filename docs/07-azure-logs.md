# 07 - Azure Logs

## Overview

Azure logs were reviewed to verify that the deployed Container App is running correctly and receiving HTTP requests.

This step adds basic operational visibility to the Cloud Homelab v2 project.

## Purpose

The purpose of reviewing Azure logs is to understand how the deployed API behaves after it has been deployed to Azure.

This step demonstrates practical skills in:

- using Azure Portal for troubleshooting
- reviewing Container App log streams
- verifying incoming requests
- confirming successful HTTP responses
- connecting monitoring activity with application logs
- documenting operational behavior

## Azure Resource

The logs were reviewed for the Azure Container App:

```text
ca-cloud-homelab-v2-api
```

Resource group:

```text
rg-cloud-homelab-v2
```

Region:

```text
North Europe
```

## Log Stream

The Azure Container App log stream was opened through the Azure Portal.

The log stream connected successfully to the running container.

The logs showed that the application was receiving HTTP requests and responding correctly.

## Observed Requests

The log stream showed repeated requests to:

```text
/health
```

It also showed a request to:

```text
/version
```

Example log behavior:

```text
GET /health HTTP/1.1 200 OK
GET /version HTTP/1.1 200 OK
```

This confirms that the deployed FastAPI application is reachable and responding successfully.

## Connection to Monitoring

The repeated `/health` requests are expected because Uptime Kuma monitors the Azure API through the `/health` endpoint.

This shows that the local homelab monitoring setup is actively checking the Azure-hosted service.

```text
Uptime Kuma
    ↓
Azure Container App /health
    ↓
Azure log stream
    ↓
200 OK responses
```

## Result

The Azure log stream confirmed that:

- the Container App is running
- the API receives incoming HTTP requests
- the `/health` endpoint returns `200 OK`
- the `/version` endpoint returns `200 OK`
- Uptime Kuma monitoring activity is visible in Azure logs

## Screenshot

A screenshot of the Azure log stream was saved in:

```text
screenshots/azure-log-stream.png
```

The screenshot shows:

- successful connection to the container log stream
- incoming `/health` requests
- incoming `/version` request
- successful `200 OK` responses

## Operational Value

This step is important because deployment alone is not enough in a real environment.

A deployed service should also be observable.

By reviewing Azure logs, it becomes possible to:

- confirm that the app is running
- verify that monitoring requests are reaching the service
- troubleshoot failed requests
- inspect runtime behavior
- connect application activity with infrastructure monitoring

## Final Result

Azure logs were successfully reviewed and documented.

Cloud Homelab v2 now includes:

- Azure deployment
- public API endpoint testing
- Uptime Kuma monitoring
- Azure log stream verification
- screenshot documentation

## Next Step

The next steps are:

- update the main `README.md` with Azure logs documentation
- create a final project summary
- optionally add GitHub Actions CD
- improve secrets handling
- continue updating the portfolio and learning log
