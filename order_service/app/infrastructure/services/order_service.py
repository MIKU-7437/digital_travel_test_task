from app.infrastructure.unit_of_work import SqlAlchemyUnitOfWork
from app.domain.models.order import Order
from app.domain.models.product import Product


class OrderService:
    def __init__(self, uow: SqlAlchemyUnitOfWork):
        self.uow = uow

    async def create_order_with_products(self, product_ids: list[int]) -> dict:
        try:
            async with self.uow:
                products = await self.uow.product_repository.get_by_ids(product_ids)


                order = Order(
                    customer_name='f',
                    products=products
                )

                order = await self.uow.order_repository.add(
                    order
                )

                for product in products:
                    await self.uow.order_product_repository.create(
                        order_id=order.order_id, product_id=product.product_id, quantity=1
                    )

                return {"order_id": order.id, "total_amount": order.total_amount}
        except Exception as e:
            await self.uow.rollback()
            raise e
