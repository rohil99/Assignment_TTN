from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from app.core.database import Base

class Doctor(Base):
    __tablename__ = "doctors"

    id: Mapped[int] = mapped_column(ForeignKey("users.id"), primary_key=True)
    name: Mapped[str]
    email: Mapped[str]
    specialization: Mapped[str]
