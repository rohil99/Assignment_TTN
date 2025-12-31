from app.models.doctor import Doctor
from app.models.appointment import Appointment
from app.core.database import AsyncSessionLocal as async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime
from typing import List
from app.models.user import User
from sqlalchemy.future import select
from app.models.availability import Availability

class DoctorService:
    @staticmethod
    async def create_doctor(user: User, specialization: str, db: AsyncSession):
        doctor = Doctor(
            id=user.id,  # same ID as user
            name=user.name,
            email=user.email,
            specialization=specialization
        )
        db.add(doctor)
        await db.commit()
        await db.refresh(doctor)
        return doctor

    @staticmethod
    async def list_all_doctors(db: AsyncSession):
        result = await db.execute(select(User).filter_by(role="Doctor"))
        return result.scalars().all()

    # Add ONLY the availability logic
    @staticmethod
    async def get_availability(doctor_id: int, db: AsyncSession):
        result = await db.execute(
            select(Availability)
            .where(Availability.doctor_id == doctor_id)
            .order_by(Availability.start_time)
        )
        return result.scalars().all()
