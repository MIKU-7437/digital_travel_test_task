from fastapi import FastAPI
from app.presentation.api.controllers import order_controller
from app.presentation.api.controllers import product_controller

app = FastAPI(title="Order Service API")

app.include_router(order_controller.router)
app.include_router(product_controller.router)
