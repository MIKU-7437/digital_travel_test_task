from uuid import UUID, uuid4
from typing import List

from pydantic import BaseModel, Field

from app.presentation.dto.requests.product_request_dto import ProductIdRequest


class OrderCreateRequest(BaseModel):
    customer_name: str
    products: List[ProductIdRequest]