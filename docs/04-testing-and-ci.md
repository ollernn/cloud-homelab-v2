# 04 - Testing and CI

## Overview

The project uses `pytest` for automated testing and GitHub Actions for continuous integration.

Testing is used to verify that the FastAPI application works correctly before future deployment to Azure.

## Purpose

The purpose of testing and CI in this project is to make sure that important parts of the API still work after changes are made.

GitHub Actions automatically runs the tests when code is pushed to the `main` branch or when a pull request is created.

## Testing Tool

The project uses:

```text
pytest
```

The test files are stored in:

```text
tests/
```

The current test file is:

```text
tests/test_health.py
```

## Pytest Configuration

The project includes a `pytest.ini` file.

This file tells pytest to use the project root as the Python path and to look for tests inside the `tests` folder.

```ini
[pytest]
pythonpath = .
testpaths = tests
```

## Local Testing

Run the tests locally with:

```powershell
pytest
```

Expected result:

```text
4 passed
```

## Current Tests

The current tests verify that:

- `/health` returns status code 200
- `/health` returns a healthy status
- `/version` returns service information
- `/secure-info` blocks requests without an API key
- `/secure-info` allows requests with a valid API key

## GitHub Actions CI

GitHub Actions is used for continuous integration.

The workflow file is located at:

```text
.github/workflows/ci.yml
```

## When CI Runs

The CI workflow runs automatically on:

- push to `main`
- pull requests to `main`

## CI Workflow Steps

The workflow performs the following steps:

```text
Checkout repository
Set up Python
Install dependencies
Run pytest
```

## CI Environment Variables

The GitHub Actions workflow defines test environment variables so the tests can run without using a local `.env` file.

```yaml
env:
  APP_NAME: Cloud Homelab v2 API
  APP_VERSION: 1.0.0
  APP_ENV: test
  API_KEY: dev-secret-key
```

The real local `.env` file is not committed to GitHub.

## Result

The first GitHub Actions CI workflow was successfully completed.

This means that the project now has automated testing and a working CI pipeline.

## Next Step

The next major step is to deploy the containerized FastAPI application to Azure.
