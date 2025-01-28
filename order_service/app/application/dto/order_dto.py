from enum import Enum
from typing import List
from uuid import UUID

from pydantic import BaseModel, Field

from app.application.dto.product_dto import ProductCreateDTO, ProductDTO

class OrderStatus(str, Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"



class OrderDTO(BaseModel):
    order_id: UUID = Field(..., example="d4f4a8fc-1122-4c3c-a56c-2b0274bee503")
    customer_name: str = Field(..., example="Иван Петров")
    status: OrderStatus = Field(OrderStatus.PENDING, example="pending")
    total_price: float = Field(..., example=1100.0)
    products: List[ProductDTO] = Field(..., example=[])
    is_deleted: bool = Field(False, example=False)


class OrderCreateDTO(BaseModel):
    customer_name: str = Field(..., example="Иван Петров")
    products: List[UUID]
