from __future__ import annotations

from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

from app.db.session import SessionLocal
from app.slots.service import get_slots_for_range

router = APIRouter(prefix="/api", tags=["slots"])


def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/slots")
def list_slots(
    date_from: str | None = Query(default=None, alias="date_from"),
    package_code: str | None = Query(default=None, alias="package_code"),
    db: Session = Depends(get_db),
):
    """Return available booking slots for the next 30 days. Supports FR-BKG-01 and FR-BKG-06."""
    return get_slots_for_range(db, package_code, date_from)
