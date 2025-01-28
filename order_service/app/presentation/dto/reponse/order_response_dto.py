from uuid import UUID
from typing import List

from pydantic import BaseModel, Field

from app.presentation.dto.shared.product_dto import ProductDTO
from app.presentation.dto.shared.order_dto import OrderStatus

class OrderResponse(BaseModel):
    order_id: UUID = Field(default_factory=uuid4, example="d4f4a8fc-1122-4c3c-a56c-2b0274bee503")
    customer_name: str = Field(..., example="Иван Петров")
    status: OrderStatus = Field(OrderStatus.PENDING, example="pending")
    total_price: float = Field(..., example=1100.0)
    products: List[ProductDTO] = Field(..., example=[])
    is_deleted: bool = Field(False, example=False)

