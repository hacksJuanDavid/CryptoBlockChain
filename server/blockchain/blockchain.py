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
        block = {
            "index": len(self.chain) + 1,
            "timestamp": str(datetime.datetime.now()),
            "proof": proof,
            "data": data,
            "previous_hash": previous_hash,
        }
        self.chain.append(block)
        return block

    # Function for get last block
    def get_previous_block(self):
        return self.chain[-1]

    # Function for proof of work
    def proof_of_work(self, previous_proof):
        new_proof = 1
        check_proof = False
        while check_proof is False:
            hash_operation = hashlib.sha256(
                str(new_proof**2 - previous_proof**2).encode()
            ).hexdigest()
            if hash_operation[:4] == "0000":
                check_proof = True
            else:
                new_proof += 1
        return new_proof

    # Function for hash block
    def hash_block(self, block):
        encoded_block = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()

    # Function for is chain valid
    def is_chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
        while block_index < len(chain):
            block = chain[block_index]
            if block["previous_hash"] != self.hash_block(previous_block):
                return False
            previous_proof = previous_block["proof"]
            proof = block["proof"]
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()
            ).hexdigest()
            if hash_operation[:4] != "0000":
                return False
            previous_block = block
            block_index += 1
        return True

    # Function for add block
    def add_block(self, block):
        self.chain.append(block)

    # Function for get chain
    def get_chain(self):
        return self.chain

    # Function for test blockchain
    def test(self):
        # Create new block
        self.create_block(
            proof=1,
            data={"user_id": "nID", "operation_type": "buy", "stock_name": "AAPL"},
            previous_hash=self.hash_block(self.get_previous_block()),
        )

        # Print the blockchain
        print(json.dumps(self.get_chain(), sort_keys=True, indent=4))


# Run test if script is executed directly
if __name__ == "__main__":
    Blockchain().test()
