from typing import List
from src.records.schemas import Record
from src.records import models


def convert_record(record: Record) -> models.Record:
    return models.Record(id=record.id, userId=record.userId, zoneId=record.zoneId, notes=record.notes, description=record.description, timestamp=record.timestamp, vegetationRate=record.vegetationRate, image=record.image)
