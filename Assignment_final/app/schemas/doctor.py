# app/schemas/doctor.py
from pydantic import BaseModel

class DoctorRead(BaseModel):
    id: int
    name: str
    email: str

    class Config:
        from_attributes = True
