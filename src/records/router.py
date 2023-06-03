from typing import List
from fastapi import APIRouter, status

from src.records.utils import convert_record
from src.records.schemas import Record
from src.records.service import record_service

router = APIRouter(prefix="/records", tags=["records"])


@router.get("/", status_code=status.HTTP_200_OK)
def get_zone_records(zoneId: str):
    records = record_service.get_zone_records(zoneId)

    return {"message": "Succesfully retrieved zone records.", "data": records}


@router.post("/", status_code=status.HTTP_200_OK)
def add_zone_records(records: List[Record]):
    new_records = []
    for record in records:
        new_records.append(convert_record(record))

    new_records = record_service.add_records(new_records)

    return {"message": "Succesfully added records."}
