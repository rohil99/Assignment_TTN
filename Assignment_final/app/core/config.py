# app/core/config.py
from pydantic_settings import BaseSettings  # changed import

class Settings(BaseSettings):
    database_url: str = "mysql+asyncmy://root:your_root_password@localhost:3306/doctor_app"
    secret_key: str = "supersecret"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 60

    class Config:
        env_file = ".env"
        from_attributes = True  # v2 replacement for orm_mode

settings = Settings()
