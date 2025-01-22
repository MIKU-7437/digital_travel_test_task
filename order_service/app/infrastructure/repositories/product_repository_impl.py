from typing import Optional, List
from uuid import UUID
from sqlalchemy.orm import Session

from app.domain.models.product import Product as DomainProduct
from app.domain.repositories.product_repository import IProductRepository
from order_service.app.infrastructure.database.models import Order as OrderORM, Product as ProductORM, OrderProduct


class ProductRepositoryImpl(IProductRepository):
    def __init__(self, session: Session):
        self.session = session

    def add(self, product: DomainProduct) -> None:
        orm_product = ProductORM(
            product_id=product.product_id,
            name=product.name,
            price=product.price,
            quantity=product.quantity,
        )
        self.session.add(orm_product)

    def get_by_id(self, product_id: int) -> Optional[ProductORM]:
        orm_product = self.session.query(ProductORM).filter_by(product_id=product_id).first()
        if orm_product is None:
            return None

        return DomainProduct(
            product_id=orm_product.product_id,
            name=orm_product.name,
            price=orm_product.price,
            quantity=orm_product.quantity,
        )

    def list_all(self) -> List[DomainProduct]:
        orm_products = self.session.query(ProductORM).all()
        products: List[DomainProduct] = []

        for orm_product in orm_products:
            products.append(DomainProduct(
                product_id=orm_product.product_id,
                name=orm_product.name,
                price=orm_product.price,
                quantity=orm_product.quantity,
            ))
        return products

    def update(self, product: DomainProduct) -> None:
        orm_product = self.session.query(ProductORM).filter_by(product_id=product.product_id).first()
        if orm_product is None:
            return None

        orm_product.name = product.name
        orm_product.price = product.price
        orm_product.quantity = product.quantity

    def delete(self, product_id: UUID) -> None:
        orm_product = self.session.query(ProductORM).filter_by(product_id=product_id).first()
        if orm_product:
            self.session.delete(orm_product)