from fastapi import FastAPI
from app.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="A secure hybrid cloud API built with FastAPI, Docker, Azure and GitHub Actions.",
    version=settings.APP_VERSION
)


@app.get("/")
def root():
    return {
        "message": f"{settings.APP_NAME} is running",
        "project": "Secure Hybrid Cloud Deployment"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "environment": settings.APP_ENV
    }


@app.get("/version")
def version():
    return {
        "service": "cloud-homelab-v2-api",
        "version": settings.APP_VERSION,
        "environment": settings.APP_ENV
    }
