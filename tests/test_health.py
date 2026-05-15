from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check_returns_healthy_status():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "healthy"
    assert "environment" in response.json()

def test_version_returns_service_information():
    response = client.get("/version")

    assert response.status_code == 200
    assert response.json()["service"] == "cloud-homelab-v2-api"
    assert "version" in response.json()
    assert "environment" in response.json()

def test_secure_info_without_api_key_returns_unauthorized():
    response = client.get("/secure-info")

    assert response.status_code == 401
    assert response.json()["detail"] == "Invalid or missing API key"


def test_secure_info_with_api_key_returns_success():
    response = client.get(
        "/secure-info",
        headers={"x-api-key": "dev-secret-key"}
    )

    assert response.status_code == 200
    assert response.json()["security"] == "API key authentication enabled"
