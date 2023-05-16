from typing import Optional
from pydantic import BaseModel, Field


class User(BaseModel):
    id: str
    email: str
    first_name: Optional[str]
    last_name: Optional[str]

    class Config:
        orm_mode = True
