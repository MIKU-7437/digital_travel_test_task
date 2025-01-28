from typing import Optional, List
from uuid import UUID
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from app.infrastructure.database.orm_models import OrderProduct


class OrderProductRepository:
    def __init__(self, session):
        self.session = session

    def create(self, order_id: int, product_id: int):
        order_product = OrderProduct(order_id=order_id, product_id=product_id)
        self.session.add(order_product)
