from typing import List

from app.domain.models.order import Order
from app.domain.models.product import Product
from app.domain.repositories.order_repository import IOrderRepository

class CreateOrderUseCase:
    def __init__(self, order_repository: IOrderRepository):
        self.order_repository = order_repository

    def execute(self, customer_name: str, products_data: List[dict]) -> Order:
        # Преобразуем входные данные в список объектов Product
        products = [
            Product.create(
                name=prod["name"],
                price=prod["price"],
                quantity=prod["quantity"]
            )
            for prod in products_data
        ]
        order = Order.create(customer_name=customer_name, products=products)
        self.order_repository.add(order)
        return order
