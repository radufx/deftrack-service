from sqlalchemy import String, Column, Numeric, TIMESTAMP
from src.database import Base


class Record(Base):
    __tablename__ = "records"
    id = Column(String, primary_key=True)
    userId = Column(String)
    zoneId = Column(String)
    image = Column(String)
    description = Column(String)
    vegetationRate = Column(Numeric)
    notes = Column(String)
    timestamp = Column(TIMESTAMP)
