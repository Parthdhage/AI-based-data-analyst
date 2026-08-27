from fastapi.testclient import TestClient
from analyst.api.main import app

client = TestClient(app)
def test_health_status():
	response = client.get("/health")
	assert response.status_code == 200
	assert response.json()["status"] == "ok"