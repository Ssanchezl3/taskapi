import pytest
from fastapi.testclient import TestClient
from app.adapters.http.fastapi_app import app

client = TestClient(app)

def test_health():
    resp = client.get("/health")
    assert resp.status_code == 200
    assert resp.json() == {"status": "ok"}

def test_create_and_list_task():
    resp = client.post("/tasks", json={"title": "  Comprar leche  ", "status": "pending"})
    assert resp.status_code == 201
    data = resp.json()
    assert data["title"] == "Comprar leche"
    assert data["status"] in ("pending","done")
    tid = data["id"]

    list_resp = client.get("/tasks")
    assert list_resp.status_code == 200
    found = [t for t in list_resp.json() if t["id"] == tid]
    assert found

def test_invalid_status_returns_400():
    resp = client.post("/tasks", json={"title": "x", "status": "invalid"})
    assert resp.status_code == 400
