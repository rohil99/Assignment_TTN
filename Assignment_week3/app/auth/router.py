from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import UserRegister, UserLogin, TokenResponse
from app.auth.service import register_user, login_user

router = APIRouter(prefix="/auth", tags=["Authentication"])

@router.post("/register")
def register(payload: UserRegister, db: Session = Depends(get_db)):
    user = register_user(db, payload.email, payload.password)
    if not user:
        raise HTTPException(status_code=400, detail="User already exists")
    return {"message": "User registered successfully"}

@router.post("/login", response_model=TokenResponse)
def login(payload: UserLogin, db: Session = Depends(get_db)):
    token = login_user(db, payload.email, payload.password)
    if not token:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    return {"access_token": token}
