from sqlmodel import select
from server.config.configDatabase import ConfigDatabase
from server.models.bagActionModel import BagActionModel


# Class for bag action repository
class BagActionRepository:
    def __init__(self):
        # Instance of ConfigDatabase
        self.config_db = ConfigDatabase()

    # Method to execute a query
    def _execute_query(self, statement):
        with self.config_db.create_session() as session:
            return session.exec(statement).all()

    # Method to get all bag actions
    def get_bag_actions(self):
        # Statement
        statement = select(BagActionModel)
        # Execute statement
        bag_actions = self._execute_query(statement)
        # Serialization
        bag_actions = [bag_action.to_dict() for bag_action in bag_actions]
        # Return bag actions
        return bag_actions

    # Method to add a bag action
    def add_bag_action(self, bag_action):
        with self.config_db.create_session() as session:
            session.add(bag_action)
            session.commit()
            session.refresh(bag_action)
        return bag_action

    # Method to update a bag action
    def update_bag_action(self, bag_action):
        with self.config_db.create_session() as session:
            session.merge(bag_action)
            session.commit()
            session.refresh(bag_action)
        return bag_action

    # Method to delete a bag action
    def delete_bag_action(self, bag_action):
        with self.config_db.create_session() as session:
            session.delete(bag_action)
            session.commit()
            session.refresh(bag_action)
        return bag_action
