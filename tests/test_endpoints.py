import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

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
