from typing import Optional
from sqlmodel import SQLModel, Field


# Class model for bag action
class BagActionModel(SQLModel, table=True):
    # Name of the table
    __tablename__ = "bag_actions"
    # Attributes
    id: Optional[int] = Field(default=None, primary_key=True, index=True)
    user_id: str
    operation_type: str
    stock_name: str
    quantity: int
    price: float

    # Config for the model
    class Config:
        arbitrary_types_allowed = True

    # Method for serializing the model
    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "operation_type": self.operation_type,
            "stock_name": self.stock_name,
            "quantity": self.quantity,
            "price": self.price,
        }
