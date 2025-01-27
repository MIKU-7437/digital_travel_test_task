from typing import List

from app.domain.models.order import Order
from app.domain.models.product import Product
from app.domain.repositories.order_repository import IOrderRepository
from app.application.dto.product_dto import  ProductCreateDTO, ProductDTO
from app.application.dto.order_dto import OrderDTO

class CreateOrderUseCase:
    def __init__(self, order_repository: IOrderRepository):
        self.order_repository = order_repository

    def execute(self, customer_name: str, products_data: List[ProductDTO]) -> OrderDTO:
        # Преобразуем входные данные в список объектов Product
        products = [
            Product.create(
                product_id=prod.product_id,
                name=prod.name,
                price=prod.price,
                quantity=prod.quantity
            )
            for prod in products_data
        ]
        order = Order.create(customer_name=customer_name, products=products)
        self.order_repository.add(order)
        return order
