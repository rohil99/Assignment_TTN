from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime
from app.models.appointment import Appointment
from fastapi import HTTPException

class AppointmentService:

    @staticmethod
    async def create_appointment(
        patient_id: int,
        doctor_id: int,
        appointment_time: datetime,
        db: AsyncSession
    ):
        # Prevent double-booking for same doctor & same time
        existing = await db.execute(
            select(Appointment).where(
                Appointment.doctor_id == doctor_id,
                Appointment.appointment_time == appointment_time
            )
        )

        if existing.scalars().first():
            raise Exception("This appointment slot is already booked")

        appointment = Appointment(
            doctor_id=doctor_id,
            patient_id=patient_id,
            appointment_time=appointment_time
        )

        db.add(appointment)
        await db.commit()
        await db.refresh(appointment)
        return appointment

    @staticmethod
    async def get_doctor_upcoming_appointments(doctor_id: int, db: AsyncSession):
        result = await db.execute(
            select(Appointment).where(
                Appointment.doctor_id == doctor_id,
                Appointment.appointment_time >= datetime.utcnow()
            ).order_by(Appointment.appointment_time)
        )
        return result.scalars().all()

    @staticmethod
    async def get_doctor_availability(doctor_id: int, db: AsyncSession):
        """
        Returns all future appointments for a doctor
        """
        result = await db.execute(
            select(Appointment).where(
                Appointment.doctor_id == doctor_id,
                Appointment.appointment_time >= datetime.utcnow()
            ).order_by(Appointment.appointment_time)
        )
        return result.scalars().all()
    
    @staticmethod
    async def cancel_appointment(
    appointment_id: int,
    patient_id: int,
    db: AsyncSession
):
        result = await db.execute(
        select(Appointment).where(
            Appointment.id == appointment_id,
            Appointment.patient_id == patient_id
        )
    )

        appointment = result.scalars().first()

        if not appointment:
            raise HTTPException(
            status_code=404,
            detail="Appointment not found or not owned by you"
        )

        if appointment.appointment_time < datetime.utcnow():
            raise HTTPException(
            status_code=400,
            detail="Past appointments cannot be cancelled"
        )

        await db.delete(appointment)
        await db.commit()

        return {"message": "Appointment cancelled successfully"}
