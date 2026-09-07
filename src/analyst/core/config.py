from pathlib import Path
from typing import Literal

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )
	
    upload_dir: Path = Path("uploads")
    max_upload_mb: int = 50
    environment: Literal["development", "production"] = "development"
    log_level: str = "INFO"
    groq_api_key: str
    groq_model: str = "llama-3.3-70b-versatile"

    @property
    def max_upload_bytes(self) -> int:
        return self.max_upload_mb * 1024 * 1024


settings = Settings()