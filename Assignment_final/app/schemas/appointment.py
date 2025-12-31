from pydantic import BaseModel
from datetime import datetime

class AppointmentCreate(BaseModel):
    doctor_id: int
    appointment_time: datetime

class AppointmentRead(BaseModel):
    id: int
    doctor_id: int
    patient_id: int
    appointment_time: datetime

    class Config:
        from_attributes = True
