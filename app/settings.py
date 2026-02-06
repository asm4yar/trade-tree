"""Конфигурация приложения, загружаемая из переменных окружения."""

from pydantic_settings import BaseSettings, SettingsConfigDict
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


class Sessings(BaseSettings):
    """Настройки сервиса: БД, метаданные приложения и префикс API."""

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
    )
    database_url: str = ""
    app_name: str = "My API"
    version: str = ""
    api_prefix: str = ""


settings = Sessings()
