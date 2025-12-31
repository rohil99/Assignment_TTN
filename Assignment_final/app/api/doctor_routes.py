from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
from app.services.doctor_service import DoctorService
from app.schemas.doctor import DoctorRead
from app.core.dependencies import get_db
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.availability import AvailabilityCreate, AvailabilityRead
from app.services.availability_service import AvailabilityService
from app.core.dependencies import get_db, get_current_user

router = APIRouter()

@router.get("/", response_model=List[DoctorRead])
async def list_doctors(db: AsyncSession = Depends(get_db)):
    return await DoctorService.list_all_doctors(db)

@router.get("/{doctor_id}/availability", response_model=List[AvailabilityRead])
async def get_doctor_availability(
    doctor_id: int,
    db: AsyncSession = Depends(get_db)
):
    return await DoctorService.get_availability(doctor_id, db)

@router.post("/availability", response_model=AvailabilityRead)
async def set_availability(
    data: AvailabilityCreate,
    db: AsyncSession = Depends(get_db),
    current_user=Depends(get_current_user)
):
    if current_user.role.lower() != "doctor":
        raise HTTPException(status_code=403, detail="Only doctors can set availability")

    return await AvailabilityService.set_availability(
        doctor_id=current_user.id,
        start_time=data.start_time,
        end_time=data.end_time,
        db=db
    )
