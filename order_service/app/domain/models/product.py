from dataclasses import dataclass
from uuid import UUID, uuid4


@dataclass
class Product:
    """
    Domain model for product
    """
    product_id: UUID
    name: str
    price: float
    quantity: int

    @staticmethod
    def create(product_id: UUID, name: str, price: float, quantity: int) -> "Product":
        """
        A fabric method for creating a new product
        with product_id generation.
        """
        return Product(
            product_id=product_id,
            name=name,
            price=price,
            quantity=quantity
        )
