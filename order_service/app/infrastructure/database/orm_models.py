from enum import Enum as PyEnum
from uuid import uuid4

from sqlalchemy import (Boolean, Column, Enum, Float, ForeignKey, Integer,
                        String)
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class OrderStatus(PyEnum):
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    CANCELLED = "CANCELLED"


class Order(Base):
    """
    SQLAlchemy-модель для таблицы 'orders'
    (физическое представление доменной сущности Order).
    """
    __tablename__ = "orders"

    order_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    customer_name = Column(String, nullable=False)
    status = Column(Enum(OrderStatus), default=OrderStatus.PENDING, nullable=False)
    total_price = Column(Float, default=0, nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)

    order_products = relationship("OrderProduct", back_populates="order")


class Product(Base):
    """
    SQLAlchemy-модель для таблицы 'products'.
    """
    __tablename__ = "products"

    product_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    name = Column(String, nullable=False)
    price = Column(Float, default=0, nullable=False)
    quantity = Column(Integer, default=1, nullable=False)


class OrderProduct(Base):
    """
    Ассоциативная таблица (order_products) для связи "многие ко многим" между
    Order и Product, где можно хранить количество (quantity) в конкретном заказе.
    """
    __tablename__ = "order_products"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    order_id = Column(UUID(as_uuid=True), ForeignKey("orders.order_id"), nullable=False)
    product_id = Column(UUID(as_uuid=True), ForeignKey("products.product_id"), nullable=False)
    quantity = Column(Integer, default=1, nullable=False)

    # Связи:
    order = relationship("Order", back_populates="order_products")
    product = relationship("Product")
