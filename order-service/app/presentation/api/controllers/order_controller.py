from fastapi import APIRouter, Depends, HTTPException
from app.presentation.api.dto.order_dto import OrderCreateDTO, OrderDTO
from app.application.use_cases.create_order_use_case import CreateOrderUseCase
from app.infrastructure.unit_of_work import SqlAlchemyUnitOfWork

router = APIRouter(prefix="/orders", tags=["Orders"])

def get_uow():
    with SqlAlchemyUnitOfWork() as uow:
        yield uow

@router.post("/", response_model=OrderDTO)
def create_order(dto: OrderCreateDTO, uow: SqlAlchemyUnitOfWork = Depends(get_uow)):
    use_case = CreateOrderUseCase(order_repository=uow.order_repository)
    order = use_case.execute(customer_name=dto.customer_name, products_data=dto.products)
    return OrderDTO(
        order_id=order.order_id,
        customer_name=order.customer_name,
        status=order.status.value,
        total_price=order.total_price,
        is_deleted=order.is_deleted
    )
