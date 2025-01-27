from typing import List
from uuid import UUID

from pydantic import BaseModel, Field, PositiveInt, PositiveFloat

class ProductCreateDTO(BaseModel):
    name: str = Field(..., example="Смартфон")
    price: PositiveFloat = Field(..., example=500.0, gt=0, description="Цена продукта должна быть положительной")
    quantity: PositiveInt = Field(..., example=10, gt=0, description="Количество продукта должно быть положительным целым числом")


class ProductDTO(BaseModel):
    product_id: UUID
    name: str = Field(..., example="Смартфон")
    price: PositiveFloat = Field(..., example=500.0, gt=0, description="Цена продукта должна быть положительной")
    quantity: PositiveInt = Field(..., example=10, gt=0, description="Количество продукта должно быть положительным целым числом")

