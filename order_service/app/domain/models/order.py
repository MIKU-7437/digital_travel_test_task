from dataclasses import dataclass, field
from enum import Enum
from typing import List
from uuid import UUID, uuid4

from .product import Product


class OrderStatus(str, Enum):
    """
    Possible order statuses
    """
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"

@dataclass
class Order:
    """
    Domain model for order
    """
    order_id: UUID
    customer_name: str
    status: OrderStatus
    total_price: float
    products: List[Product] = field(default_factory=list)
    is_deleted: bool = False  # для мягкого удаления, если нужно

    @staticmethod
    def create(customer_name: str, products: List[Product]) -> "Order":
        """
        A method for creating a new order
        calculates total_price by lust of Products
        """
        total = sum(p.price * p.quantity for p in products)
        return Order(
            order_id=uuid4(),
            customer_name=customer_name,
            status=OrderStatus.PENDING,
            total_price=total,
            products=products
        )

    def update_status(self, new_status: OrderStatus):
        """
        Updating order status
        """
        self.status = new_status

    def soft_delete(self):
        """
        Soft deletion of order (marks flag is_deleted = True).
        """
        self.is_deleted = True
