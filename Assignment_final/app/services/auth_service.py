from passlib.context import CryptContext
from datetime import datetime, timedelta
from typing import Optional
import jwt

from app.models.user import User
from app.schemas.auth import UserCreate, UserLogin
from app.core.database import AsyncSessionLocal as async_session
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select

# Secret key for JWT
from app.core.config import settings

SECRET_KEY = settings.secret_key
ALGORITHM = settings.algorithm
# SECRET_KEY = "supersecret"  # replace with env variable for production
# ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


class AuthService:
    def __init__(self):
        pass

    async def register(self, user_data: UserCreate):
        async with async_session() as session:
            async with session.begin():
                # Check if user already exists
                result = await session.execute(select(User).filter_by(email=user_data.email))
                existing_user = result.scalar_one_or_none()
                if existing_user:
                    return {"error": "Email already registered"}

                hashed_password = pwd_context.hash(user_data.password)
                new_user = User(
                    email=user_data.email,
                    name=user_data.name,
                    role=user_data.role,
                    password_hash=hashed_password,
                )
                session.add(new_user)
            await session.commit()
            return {"message": "User registered successfully"}

    async def login(self, user_data: UserLogin):
        async with async_session() as session:
            async with session.begin():
                result = await session.execute(select(User).filter_by(email=user_data.email))
                user = result.scalar_one_or_none()
                if not user or not pwd_context.verify(user_data.password, user.password_hash):
                    return {"error": "Invalid email or password"}

                access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
                token = self.create_access_token(str(user.id), expires_delta=access_token_expires)
                return {"access_token": token, "token_type": "bearer"}

    def create_access_token(self, subject: str, expires_delta: Optional[timedelta] = None):
        to_encode = {
        "sub": subject,
        "exp": datetime.utcnow() + (expires_delta or timedelta(minutes=15))
        }
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

