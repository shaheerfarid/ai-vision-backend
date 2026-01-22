from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_analyze_image_empty():
    # send empty bytes
    response = client.post(
        "/analyze-image",
        files={"file": ("empty.jpg", b"")}
    )
    assert response.status_code == 200
    json_data = response.json()
    assert "error" in json_data or "filename" in json_data


def test_heatmap_json():
    data = {
        "zone_1": 0,
        "zone_2": 1
    }
    response = client.post("/heatmap/json", json=data)
    assert response.status_code == 200
    assert "heatmap" in response.json()
    assert response.json()["zones"] == len(data)
