"""Pydantic-схемы для API каталога и заказов."""

from pydantic import BaseModel, Field


class AddItemRequest(BaseModel):
    """Запрос на добавление товара в заказ."""

    product_id: int
    quantity: int = Field(gt=0)


class AddItemResponse(BaseModel):
    """Ответ после успешного добавления товара в заказ."""

    order_id: int
    product_id: int
    new_qty: int
    remaining_stock: int


class CategoryChildrenCountOut(BaseModel):
    """Агрегированные данные по дочерним категориям."""

    id: int
    name: str
    children_count: int


class ClientStatistics(BaseModel):
    """Статистика клиента по общей сумме заказов."""

    name: str
    total_amount: int


class TopProductOut(BaseModel):
    """Элемент ответа с данными о популярном товаре за последний месяц."""

    product_name: str
    category_level1: str
    total_sold_qty: int
