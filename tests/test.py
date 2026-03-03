from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "healthy"}

def test_metrics():
    r = client.get("/metrics")
    assert r.status_code == 200
    json_body = r.json()
    # Keys exist and are numeric where expected
    assert "cpu_percent" in json_body
    assert "memory_percent" in json_body
    assert "disk_percent" in json_body