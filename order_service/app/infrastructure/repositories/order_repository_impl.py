from typing import Optional, List
from uuid import UUID
from sqlalchemy.orm import Session

from app.domain.models.order import Order as DomainOrder, OrderStatus as DomainOrderStatus
from app.domain.repositories.order_repository import IOrderRepository
from app.infrastructure.database.orm_models import Order as OrderORM, OrderProduct, Product as ProductORM

class OrderRepositoryImpl(IOrderRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, orm_order: OrderORM) -> None:
        self.session.add(orm_order)

    def get_by_id(self, order_id: UUID) -> Optional[DomainOrder]:
        orm_order = self.session.query(OrderORM).filter_by(order_id=order_id, is_deleted=False).first()
        if orm_order is None:
            return None
        # Маппинг ORM заказа в доменную модель (упрощённо)
        from app.domain.models.order import Order  # предполагаем, что это доменная модель
        # Здесь мы просто создаем доменный заказ без наполнения списка продуктов (расширьте при необходимости)
        return Order(
            order_id=orm_order.order_id,
            customer_name=orm_order.customer_name,
            status=DomainOrderStatus(orm_order.status),
            total_price=orm_order.total_price,
            products=[],  # Можно реализовать маппинг продуктов через orm_order.order_products
            is_deleted=orm_order.is_deleted
        )

    def list_all(self) -> List[DomainOrder]:
        orm_orders = self.session.query(OrderORM).filter_by(is_deleted=False).all()
        orders: List[DomainOrder] = []
        for orm_order in orm_orders:
            # Какой-то маппинг, упрощённо:
            from app.domain.models.order import Order, OrderStatus
            orders.append(Order(
                order_id=orm_order.order_id,
                customer_name=orm_order.customer_name,
                status=OrderStatus(orm_order.status),
                total_price=orm_order.total_price,
                products=[],  # Реализуйте маппинг продуктов при необходимости
                is_deleted=orm_order.is_deleted
            ))
        return orders

    def update(self, order: DomainOrder) -> None:
        orm_order: Optional[OrderORM] = self.session.query(OrderORM).filter_by(order_id=order.order_id).first()
        if orm_order is None:
            return
        orm_order.customer_name = order.customer_name
        orm_order.status = order.status.value
        orm_order.total_price = order.total_price
        orm_order.is_deleted = order.is_deleted
        # Если нужно обновление продуктов, реализуйте соответствующую логику

    def delete(self, order_id: UUID) -> None:
        orm_order: Optional[OrderORM] = self.session.query(OrderORM).filter_by(order_id=order_id).first()
        if orm_order:
            # Реализуем мягкое удаление
            orm_order.is_deleted = True
