from fastapi import APIRouter, UploadFile, File, HTTPException
from analyst.data.storage import save_upload, load_dataset
from analyst.analysis.profiler import profile_dataset
from analyst.core.config import settings

router = APIRouter()


@router.post("/upload")
async def upload(file: UploadFile = File(...), label: str | None = None):
	if not file.filename.endswith(".csv"):
		raise HTTPException(status_code = 400, detail = "Only csv files are accepted")
	content = await file.read()
	if len(content) > settings.max_upload_bytes:
		raise HTTPException(status_code = 413, detail = "File too large")
	try:
		data_uid = save_upload(content, label)
	except ValueError as e:
		raise HTTPException(status_code = 409, detail=str(e))

	return {"data_uid": data_uid}

@router.get("/datasets/{data_uid}/profile")
async def get_profile(data_uid:str):
	try:
		dataset = load_dataset(data_uid)
	except FileNotFoundError as e:
		raise HTTPException(status_code = 404, detail = str(e))
	profile = profile_dataset(dataset)
	return profile