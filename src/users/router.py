from typing import List
from fastapi import APIRouter, HTTPException, status

from src.users.schemas import User
from src.users.service import user_service
from src.users import models

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/", status_code=status.HTTP_200_OK)
def get_all_users():
    users = user_service.get_all_users()

    return {"message": "Succesfully retrieved all users.", "data": users}


@router.put("/{user_id}", status_code=status.HTTP_201_CREATED)
def update_user(user: User):
    new_user = models.User(id=user.id, email=user.email)

    user_service.update_user(new_user)
    return {"message": "Succesfully created user.", "data": user}


@router.get("/{user_id}", response_model=User, status_code=status.HTTP_200_OK)
def get_user(user_id: str):
    user = user_service.get_user(user_id)

    if user is None:
        return HTTPException(status=404)
    return user
