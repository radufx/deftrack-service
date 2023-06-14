from typing import List
from fastapi import APIRouter, HTTPException, status

from src.interestZones.schemas import InterestZone, UpdateInterestZoneDTO
from src.interestZones.service import interest_zone_service
from src.interestZones import models

router = APIRouter(prefix="/interest-zones", tags=["interest-zones"])


@router.get("/", status_code=status.HTTP_200_OK)
def get_user_zones(userId: str):
    interest_zones = interest_zone_service.get_user_interest_zones(userId)

    return {"message": "Succesfully retrieved zones.", "data": interest_zones}


@router.get("/ids", status_code=status.HTTP_200_OK)
def get_zone_ids():
    ids = interest_zone_service.get_zone_ids()

    return {"message": "Succesfully retrieved zones.", "data": [value for value, in ids]}


@router.post("/", status_code=status.HTTP_200_OK)
def add_interest_zone(interest_zone: InterestZone):
    new_interest_zone = models.InterestZone(id='', userId=interest_zone.userId, name=interest_zone.name,
                                            description=interest_zone.description, lat=interest_zone.lat, lng=interest_zone.lng, priority=interest_zone.priority)
    new_interest_zone = interest_zone_service.add_interest_zone(
        new_interest_zone)

    return {"message": "Succesfully added interest zone.", "data": new_interest_zone}


@router.put("/{zone_id}", status_code=status.HTTP_200_OK)
def update_zone(interest_zone: UpdateInterestZoneDTO):
    interest_zone_service.update_zone_details(interest_zone)

    return {"message": "Succesfully updated zone."}


@router.get("/{zone_id}", status_code=status.HTTP_200_OK)
def get_user_zones(zone_id: str):
    interest_zone = interest_zone_service.get_zone(zone_id)

    return {"message": "Succesfully retrieved zone.", "data": interest_zone}
