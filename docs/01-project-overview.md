# 01 - Project Overview

## Overview

Cloud Homelab v2 is a secure hybrid cloud deployment project where a small FastAPI application is built, tested, containerized and prepared for deployment to Azure.

The project builds on Secure Homelab v1, where a local Ubuntu Server-based homelab was created with SSH, firewall protection, fail2ban, Docker, Portainer, Uptime Kuma, Homepage and Nginx.

## Purpose

The purpose of this project is to move from a local-only homelab environment into a hybrid cloud setup.

The project demonstrates practical skills in:

- Python FastAPI
- Environment-based configuration
- API key protection
- Docker and Docker Compose
- Automated testing with pytest
- GitHub Actions CI
- Technical documentation

## Current Architecture

```text
Developer PC
│
├── FastAPI application
├── .env configuration
├── Docker container
├── pytest tests
│
└── GitHub repository
    └── GitHub Actions CI
