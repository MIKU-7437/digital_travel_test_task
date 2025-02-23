from app.infrastructure.config import settings

from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.asyncio import async_sessionmaker

class DatabaseHelper:
    def __init__(
            self,
            url: str,
            echo: bool = False,
            pool_size: int = 5,
            max_overflow: int = 10,
            echo_pool: bool = False,

    )->None:
        self.engine = create_async_engine(
            url=url,
            echo=echo,
            echo_pool=echo_pool,
            pool_size=pool_size,
            max_overflow=max_overflow,

        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False,
        )
    async def dispose(self):
        await self.engine.dispose()

    async def session_getter(self)->AsyncGenerator[AsyncSession, None]:
        async with self.session_factory() as session:
            yield session

db_helper = DatabaseHelper(
    url= settings.db.url,
    echo = settings.db.echo,
    echo_pool = settings.db.echo_pool,
    pool_size = settings.db.pool_size,
    max_overflow = settings.db.max_overflow,
)
# db_helper = DatabaseHelper(
#     url= settings.url,
#     echo = settings.echo,
#     echo_pool = settings.echo_pool,
#     pool_size = settings.pool_size,
#     max_overflow = settings.max_overflow,
# )