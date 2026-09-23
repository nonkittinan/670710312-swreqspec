from __future__ import annotations

from fastapi import FastAPI

from app.db.session import init_db
from app.slots.router import router as slots_router


app = FastAPI(title="Booking API")


@app.on_event("startup")
def startup() -> None:
    """Initialize the database schema and seed demo data for the booking feature. Supports CON-TECH-01 and FR-BKG-01."""
    init_db()


app.include_router(slots_router)
