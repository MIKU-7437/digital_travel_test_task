from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ProductResponseDto(BaseModel):
    name: str = Field(..., example="Смартфон")
    price: float = Field(..., ge=0, example=999.99)
    quantity: int = Field(..., ge=1, example=10)
    product_id: UUID = Field(default_factory=uuid4, example="f47ac10b-58cc-4372-a567-0e02b2c3d479")