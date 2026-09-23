from __future__ import annotations

from datetime import date, time

from fastapi.testclient import TestClient

from app.db.models import Slot
from app.db.session import SessionLocal, init_db
from app.main import app


client = TestClient(app)


def seed_slots() -> None:
    db = SessionLocal()
    try:
        db.query(Slot).delete()
        db.add_all(
            [
                Slot(slot_date=date(2026, 9, 24), start_time=time(9, 0), package_code="GENERAL", capacity=5, remaining=3),
                Slot(slot_date=date(2026, 9, 24), start_time=time(10, 0), package_code="GENERAL", capacity=5, remaining=2),
                Slot(slot_date=date(2026, 9, 25), start_time=time(9, 0), package_code="PREMIUM", capacity=4, remaining=1),
            ]
        )
        db.commit()
    finally:
        db.close()


def test_get_slots_returns_available_slots() -> None:
    init_db()
    seed_slots()

    response = client.get("/api/slots", params={"date_from": "2026-09-24", "package_code": "GENERAL"})

    assert response.status_code == 200
    payload = response.json()
    assert len(payload) == 2
    assert payload[0]["start_time"] == "09:00"
    assert payload[0]["remaining"] == 3
    assert payload[1]["start_time"] == "10:00"
    assert payload[1]["remaining"] == 2
