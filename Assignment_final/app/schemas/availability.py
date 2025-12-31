from pydantic import BaseModel
from datetime import datetime

class AvailabilityBase(BaseModel):
    start_time: datetime
    end_time: datetime

class AvailabilityCreate(AvailabilityBase):
    pass

class AvailabilityRead(AvailabilityBase):
    id: int

    class Config:
        from_attributes = True
