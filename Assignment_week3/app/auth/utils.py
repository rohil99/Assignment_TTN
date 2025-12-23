from passlib.context import CryptContext
from datetime import datetime, timedelta
import jwt
import os

SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

# Password hashing
pwd_context = CryptContext(schemes=["bcrypt"])

def hash_password(password: str):
    # Truncate to 72 bytes for bcrypt
    truncated = password.encode('utf-8')[:72]  # encode to bytes first
    return pwd_context.hash(truncated)



def verify_password(plain_password: str, hashed_password: str):
    return pwd_context.verify(plain_password.encode('utf-8')[:72], hashed_password)



# JWT token creation
def create_access_token(data: dict, expires_minutes: int = 60):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt
