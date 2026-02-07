"""Эндпоинт для получения самых продаваемых товаров за 30 дней."""

import logging
from fastapi import APIRouter, Depends
from app.db import get_db
from sqlalchemy.orm import Session
from app.api.catalog.schemas import TopProductOut
from app.repositories.catalog import get_top5_products_last_30_days

logger = logging.getLogger(__name__)

router = APIRouter(prefix="/catalog", tags=["Catalog"])


@router.get("/top-products", response_model=list[TopProductOut])
async def get_top_products(db: Session = Depends(get_db)):
    """Возвращает топ-5 товаров по количеству продаж за последний месяц."""

    return get_top5_products_last_30_days(db)
