from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class ProductIdRequest(BaseModel):
    product_id: UUID = Field(default_factory=uuid4)