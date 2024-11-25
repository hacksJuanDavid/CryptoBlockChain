from sqlmodel import select
from server.config.configDatabase import ConfigDatabase
from server.models.blockchainModel import BlockchainModel


# Class for blockchain repository
class BlockchainRepository:
    # Constructor
    def __init__(self):
        # Instance of ConfigDatabase    
        self.config_db = ConfigDatabase()

    # Method for execute query
    def _execute_query(self, statement):
        with self.config_db.create_session() as session:
            return session.exec(statement).all()

    # Method for get all blocks
    def get_chain(self):
        # Statement
        statement = select(BlockchainModel)
        # Execute statement
        blocks = self._execute_query(statement)
        # Serialization
        blocks = [block.to_dict() for block in blocks]
        # return blocks
        return blocks

    # Method for get last block
    def get_last_block(self):
        # Statement to get the last block
        statement = (
            select(BlockchainModel).order_by(BlockchainModel.index.desc()).limit(1)
        )
        # Execute statement
        blocks = self._execute_query(statement)
        # Return the first block if available, otherwise return None
        return blocks[0].to_dict()        

    # Method for get blocks with user id
    def get_blocks_with_user_id(self, user_id):
        # Statement
        statement = select(BlockchainModel).where(
            BlockchainModel.data.contains(f'"user_id": "{user_id}"')
        )
        # Execute statement
        blocks = self._execute_query(statement)
        # Serialization
        blocks = [block.to_dict() for block in blocks]
        # Return blocks
        return blocks

    # Method for add block
    def add_block_to_chain(self, block):
        with self.config_db.create_session() as session:
            session.add(block)
            session.commit()
            session.refresh(block)
        return block
