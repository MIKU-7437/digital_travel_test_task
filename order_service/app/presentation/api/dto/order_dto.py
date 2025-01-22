from enum import Enum
from typing import List
from uuid import UUID, uuid4

from pydantic import BaseModel, Field

from .product_dto import ProductCreateDTO, ProductDTO


class OrderStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"


class OrderCreateDTO(BaseModel):
    customer_name: str = Field(..., example="Иван Петров")
    products: List[ProductCreateDTO] = Field(
        ...,
        example=[
            {"name": "Смартфон", "price": 500.0, "quantity": 2},
            {"name": "Наушники", "price": 50.0, "quantity": 1}
        ]
    )


class OrderDTO(BaseModel):
    order_id: UUID = Field(default_factory=uuid4, example="d4f4a8fc-1122-4c3c-a56c-2b0274bee503")
    customer_name: str = Field(..., example="Иван Петров")
    status: OrderStatus = Field(OrderStatus.PENDING, example="pending")
    total_price: float = Field(..., example=1100.0)
    products: List[ProductDTO] = Field(..., example=[])
    is_deleted: bool = Field(False, example=False)

