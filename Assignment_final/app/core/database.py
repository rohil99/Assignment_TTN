# app/core/database.py
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings
import os

# Make sure you have a database_url in your settings
DATABASE_URL = settings.database_url  # e.g., "postgresql+asyncpg://user:pass@localhost/dbname"
# DATABASE_URL = os.getenv("DATABASE_URL")

# Async engine
engine = create_async_engine(DATABASE_URL, echo=True)

# Session factory
AsyncSessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# Base class for models
Base = declarative_base()

# Optional helper to get a session (already used in dependencies.py)
async def get_db():
    async with AsyncSessionLocal() as session:
        yield session
