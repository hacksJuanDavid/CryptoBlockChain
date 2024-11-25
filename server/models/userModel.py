from sqlmodel import SQLModel, Field


# Class model for user
class UserModel(SQLModel, table=True):
    # Name of the table
    __tablename__ = "users"
    # Attributes
    user_uuid: str = Field(primary_key=True)
    user_name: str
    user_email: str
    user_password: str
