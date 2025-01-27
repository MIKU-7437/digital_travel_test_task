# app/infrastructure/database/db_connection.py
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker
from app.infrastructure.config import settings

# engine = create_engine(settings.db.url, echo=True)
# SessionLocal = sessionmaker(bind=engine)
engine = create_async_engine(settings.db.url, pool_pre_ping=True)
session = async_sessionmaker(bind=engine)
session_factory = async_sessionmaker(bind=engine)
