import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_root():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        res = await ac.get("/hello")
    assert res.status_code == 200
    assert res.json() == {"message": "Hello from CI/CD!"}

@pytest.mark.asyncio
async def test_hellotest():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as ac:
        res = await ac.get("/bonjour")
    assert res.status_code == 200
    assert res.json() == {"message": "Bonjour from CI/CD!"}
