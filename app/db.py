"""Настройки подключения к базе данных и фабрика сессий SQLAlchemy."""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.settings import settings

engine = create_engine(settings.database_url)

SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


def get_db():
    """Предоставляет сессию БД для зависимостей FastAPI.

    Yields:
        Session: SQLAlchemy-сессия с автоматическим закрытием после запроса.
    """

    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
