from sqlalchemy import desc
from sqlmodel import Session

from app.models.ram_status import RamStatus


def ram_status_create(db: Session, used: float, free: float, total: float) -> None:
    obj_ = RamStatus(
        used=used,
        free=free,
        total=total,
    )
    db.add(obj_)
    db.commit()


def ram_status_list(db: Session, limit: int, ):
    return db.query(
        RamStatus.used,
        RamStatus.free,
        RamStatus.total,
        RamStatus.created_at,
    ) \
        .order_by(desc(RamStatus.id)) \
        .limit(limit) \
        .all()
