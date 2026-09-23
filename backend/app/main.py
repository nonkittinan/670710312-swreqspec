from __future__ import annotations

from datetime import date, time, timedelta

from fastapi import FastAPI
from sqlalchemy import select

from app.db.models import Slot
from app.db.session import SessionLocal, init_db
from app.slots.router import router as slots_router


app = FastAPI(title="Booking API")


@app.on_event("startup")
def startup() -> None:
    """Initialize the database schema and seed demo data for the booking feature. Supports CON-TECH-01 and FR-BKG-01."""
    init_db()
    seed_demo_slots()


def seed_demo_slots() -> None:
    """Insert example slots so the UI has real data when the database is empty. Supports FR-BKG-01 and FR-BKG-06."""
    db = SessionLocal()
    try:
        has_rows = db.execute(select(Slot.id)).first() is not None
        if has_rows:
            return

        today = date.today()
        db.add_all(
            [
                Slot(slot_date=today + timedelta(days=1), start_time=time(9, 0), package_code="GENERAL", capacity=5, remaining=3),
                Slot(slot_date=today + timedelta(days=1), start_time=time(10, 0), package_code="GENERAL", capacity=5, remaining=2),
                Slot(slot_date=today + timedelta(days=1), start_time=time(13, 0), package_code="GENERAL", capacity=4, remaining=1),
                Slot(slot_date=today + timedelta(days=1), start_time=time(9, 0), package_code="PREMIUM", capacity=3, remaining=2),
            ]
        )
        db.commit()
    finally:
        db.close()


app.include_router(slots_router)
