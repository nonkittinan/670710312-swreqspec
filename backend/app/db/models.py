from __future__ import annotations

from datetime import date, datetime, time

from sqlalchemy import DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    pass


class Slot(Base):
    """Stores available booking slots for each package and time window. Supports FR-BKG-01, FR-BKG-06, and CON-TECH-01."""

    __tablename__ = "slots"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    slot_date: Mapped[date] = mapped_column(nullable=False, index=True)
    start_time: Mapped[time] = mapped_column(nullable=False)
    package_code: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    capacity: Mapped[int] = mapped_column(Integer, nullable=False)
    remaining: Mapped[int] = mapped_column(Integer, nullable=False)

    bookings: Mapped[list["Booking"]] = relationship(back_populates="slot")


class Booking(Base):
    """Stores a single booking record and keeps only HN for patient identification. Supports IF-HIS-01 and FR-BKG-04."""

    __tablename__ = "bookings"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    hn: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    slot_id: Mapped[int] = mapped_column(ForeignKey("slots.id"), nullable=False, index=True)
    booking_date: Mapped[date] = mapped_column(nullable=False, index=True)
    queue_no: Mapped[str | None] = mapped_column(String(50), nullable=True)
    status: Mapped[str] = mapped_column(String(20), nullable=False, default="booked")
    created_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)

    slot: Mapped[Slot] = relationship(back_populates="bookings")


class AuditLog(Base):
    """Tracks all access to booking data. Supports DOM-PDPA-01 and the retention requirement for audit records."""

    __tablename__ = "audit_logs"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    actor_id: Mapped[str] = mapped_column(String(100), nullable=False, index=True)
    action: Mapped[str] = mapped_column(String(100), nullable=False)
    hn: Mapped[str] = mapped_column(String(50), nullable=False, index=True)
    accessed_at: Mapped[datetime] = mapped_column(DateTime, nullable=False, default=datetime.utcnow)
