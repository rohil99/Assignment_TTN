from fastapi import APIRouter, Depends
from app.schemas.auth import UserCreate, UserLogin
from app.services.auth_service import AuthService

router = APIRouter()

auth_service = AuthService()

@router.post("/register")
async def register(user: UserCreate):
    return await auth_service.register(user)

@router.post("/login")
async def login(user: UserLogin):
    return await auth_service.login(user)
