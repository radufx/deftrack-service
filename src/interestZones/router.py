from typing import List
from fastapi import APIRouter, HTTPException, status

from src.interestZones.schemas import InterestZone, UpdateInterestZoneDTO
from src.interestZones.service import interest_zone_service
from src.interestZones import models

router = APIRouter(prefix="/interest-zones", tags=["interest-zones"])


@router.get("/{user_id}", status_code=status.HTTP_200_OK)
def get_user_zones(user_id: str):
    interest_zones = interest_zone_service.get_user_interest_zones(user_id)

    return {"message": "Succesfully retrieved zones.", "data": interest_zones}


@router.post("/", status_code=status.HTTP_200_OK)
def add_interest_zone(interest_zone: InterestZone):
    new_interest_zone = models.InterestZone(id='', userId=interest_zone.userId, name=interest_zone.name,
                                            description=interest_zone.description, lat=interest_zone.lat, lng=interest_zone.lng, priority=interest_zone.priority)
    new_interest_zone = interest_zone_service.add_interest_zone(
        new_interest_zone)

    return {"message": "Succesfully added interest zone.", "data": new_interest_zone}


@router.put("/{zone_id}", status_code=status.HTTP_200_OK)
def get_user_zones(interest_zone: UpdateInterestZoneDTO):
    interest_zone_service.update_zone_details(interest_zone)

    return {"message": "Succesfully updated zone."}
