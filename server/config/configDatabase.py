from sqlmodel import create_engine, Session, SQLModel


# Class for configuring the database
class ConfigDatabase:
    # Constructor
    def __init__(self, database_url="sqlite:///server/data/database.db"):
        self.engine = create_engine(database_url)
        # Create tables using SQLModel's metadata
        SQLModel.metadata.create_all(
            self.engine, checkfirst=True
        )  # Creates tables if they don't exist

    # Create a session
    def create_session(self):
        return Session(self.engine)
