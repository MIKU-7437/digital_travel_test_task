from typing import Optional, List
from uuid import UUID
from sqlalchemy.future import select
from sqlalchemy.orm import Session
from sqlalchemy.ext.asyncio import AsyncSession

from app.domain.models.product import Product as DomainProduct
from app.domain.repositories.product_repository import IProductRepository
from app.infrastructure.database.orm_models import Order as OrderORM, Product as ProductORM, OrderProduct


class ProductRepositoryImpl(IProductRepository):
    def __init__(self, session: Session|AsyncSession):
        self.session = session

    async def add(self, product: DomainProduct) -> None:
        orm_product = ProductORM(
            product_id=product.product_id,
            name=product.name,
            price=product.price,
            quantity=product.quantity,
        )
        await self.session.add(orm_product)

    async def get_by_id(self, product_id: int) -> Optional[ProductORM]:
        orm_product = await self.session.query(ProductORM).filter_by(product_id=product_id).first()
        if orm_product is None:
            return None

        return DomainProduct(
            product_id=orm_product.product_id,
            name=orm_product.name,
            price=orm_product.price,
            quantity=orm_product.quantity,
        )

    async def list_all(self) -> List[DomainProduct]:
        result = await self.session.execute(select(ProductORM))
        orm_products = result.scalars().all()
        products: List[DomainProduct] = []

        for orm_product in orm_products:
            products.append(DomainProduct(
                product_id=orm_product.product_id,
                name=orm_product.name,
                price=orm_product.price,
                quantity=orm_product.quantity,
            ))
        return products

    async def update(self, product: DomainProduct) -> None:
        orm_product = await self.session.query(ProductORM).filter_by(product_id=product.product_id).first()
        if orm_product is None:
            return None

        orm_product.name = product.name
        orm_product.price = product.price
        orm_product.quantity = product.quantity

    async def delete(self, product_id: UUID) -> None:
        orm_product = await self.session.query(ProductORM).filter_by(product_id=product_id).first()
        if orm_product:
            await self.session.delete(orm_product)

    async def get_by_ids(self, product_ids: List[int]) -> List[DomainProduct]:
        result = await self.session.execute(
            select(ProductORM).where(ProductORM.product_id.in_(product_ids))
        )
        orm_products = result.scalars().all()

        return [
            DomainProduct(
                product_id=orm_product.product_id,
                name=orm_product.name,
                price=orm_product.price,
                quantity=orm_product.quantity,
            )
            for orm_product in orm_products
        ]