from pydantic import BaseModel, EmailStr

# Request model for user registration
class UserCreate(BaseModel):
    email: EmailStr
    password: str
    name: str
    role: str  # "doctor" or "patient"

# Request model for login
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Response model (optional)
class UserResponse(BaseModel):
    id: int
    email: EmailStr
    name: str
    role: str

    class Config:
        orm_mode = True
