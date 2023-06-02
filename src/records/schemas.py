from typing import Optional
from pydantic import BaseModel


class Record(BaseModel):
    id: str
    userId: str
    zoneID: str
    vegetationRate: float
    timestamp: int
    image: str
    notes: Optional[str]

    class Config:
        orm_mode = True
