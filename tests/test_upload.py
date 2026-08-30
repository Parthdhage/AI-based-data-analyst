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
 
		
def test_profile_returns_summary():
	upload_response = client.post(
		"/upload",
		files = {"file": ("data.csv", b"a,b\n1, 2\n3, 4\n", "text/csv")}
	)
	data_uid = upload_response.json()["data_uid"]
	
	response = client.get(f"/datasets/{data_uid}/profile")
	assert response.status_code == 200
	assert response.json()["rows"] == 2

def test_profile_missing_dataset_returns_404():
	response = client.get(f"/datasets/data-not-exist/profile")
	assert response.status_code == 404
