from sqlalchemy import Column, String
from src.database import Base


class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True)
    email = Column(String(50), nullable=False, unique=True)
    first_name = Column(String(30), default="")
    last_name = Column(String(30), default="")

    def __repr__(self):
        return f"<User email={self.email} first_name={self.first_name} last_name={self.last_name}"
