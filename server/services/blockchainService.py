import hashlib
import json
import datetime
from server.models.blockchainModel import BlockchainModel
from server.repositories.blockchainRepository import BlockchainRepository


# Class blockchain for manage blockchain
class BlockchainService:
    # Constructor
    def __init__(self):
        # Instance of blockchain repository
        self.blockchain_repository = BlockchainRepository()

    # Function for create block
    def create_block(self, proof, data, previous_hash):
        # Structure of block
        block = BlockchainModel(
            index=len(self.blockchain_repository.get_chain()) + 1,
            timestamp=str(datetime.datetime.now()),
            proof=proof,
            previous_hash=previous_hash,
        )
        ## Add data to block
        block.set_data(data)
        # Add hash to block
        block.hash = self.hash_block(block)
        # Return block
        return block

    # Function for proof of work
    def proof_of_work(self, previous_proof):
        # Proof of work
        new_proof = 1
        # Check proof
        check_proof = False
        # Loop until check_proof is True
        while check_proof is False:
            # Hash operation
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()
            ).hexdigest()
            # Check if hash_operation starts with 0000
            if hash_operation[:4] == "0000":
                check_proof = True
            else:
                new_proof += 1
        # Return new_proof
        return new_proof

    # Function for hash block
    def hash_block(self, block):
        # Check if block is dict
        if isinstance(block, dict):
            block_dict = block
        else:
            block_dict = block.to_dict()
        # Encode block
        encoded_block = json.dumps(block_dict, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    # Function for is chain valid
    def is_chain_valid(self, chain):
        # Check if chain is valid
        previous_block = chain[0]
        # Loop through chain
        block_index = 1
        # Loop until block_index is greater than len(chain)
        while block_index < len(chain):
            # Get block
            block = chain[block_index]
            # Check if block is valid
            if block["previous_hash"] != self.hash_block(previous_block):
                return False
            # Previous proof and proof
            previous_proof = previous_block["proof"]
            proof = block["proof"]
            # Hash operation
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()
            ).hexdigest()
            # Check if hash_operation starts with 0000
            if hash_operation[:4] != "0000":
                return False
            # Get previous block
            previous_block = block
            # Increment block_index
            block_index += 1
        # Return True
        return True

    # Function for add block
    def add_block(self, block):
        # Add block to chain
        self.blockchain_repository.add_block_to_chain(block)

    # Function for display blockchain
    def display_blockchain(self):
        # Print
        print("")
        print("------------*Blockchain*------------")
        # Print blockchain
        print(json.dumps(self.get_chain(), sort_keys=True, indent=4))
        print("------------*****************************------------")
        print("")

    def get_previous_block(self):
        # Get the last block
        block = self.blockchain_repository.get_last_block()
        # Ensure the block exists
        if not block:
            raise Exception("No block found!")
        return block

    # Function for get chain
    def get_chain(self):
        # Return chain
        return self.blockchain_repository.get_chain()

    # Function for get previus hash
    def get_previous_hash(self):
        # Return previous hash
        return self.get_previous_block().hash

    # Function to get all blocks with a specific user ID
    def get_blocks_with_user_id(self, user_id):
        # Serialize
        blocks = self.blockchain_repository.get_blocks_with_user_id(user_id)
        # Return blocks with user id
        return blocks

    # Function for test blockchain
    def test(self):
        # Create genesis block
        genesis_block = self.create_block(
            proof=1,
            data={
                "Genesis Block": "Genesis Block",
            },
            previous_hash="0",
        )

        # Add block
        self.add_block(genesis_block)

        # Create new block
        block1 = self.create_block(
            proof=self.proof_of_work(self.get_previous_block().proof),
            data={
                "user_id": "nID",
                "operation_type": "buy",
                "stock_name": "AAPL",
                "quantity": 10,
                "price": 150.00,
            },
            previous_hash=self.get_previous_hash(),
        )
        # Add block
        self.add_block(block1)

        # Create new block
        block2 = self.create_block(
            proof=self.proof_of_work(self.get_previous_block().proof),
            data={
                "user_id": "nID",
                "operation_type": "buy",
                "stock_name": "AAPL",
                "quantity": 10,
                "price": 150.00,
            },
            previous_hash=self.get_previous_hash(),
        )
        # Add block
        self.add_block(block2)

        # Display the blockchain
        self.display_blockchain()

        # Print the blockchain
        print(json.dumps(self.get_chain(), sort_keys=True, indent=4))

        # Check if blockchain is valid
        print(self.is_chain_valid(self.get_chain()))

        # Get blocks with user id
        print(self.get_blocks_with_user_id("nID"))

        # Get previous hash
        print(self.get_previous_hash())


# Run test if script is executed directly
if __name__ == "__main__":
    BlockchainService().test()
