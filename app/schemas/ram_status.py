from datetime import datetime
from typing import List

from pydantic.main import BaseModel


class RamStatusResponse(BaseModel):
    used: float
    free: float
    total: float
    created_at: datetime


class RamStatusListResponseSchema(BaseModel):
    data: List[RamStatusResponse]
