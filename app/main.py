from fastapi import Depends, FastAPI
from app.config import settings
from app.security import verify_api_key

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


@app.get("/secure-info")
def secure_info(api_key_valid: bool = Depends(verify_api_key)):
    return {
        "message": "This endpoint is protected with an API key.",
        "environment": settings.APP_ENV,
        "security": "API key authentication enabled"
    }
