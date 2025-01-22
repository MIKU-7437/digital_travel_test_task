# app/presentation/main.py
from contextlib import asynccontextmanager

import uvicorn
from api.controllers import router as api_router
from app.infrastructure.config import settings
from app.infrastructure.database.db_helper import db_helper
from fastapi import FastAPI


@asynccontextmanager
async def lifespan():
    yield
    await db_helper.dispose()


main_app = FastAPI(
    lifespan=lifespan,
)
main_app.include_router(api_router, prefix=settings.api.prefix)

if __name__ == "__main__":
    uvicorn.run("main:app", host=settings.run.host, port=settings.run.port, reload=True)
