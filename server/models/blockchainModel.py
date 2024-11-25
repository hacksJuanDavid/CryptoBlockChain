from sqlalchemy import Text
from sqlmodel import SQLModel, Field
from typing import Optional, Dict
import json


# Class model for blockchain
class BlockchainModel(SQLModel, table=True):
    # Name of the table
    __tablename__ = "blockchain"
    # Atributes
    index: Optional[int] = Field(default=None, primary_key=True)
    timestamp: str
    proof: int
    data: str = Field(default="")  # Using Text type for data
    hash: str
    previous_hash: str

    # Config
    class Config:
        arbitrary_types_allowed = True

    # Function for serializing data
    def set_data(self, data: Dict):
        self.data = json.dumps(data)

    # Function for deserializing data
    def get_data(self) -> Dict:
        return json.loads(self.data)

    # Function to convert the model to a dictionary
    def to_dict(self):
        """Método para convertir el modelo a un diccionario serializable"""
        return {
            "index": self.index,
            "timestamp": self.timestamp,
            "proof": self.proof,
            "data": self.get_data(),
            "hash": self.hash,
            "previous_hash": self.previous_hash,
        }
    