from typing import Optional
from pydantic import BaseModel


class Record(BaseModel):
    id: str
    userId: str
    zoneId: str
    vegetationRate: float
    timestamp: int
    image: str
    notes: str
    description: str

    class Config:
        orm_mode = True
