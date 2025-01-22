from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID

from app.domain.models.product import Product

class IProductRepository(ABC):
    @abstractmethod
    def add(self, product: Product) -> None:
        pass

    @abstractmethod
    def get_by_id(self, product_id: UUID) -> Optional[Product]:
        pass

    @abstractmethod
    def list_all(self) -> List[Product]:
        pass

    @abstractmethod
    def update(self, product: Product) -> None:
        pass

    @abstractmethod
    def delete(self, product_id: UUID) -> None:
        pass
