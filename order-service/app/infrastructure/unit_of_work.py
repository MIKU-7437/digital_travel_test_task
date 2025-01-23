from sqlalchemy.orm import Session

from app.application.unit_of_work import IUnitOfWork
from app.infrastructure.database.db_connection import SessionLocal
from app.infrastructure.repositories.order_repository_impl import OrderRepositoryImpl
from app.infrastructure.repositories.product_repository_impl import ProductRepositoryImpl

class SqlAlchemyUnitOfWork(IUnitOfWork):
    def __init__(self):
        self.session: Session = SessionLocal()
        self.order_repository = OrderRepositoryImpl(self.session)
        self.product_repository = ProductRepositoryImpl(self.session)

    def commit(self) -> None:
        self.session.commit()

    def rollback(self) -> None:
        self.session.rollback()

    def __enter__(self) -> "SqlAlchemyUnitOfWork":
        return self

    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        if exc_type:
            self.rollback()
        else:
            self.commit()
        self.session.close()