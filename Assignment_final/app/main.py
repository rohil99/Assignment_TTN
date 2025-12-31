from fastapi import FastAPI
from app.api import auth_routes, doctor_routes, appointment_routes

app = FastAPI()

app.include_router(auth_routes.router, prefix="/auth", tags=["Auth"])
app.include_router(doctor_routes.router, prefix="/doctors", tags=["Doctors"])
app.include_router(appointment_routes.router, prefix="/appointments", tags=["Appointments"])

from app.core.database import engine, Base

@app.on_event("startup")
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
