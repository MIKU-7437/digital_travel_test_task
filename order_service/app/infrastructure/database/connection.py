# app/infrastructure/database/db_connection.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.infrastructure.config import settings

engine = create_engine(settings.db.url, echo=True)
SessionLocal = sessionmaker(bind=engine)
