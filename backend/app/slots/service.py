from __future__ import annotations

from datetime import date, datetime, timedelta

from sqlalchemy.orm import Session

from app.db.models import Slot


def get_slots_for_range(db: Session, package_code: str | None, date_from: str | None) -> list[dict]:
    """Return slot availability and remaining capacity for the next 30 days. Supports FR-BKG-01 and FR-BKG-06."""
    start_date = _parse_date(date_from) if date_from else date.today()
    end_date = start_date + timedelta(days=29)

    query = db.query(Slot).filter(Slot.slot_date >= start_date, Slot.slot_date <= end_date)
    if package_code:
        query = query.filter(Slot.package_code == package_code)

    rows = query.order_by(Slot.slot_date.asc(), Slot.start_time.asc()).all()

    return [
        {
            "id": row.id,
            "slot_date": row.slot_date.isoformat(),
            "start_time": row.start_time.strftime("%H:%M"),
            "end_time": _end_time(row.start_time),
            "package_code": row.package_code,
            "capacity": row.capacity,
            "remaining": row.remaining,
        }
        for row in rows
    ]


def _parse_date(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def _end_time(start_time) -> str:
    hours = int(start_time.strftime("%H"))
    minutes = int(start_time.strftime("%M"))
    total = hours * 60 + minutes + 60
    end_hours, end_minutes = divmod(total, 60)
    return f"{end_hours:02d}:{end_minutes:02d}"
