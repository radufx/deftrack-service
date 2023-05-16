from src.database import db
from src.users.models import User


class UserService():
    def get_all_users(self):
        return db.query(User).all()

    def create_user(self, user: User):
        db.add(user)
        db.commit()


user_service = UserService()
