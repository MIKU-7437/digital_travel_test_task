from abc import ABC, abstractmethod
from typing import Optional, List
from uuid import UUID

from app.domain.models.order import Order

class IOrderRepository(ABC):
    @abstractmethod
    def add(self, order: Order) -> None:
        pass

    @abstractmethod
    def get_by_id(self, order_id: UUID) -> Optional[Order]:
        pass

    @abstractmethod
    def list_all(self) -> List[Order]:
        pass

    @abstractmethod
    def update(self, order: Order) -> None:
        pass

    @abstractmethod
    def delete(self, order_id: UUID) -> None:
        pass
