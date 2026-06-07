from fastapi.testclient import TestClient

from server import app


client = TestClient(app)


def test_metrics_endpoint():
    response = client.get("/metrics")

    assert response.status_code == 200
    assert "# HELP" in response.text
    assert "python_info" in response.text or "process_" in response.text
    