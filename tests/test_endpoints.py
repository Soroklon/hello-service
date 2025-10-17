import pytest
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

@pytest.mark.parametrize("name, answer", [
    ("Name", "Hello, Name!"),
    ("abc", "Hello, abc!")
])
def test_hello_by_name(name, answer):
    response = client.get(f"/hello/{name}")
    assert response.status_code == 200
    assert response.json() == {"message": answer}

def test_about():
    response = client.get("/about")
    assert response.status_code == 200
    assert response.json() == {"message": "This is FastAPI application with CI/CD workflow useing local Docker image"}
