from fastapi import HTTPException
from pyparsing import List


from src.database import db
from src.records.models import Record
from src.utils.model import prediction_model


class RecordService():
    def get_zone_records(self, zoneId: str):
        records = db.query(Record).filter_by(
            zoneId=zoneId).order_by(Record.timestamp)

        if records.count() == 0:
            return []

        return records.all()

    def add_records(self, records: List[Record]):
        for record in records:
            record.vegetationRate = prediction_model.getImageVegetationRate(
                record.image)

        try:
            db.add_all(records)
            db.commit()
        except Exception as ex:
            print(ex)
            db.rollback()
            raise HTTPException(status_code=500)

        return records


record_service = RecordService()
