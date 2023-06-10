from fastapi import HTTPException
import uuid

from src.interestZones.schemas import UpdateInterestZoneDTO
from src.database import db
from src.interestZones.models import InterestZone


class InterestZoneService():
    def get_user_interest_zones(self, userId: str):
        interest_zones = db.query(InterestZone).filter_by(userId=userId)
        if interest_zones.count() == 0:
            return []

        return interest_zones.all()

    def get_zone_ids(self):
        interest_zones = db.query(InterestZone.id)
        if interest_zones.count() == 0:
            return []

        return interest_zones.all()

    def add_interest_zone(self, interestZone: InterestZone):
        interestZone.id = str(uuid.uuid4())
        try:
            db.add(interestZone)
            db.commit()
        except Exception as ex:
            print(ex)
            db.rollback()
            raise HTTPException(status_code=500)

        return interestZone

    def update_zone_details(self, interestZone: UpdateInterestZoneDTO):
        interest_zone = db.query(InterestZone).filter_by(
            id=interestZone.id).first()
        interest_zone.description = interestZone.description
        interest_zone.name = interestZone.name
        interest_zone.priority = interestZone.priority

        try:
            db.commit()
        except Exception as ex:
            print(ex)
            db.rollback()
            raise HTTPException(status_code=500)

    def get_zone(self, id: str):
        interest_zone = db.query(InterestZone).filter(
            InterestZone.id == id).first()

        return interest_zone


interest_zone_service = InterestZoneService()
