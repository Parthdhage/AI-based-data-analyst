from fastapi.testclient import TestClient

from analyst.api.main import app

client = TestClient(app)

def test_upload_csv():
	response = client.post(
		"/upload",
		files = {"file": ("data.csv", b"a,b\n 1, 2\n", "text/csv")}
		)
	assert response.status_code == 200
	assert "data_uid" in response.json()

def test_not_csv():
	response = client.post(
		"/upload",
		files = {"file": ("data.txt", b"hello", "text/plain")}
		)
	assert response.status_code == 400
 
		