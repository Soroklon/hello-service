from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_hello():
    response = client.get("/hello")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from CI/CD!"}

def test_bonjour():
    response = client.get("/bonjour")
    assert response.status_code == 200
    assert response.json() == {"message": "Bonjour from CI/CD!"}

def test_root():
    response = client.get("/root")
    assert response.status_code == 200
    assert response.json() == {"message": "Root endpoint"}
