from sqlalchemy import Column, String, Boolean, Float

from app.models.base_model import DBBaseModel


class RamStatus(DBBaseModel):
    used = Column(Float())
    free = Column(Float())
    total = Column(Float())
