# import uuid

from sqlalchemy import Column, DateTime, Boolean, func, Integer
# from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import declared_attr

from app.utils.utils import camel_to_snake

Base = declarative_base()  # https://docs.sqlalchemy.org/en/13/orm/extensions/declarative/mixins.html


class DBBaseModel(Base):
    @declared_attr
    def __tablename__(cls):
        return camel_to_snake(cls.__name__)

    id = Column(Integer, primary_key=True, index=True)
    # id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime, default=func.now())
    # is_deleted = Column(Boolean, default=False)

    __abstract__ = True
