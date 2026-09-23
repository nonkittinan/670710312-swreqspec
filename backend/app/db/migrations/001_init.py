from __future__ import annotations

from sqlalchemy import Engine

from backend.app.db.models import Base


def upgrade(engine: Engine) -> None:
    """Create the initial PostgreSQL-compatible booking schema. Supports CON-TECH-01, DOM-PDPA-01, and IF-HIS-01."""
    Base.metadata.create_all(bind=engine)
