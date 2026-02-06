"""Точка входа FastAPI-приложения."""

from app.settings import settings
from app.api.router import api_router
from fastapi import FastAPI


def create_app() -> FastAPI:
    """Создаёт и настраивает экземпляр FastAPI.

    Returns:
        FastAPI: Инициализированное приложение с подключёнными роутерами.
    """

    app = FastAPI(title=settings.app_name, version=settings.version)
    app.include_router(api_router, prefix=settings.api_prefix)
    return app


app = create_app()
