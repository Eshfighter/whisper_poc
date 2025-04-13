import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Test the /health endpoint
def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "Service is running"}

# Test the /transcriptions endpoint
def test_get_transcriptions():
    response = client.get("/transcriptions")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test the /search endpoint
def test_search_transcriptions():
    response = client.get("/search?filename=test")
    assert response.status_code == 200
    assert isinstance(response.json(), list) 