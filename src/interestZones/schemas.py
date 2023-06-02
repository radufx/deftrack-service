from typing import Optional
from pydantic import BaseModel


class InterestZone(BaseModel):
    id: str
    userId: str
    lat: float
    lng: float
    name: str
    description: Optional[str]
    priority: str

    class Config:
        orm_mode = True


class UpdateInterestZoneDTO(BaseModel):
    name: str
    description: Optional[str]
    priority: str
    id: str
