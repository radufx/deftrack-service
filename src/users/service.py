from fastapi import HTTPException
from src.database import db
from src.users.models import User


class UserService():
    def get_all_users(self):
        return db.query(User).all()

    def update_user(self, user: User):
        db_user = db.query(User).filter_by(email=user.email).first()
        if db_user is not None:
            raise HTTPException(
                status_code=400, detail="User with given email already exists")

        try:
            db.add(user)
            db.commit()
        except:
            db.rollback()
            raise HTTPException(status_code=500)

    def get_user(self, id: str):
        user = db.query(User).filter(User.id == id).first()

        return user


user_service = UserService()
