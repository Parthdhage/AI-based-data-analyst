import json
import pandas as pd
from analyst.core.config import settings
import uuid
from pathlib import Path
def label_check(label: str) -> bool:
    for path in settings.upload_dir.glob("*.json"):
        data = json.loads(path.read_text())
        if data["label"] == label:
            return True
    return False

def save_upload(file_bytes: bytes, label:str | None = None) -> str:
	if label and label_check(label):
		raise_ValueError("Name Already Exists")
	data_uid = str(uuid.uuid4())
	path = settings.upload_dir/ f"{data_uid}.csv"
	meta_path = settings.upload_dir / f"{data_uid}.json"
	path.write_bytes(file_bytes)
	if label:
		meta_path.write_text(json.dumps({"label": label}))
	return data_uid 


def load_dataset(data_uid: str) -> pd.DataFrame:
    path = settings.upload_dir/ f"{data_uid}.csv"

    if not path.exists():
        raise FileNotFoundError(f"dataset not found: {data_uid}")

    return pd.read_csv(path)

def find_label(label: str) -> str| None:
	for path in settings.upload_dir.glob("*.json"):
		data = json.loads(path.read_text())
		if data["label"] == label:
			return path.stem
	return None
def load_by_label(label: str) -> pd.DataFrame:
	dataset = find_label(label)
	if dataset is None:
		raise ValueError(f"No dataset found")
	return load_dataset(dataset)
