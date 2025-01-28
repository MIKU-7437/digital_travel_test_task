from uuid import UUID

from pydantic import BaseModel


class OrderProductDto(BaseModel):
    product_id: UUID

    @staticmethod
    async def create(product_id: UUID) -> 'OrderProductDto':
        return OrderProductDto(product_id=product_id)