from sqlalchemy.orm import Session
from app.models import User
from app.auth.utils import hash_password, verify_password, create_access_token
import os

def register_user(db: Session, email: str, password: str):
    if db.query(User).filter(User.email == email).first():
        return None
    user = User(email=email, password=hash_password(password))
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def login_user(db: Session, email: str, password: str):
    user = db.query(User).filter(User.email == email).first()
    if not user or not verify_password(password, user.password):
        return None
    token = create_access_token(
        {"sub": user.email},
        int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 60))  # safe default
    )
    return token
