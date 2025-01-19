from uuid import uuid4
from sqlalchemy import Column, String, Boolean, Enum
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base
from enum import Enum as PyEnum

Base = declarative_base()

class Role(PyEnum):
    """
    enum для роли пользователя
    """
    USER = "user"
    ADMIN = "admin"

class User(Base):
    """
    SQLAlchemy-модель для таблицы 'users'
    """
    __tablename__ = "users"

    user_id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    role = Column(Enum(Role), default=Role.USER, nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    is_deleted = Column(Boolean, default=False, nullable=False)

