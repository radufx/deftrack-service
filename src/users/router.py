from typing import List
from fastapi import APIRouter, status

from src.users.schemas import User
from src.users.service import user_service
from src.users import models

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", status_code=200)
def get_all_users():
    users = user_service.get_all_users()

    return {"message": "Succesfully retrieved all users.", "data": users}


@router.post("/", status_code=status.HTTP_201_CREATED)
def creat_user(user: User):
    new_user = models.User(id=user.id, email=user.email)

    user_service.create_user(new_user)
    return {"message": "Succesfully created user.", "data": user}
