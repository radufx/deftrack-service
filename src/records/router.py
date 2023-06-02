from typing import List
from fastapi import APIRouter, HTTPException, status

from src.records.schemas import Record
from src.records.service import record_service
from src.records import models

router = APIRouter(prefix="/records", tags=["records"])


@router.get("/{zone_id}", status_code=status.HTTP_200_OK)
def get_zone_records(zone_id: str):
    records = record_service.get_zone_records(zone_id)

    return {"message": "Succesfully retrieved zone records.", "data": records}


@router.post("/", status_code=status.HTTP_200_OK)
def add_zone_records(records: List[Record]):
    records = record_service.add_records(records)

    return {"message": "Succesfully added records.", "data": records}
