from fastapi import FastAPI

app = FastAPI(
    title="Cloud Homelab v2 API",
    description="A secure hybrid cloud API built with FastAPI, Docker, Azure and GitHub Actions.",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Cloud Homelab v2 API is running",
        "project": "Secure Hybrid Cloud Deployment"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }


@app.get("/version")
def version():
    return {
        "service": "cloud-homelab-v2-api",
        "version": "1.0.0",
        "environment": "local"
    }
