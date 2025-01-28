from fastapi import APIRouter, Depends, Body

from app.presentation.dto.requests.order_request_dto import  OrderCreateRequest
from app.presentation.dto.shared.product_dto import ProductDTO
from app.presentation.dto.shared.order_dto import OrderDTO
from app.application.use_cases.create_order_use_case import CreateOrderUseCase
from app.infrastructure.unit_of_work import SqlAlchemyUnitOfWork
from app.infrastructure.database.db_connection import session_factory
from app.infrastructure.config import settings

print(settings.db.url)
router = APIRouter(prefix="/orders", tags=["Orders"])

async def get_uow():
    async with SqlAlchemyUnitOfWork(session_factory) as uow:
        yield uow

@router.post("/", response_model=OrderDTO)
def create_order(dto: OrderCreateRequest = Body(..., media_type="application/json"), uow: SqlAlchemyUnitOfWork = Depends(get_uow)):
    use_case = CreateOrderUseCase(order_repository=uow.order_repository)
    order = use_case.execute(customer_name=dto.customer_name, products_data=dto.products)
    return OrderDTO(
        order_id=order.order_id,
        customer_name=order.customer_name,
        status=order.status.value,
        total_price=order.total_price,
        is_deleted=order.is_deleted,
        products=[
            ProductDTO(
                product_id=prod.product_id,
                name=prod.name,
                price=prod.price,
                quantity=prod.quantity
            )
            for prod in order.products
        ]
    )
