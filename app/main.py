from app.settings import settings
from fastapi import FastAPI


def create_app() -> FastAPI:

    app = FastAPI(title=settings.app_name)
    return app


app = create_app()
