from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: str
    email: str 
    name: Optional[str]
    last_name: Optional[str]
