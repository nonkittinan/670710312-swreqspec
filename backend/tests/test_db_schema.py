from __future__ import annotations

from sqlalchemy import inspect

from app.db.models import AuditLog, Booking, Slot, Base
from app.db.session import engine, init_db


def test_db_schema_has_required_tables_and_fields() -> None:
    """Validates the schema for slots, bookings, and audit logs. This is a minimal test for T-01 completion."""
    init_db()
    inspector = inspect(engine)

    assert inspector.has_table("slots")
    assert inspector.has_table("bookings")
    assert inspector.has_table("audit_logs")

    slot_columns = {col["name"] for col in inspector.get_columns("slots")}
    booking_columns = {col["name"] for col in inspector.get_columns("bookings")}
    audit_columns = {col["name"] for col in inspector.get_columns("audit_logs")}

    assert {"id", "slot_date", "start_time", "package_code", "capacity", "remaining"}.issubset(slot_columns)
    assert {"id", "hn", "slot_id", "booking_date", "queue_no", "status", "created_at"}.issubset(booking_columns)
    assert {"id", "actor_id", "action", "hn", "accessed_at"}.issubset(audit_columns)

    assert "national_id" not in booking_columns
    assert "national_id" not in slot_columns
    assert "national_id" not in audit_columns

    assert Base.metadata.tables["slots"].columns["remaining"].nullable is False
