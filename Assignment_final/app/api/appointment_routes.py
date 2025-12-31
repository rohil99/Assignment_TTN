from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.appointment import AppointmentCreate, AppointmentRead
from app.services.appointment_service import AppointmentService
from app.core.dependencies import get_db, get_current_user
from typing import List

router = APIRouter()

# Patient books an appointment
@router.post("/", response_model=AppointmentRead)
async def book_appointment(
    appointment: AppointmentCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if current_user.role.lower() != "patient":
        raise HTTPException(status_code=403, detail="Only patients can book appointments")
    try:
        new_appointment = await AppointmentService.create_appointment(
            patient_id=current_user.id,
            doctor_id=appointment.doctor_id,
            appointment_time=appointment.appointment_time,
            db=db
        )
        return new_appointment
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


# # Optional: Check doctor availability (can be called by patients)
# @router.get("/doctor/{doctor_id}/availability", response_model=List[AppointmentRead])
# async def doctor_availability(
#     doctor_id: int,
#     db: AsyncSession = Depends(get_db),
#     current_user=Depends(get_current_user)
# ):
#     return await AppointmentService.get_doctor_availability(doctor_id, db)

@router.get("/doctor/upcoming", response_model=List[AppointmentRead])
async def upcoming_appointments(
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if current_user.role.lower() != "doctor":
        raise HTTPException(status_code=403, detail="Only doctors can view upcoming appointments")
    return await AppointmentService.get_doctor_upcoming_appointments(current_user.id, db)

@router.delete("/{appointment_id}")
async def cancel_my_appointment(
    appointment_id: int,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if current_user.role.lower() != "patient":
        raise HTTPException(
            status_code=403,
            detail="Only patients can cancel appointments"
        )

    return await AppointmentService.cancel_appointment(
        appointment_id=appointment_id,
        patient_id=current_user.id,
        db=db
    )