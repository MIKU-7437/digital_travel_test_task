from fastapi import FastAPI
from app.presentation.api.controllers import order_controller

app = FastAPI(title="Order Service API")

app.include_router(order_controller.router)
