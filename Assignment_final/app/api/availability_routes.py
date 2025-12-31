from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.schemas.availability import AvailabilityCreate, AvailabilityRead
from app.services.availability_service import AvailabilityService
from app.core.dependencies import get_db, get_current_user

router = APIRouter(prefix="/availability", tags=["Availability"])

@router.post("/", response_model=AvailabilityRead)
async def create_availability(slot: AvailabilityCreate, db: AsyncSession = Depends(get_db), current_user=Depends(get_current_user)):
    if current_user.role.lower() != "doctor":
        raise HTTPException(status_code=403, detail="Only doctors can set availability")
    return await AvailabilityService.set_availability(current_user.id, slot.start_time, slot.end_time, db)

@router.get("/{doctor_id}", response_model=List[AvailabilityRead])
async def doctor_availability(doctor_id: int, db: AsyncSession = Depends(get_db)):
    return await AvailabilityService.get_doctor_availability(doctor_id, db)


@router.post("/doctor/availability", response_model=AvailabilityRead)
async def set_availability(
    availability: AvailabilityCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if current_user.role.lower() != "doctor":
        raise HTTPException(status_code=403, detail="Only doctors can set availability")
    return await AvailabilityService.set_availability(
        doctor_id=current_user.id,
        start_time=availability.start_time,
        end_time=availability.end_time,
        db=db
    )

@router.get("/doctors/{doctor_id}/availability")
async def get_availability(
    doctor_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await AvailabilityService.get_doctor_availability(doctor_id, db)

