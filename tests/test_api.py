from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"


def test_get_train():
    response = client.get("/trains/ICE101")

    assert response.status_code == 200
    assert response.json()["train_id"] == "ICE101"


def test_train_not_found():
    response = client.get("/trains/ICE999")

    assert response.status_code == 404
