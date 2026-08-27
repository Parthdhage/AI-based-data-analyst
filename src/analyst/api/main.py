from contextlib import asynccontextmanager

from fastapi import FastAPI

from analyst.core.config import settings


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings.upload_dir.mkdir(parents=True, exist_ok=True)
    yield


app = FastAPI(lifespan=lifespan)


@app.get("/health")
def health():
    return {"status": "ok", "environment": settings.environment}