from sqlmodel import select
from server.models.userModel import UserModel
from server.config.configDatabase import ConfigDatabase


# Class for user repository
class UserRepository:
    def __init__(self):
        # Instance of ConfigDatabase
        self.config_db = ConfigDatabase()

    # Method to execute a query
    def _execute_query(self, statement):
        with self.config_db.create_session() as session:
            return session.exec(statement).all()

    # Method to get all users
    def get_users(self):
        statement = select(UserModel)
        return self._execute_query(statement)

    # Method to get user by uuid
    def get_user_by_uuid(self, uuid):
        statement = select(UserModel).where(UserModel.user_uuid == uuid)
        users = self._execute_query(statement)
        return users[0] if users else None

    # Method to get user by email
    def get_user_by_email(self, email):
        statement = select(UserModel).where(UserModel.user_email == email)
        users = self._execute_query(statement)
        return users[0] if users else None

    # Method to create user
    def create_user(self, user):
        with self.config_db.create_session() as session:
            session.add(user)
            session.commit()
            session.refresh(user)
        return user

    # Method to update user
    def update_user(self, user):
        with self.config_db.create_session() as session:
            session.merge(user)
            session.commit()
            session.refresh(user)
        return user

    # Method to delete user
    def delete_user(self, user):
        with self.config_db.create_session() as session:
            session.delete(user)
            session.commit()
            session.refresh(user)
        return user
