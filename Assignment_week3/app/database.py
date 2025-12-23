from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# MySQL connection URL
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "mysql+pymysql://root:your_root_password@localhost:3306/fastapi_db"
)

# SQLAlchemy engine
engine = create_engine(DATABASE_URL, echo=True)

# Base class for models
Base = declarative_base()

# Session class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get DB session in routes
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
