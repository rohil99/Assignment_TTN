from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from datetime import datetime
from app.models.availability import Availability
from app.models.appointment import Appointment

class AvailabilityService:

    @staticmethod
    async def set_availability(doctor_id: int, start_time: datetime, end_time: datetime, db: AsyncSession):
        # Add new availability slot
        new_slot = Availability(
            doctor_id=doctor_id,
            start_time=start_time,
            end_time=end_time
        )
        db.add(new_slot)
        await db.commit()
        await db.refresh(new_slot)
        return new_slot

    @staticmethod
    async def get_doctor_availability(doctor_id: int, db: AsyncSession):
        # Fetch all availability slots
        result = await db.execute(
            select(Availability).where(Availability.doctor_id == doctor_id)
        )
        avail_slots = result.scalars().all()

        # Fetch all future appointments
        app_result = await db.execute(
            select(Appointment).where(
                Appointment.doctor_id == doctor_id,
                Appointment.appointment_time >= datetime.utcnow()
            )
        )
        booked_slots = app_result.scalars().all()

        # Combine slots and booked appointments
        response = []
        for slot in avail_slots:
            booked_times = [a.appointment_time for a in booked_slots
                            if slot.start_time <= a.appointment_time < slot.end_time]
            response.append({
                "start_time": slot.start_time,
                "end_time": slot.end_time,
                "booked_times": booked_times
            })
        return response
    
    @staticmethod
    async def set_availability(
        doctor_id: int,
        start_time,
        end_time,
        db: AsyncSession
    ):
        slot = Availability(
            doctor_id=doctor_id,
            start_time=start_time,
            end_time=end_time
        )
        db.add(slot)
        await db.commit()
        await db.refresh(slot)
        return slot


