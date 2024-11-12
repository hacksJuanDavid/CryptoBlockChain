import hashlib
import json
import datetime


# Class blockchain for manage blockchain
class Blockchain:
    def __init__(self):
        # Initialize the blockchain
        self.chain = []
        # Create the genesis block
        self.create_block(proof=1, data="Genesis Block", previous_hash="0")

    # Function for create block
    def create_block(self, proof, data, previous_hash):
        # Structure of block
        block = {
            "index": len(self.chain) + 1,
            "timestamp": str(datetime.datetime.now()),
            "proof": proof,
            "data": data,
            "previous_hash": previous_hash,
        }
        # Add hash to block
        block["hash"] = self.hash_block(block)

        # Add block to chain
        self.chain.append(block)
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
        return new_proof

    # Function for hash block
    def hash_block(self, block):
        # Hash block with sort keys
        encoded_block = json.dumps(block, sort_keys=True).encode()
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
        return True

    # Function for add block
    def add_block(self, block):
        # Add block to chain
        self.chain.append(block)

    # Function for get last block
    def get_previous_block(self):
        # Get last block
        return self.chain[-1]

    # Function for get chain
    def get_chain(self):
        # Return chain
        return self.chain

    # Function for get previus hash
    def get_previous_hash(self):
        # Return previous hash
        return self.get_previous_block()["hash"]

    # Function for test blockchain
    def test(self):
        # Create new block
        self.create_block(
            proof=self.proof_of_work(self.get_previous_block()["proof"]),
            data={"user_id": "nID", "operation_type": "buy", "stock_name": "AAPL"},
            previous_hash=self.get_previous_hash(),
        )

        # Create new block
        self.create_block(
            proof=self.proof_of_work(self.get_previous_block()["proof"]),
            data={"user_id": "nID", "operation_type": "buy", "stock_name": "AAPL"},
            previous_hash=self.get_previous_hash(),
        )

        # Create new block
        self.create_block(
            proof=self.proof_of_work(self.get_previous_block()["proof"]),
            data={"user_id": "nID", "operation_type": "buy", "stock_name": "AAPL"},
            previous_hash=self.get_previous_hash(),
        )

        # Print the blockchain
        print(json.dumps(self.get_chain(), sort_keys=True, indent=4))


# Run test if script is executed directly
if __name__ == "__main__":
    Blockchain().test()
