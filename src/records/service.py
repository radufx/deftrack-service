from fastapi import HTTPException
import uuid
from pyparsing import List


from src.database import db
from src.records.models import Record


class RecordService():
    def get_zone_records(self, zoneId: str):
        records = db.query(Record).filter_by(zoneId=zoneId)

        if records is None:
            return []

        return records

    def add_records(self, records: List[Record]):
        for record in records:
            record.id = uuid.uuid4()

        try:
            db.add_all(records)
            db.commit()
        except:
            db.rollback()
            raise HTTPException(status_code=500)

        return records


record_service = RecordService()
