#TODO make uow


# class SqlAlchemyUnitOfWork(IUnitOfWork):
#     def __init__(self):
#         self.session: Session = SessionLocal()
#         self.order_repository = OrderRepositoryImpl(self.session)
#         self.product_repository = ProductRepositoryImpl(self.session)
#         # self.user_repository = UserRepositoryImpl(self.session)
#
#     def commit(self) -> None:
#         self.session.commit()
#
#     def rollback(self) -> None:
#         self.session.rollback()
#
#     def __enter__(self) -> "SqlAlchemyUnitOfWork":
#         return self
#
#     def __exit__(self, exc_type, exc_val, exc_tb) -> None:
#         if exc_type:
#             self.rollback()
#         else:
#             self.commit()
#         self.session.close()