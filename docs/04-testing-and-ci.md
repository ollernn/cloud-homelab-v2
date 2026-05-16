# 04 - Testing and CI

## Overview

The project uses `pytest` for automated testing and GitHub Actions for continuous integration.

Testing is used to verify that the FastAPI application works correctly before future deployment to Azure.

GitHub Actions is used to automatically run the tests when changes are pushed to GitHub.

## Purpose

The purpose of testing and CI in this project is to make sure that important parts of the API still work after changes are made.

This step demonstrates practical skills in:

- writing automated API tests
- using pytest
- testing FastAPI endpoints
- testing protected endpoints
- configuring GitHub Actions
- running CI automatically on push and pull requests
- separating local secrets from CI test values

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

## Testing the Protected Endpoint

The protected `/secure-info` endpoint requires an API key through the `x-api-key` header.

In local testing, the test value must match the `API_KEY` value provided through the test environment.

The real local `.env` file is not committed to GitHub.

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

Example CI environment variables:

```yaml
env:
  APP_NAME: Cloud Homelab v2 API
  APP_VERSION: 1.0.0
  APP_ENV: test
  API_KEY: <test-api-key>
```

The `API_KEY` value used in CI is a test value for automated testing.

The real local `.env` file is not committed to GitHub.

## Security Note

This project avoids committing real secrets to GitHub.

The `.env` file is ignored by Git, and `.env.example` is used to show which variables are required.

In documentation, API keys should be written as placeholders, for example:

```text
API_KEY=change-me
```

or:

```text
x-api-key: <your-api-key>
```

## CI Result

The GitHub Actions CI workflow was successfully completed.

This means that automated tests run correctly in GitHub after code is pushed.

## Result

Testing and CI were successfully added to the project.

The project now has:

- automated endpoint tests
- tests for public endpoints
- tests for a protected endpoint
- pytest configuration
- a GitHub Actions CI workflow
- automatic test execution on push and pull request

## Next Step

After testing and CI, the next major step was to deploy the containerized FastAPI application to Azure.
