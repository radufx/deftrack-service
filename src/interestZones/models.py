from sqlalchemy import String, Column, Numeric
from src.database import Base


class InterestZone(Base):
    __tablename__ = "interestZones"
    id = Column(String, primary_key=True)
    userId = Column(String)
    name = Column(String)
    description = Column(String)
    lat = Column(Numeric)
    lng = Column(Numeric)
    priority = Column(String)

    def __repr__(self):
        return f"<Zone id={self.id} name={self.name} userId={self.userId} descritpion={self.description} priority={self.priority}"
