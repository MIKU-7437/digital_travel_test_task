from typing import List

from fastapi import APIRouter, Depends, Body
from sqlalchemy.ext.asyncio import AsyncSession


from app.application import *
from app.infrastructure.database.db_connection import session_factory
from app.infrastructure.database.orm_models import Product
from app.infrastructure.unit_of_work import SqlAlchemyUnitOfWork
from app.infrastructure.repositories.product_repository_impl import ProductRepositoryImpl
from app.presentation.dto.reponse.product_response_dto import ProductResponseDto
router = APIRouter(prefix="/products", tags=["Products"])

async def get_session():
    yield session_factory()


@router.get("/", response_model=List[ProductResponseDto])
async def list_products(session: AsyncSession = Depends(get_session)):
    product_repository = ProductRepositoryImpl(session=session)
    products = await product_repository.list_all()
    return [
        ProductResponseDto(
            product_id=prod.product_id,
            name=prod.name,
            price=prod.price,
            quantity=prod.quantity,
        ) for prod in products
    ]
