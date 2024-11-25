import json
from server.models.bagActionModel import BagActionModel
from server.repositories.bagActionRepository import BagActionRepository
from server.services.blockchainService import BlockchainService


# Class for manage transactions
class TransactionsService:
    # Constructor
    def __init__(self):
        # Instance of bag action repository
        self.bag_actions = BagActionRepository()
        # Instance of blockchain service
        self.blockchain = BlockchainService()

    # Function to add bag action
    def add_bag_action(self, bag_action):
        return self.bag_actions.add_bag_action(bag_action)

    # Function to list bag actions
    def list_bag_actions(self):
        return self.bag_actions.get_bag_actions()

    # Function to my bag actions
    def my_bag_actions(self, user_id):
        # Get blocks with user id
        blocks = self.blockchain.get_blocks_with_user_id(user_id)
        # Return blocks
        return blocks

    # Function to my transactions
    def my_transactions(self, user_id):
        # Get blocks with user id
        blocks = self.blockchain.get_blocks_with_user_id(user_id)
        # Return blocks
        return blocks

    # Function to buy
    def buy_action(self, user_id, stock_name, quantity, price):
        # Get previous block
        previous_block = self.blockchain.get_previous_block()
        # Access to attributes of previous block
        proof = self.blockchain.proof_of_work(previous_block["proof"])
        previous_hash = previous_block["hash"]
        # Create new block
        block = self.blockchain.create_block(
            proof=proof,
            data={
                "user_id": user_id,
                "operation_type": "buy",
                "stock_name": stock_name,
                "quantity": quantity,
                "price": price,
            },
            previous_hash=previous_hash,
        )
        # Add block  in blockchain repository
        self.blockchain.add_block(block)
        # Return buy action
        block_dict = block.to_dict()
        # Ya no es necesario llamar a to_dict, simplemente devuelve el bloque
        return json.dumps(block_dict, sort_keys=True, indent=4)

    # Function to sell
    def sell_action(self, user_id, stock_name, quantity, price):
        # Get previous block
        previous_block = self.blockchain.get_previous_block()
        # Access to attributes of previous block
        proof = self.blockchain.proof_of_work(previous_block["proof"])
        previous_hash = previous_block["hash"]
        # Create new block
        block = self.blockchain.create_block(
            proof=proof,
            data={
                "user_id": user_id,
                "operation_type": "sell",
                "stock_name": stock_name,
                "quantity": quantity,
                "price": price,
            },
            previous_hash=previous_hash,
        )
        # Add block  in blockchain repository
        self.blockchain.add_block(block)
        # Return buy action
        block_dict = block.to_dict()
        # Ya no es necesario llamar a to_dict, simplemente devuelve el bloque
        return json.dumps(block_dict, sort_keys=True, indent=4)

    # Function to test class
    def test(self):
        # Add bag actions
        new_bag_actions = BagActionModel(
            user_id="nID1",
            operation_type="buy",
            stock_name="AAPL",
            quantity=10,
            price=150.00,
        )
        # Add bag action
        self.add_bag_action(new_bag_actions)

        # Add bag actions
        new_bag_actions = BagActionModel(
            user_id="nID1",
            operation_type="sell",
            stock_name="AAPL",
            quantity=10,
            price=150.00,
        )
        # Add bag action
        self.add_bag_action(new_bag_actions)

        # Add bag actions
        new_bag_actions = BagActionModel(
            user_id="nID1",
            operation_type="buy",
            stock_name="AAPL",
            quantity=10,
            price=150.00,
        )
        # Add bag action
        self.add_bag_action(new_bag_actions)

        # List bag actions
        print(self.list_bag_actions())

        # My transactions
        print(self.my_transactions("nID1"))

        # Buy action
        print(self.buy_action("nID1", "AAPL", 10, 150.00))

        # Sell action
        print(self.sell_action("nID1", "AAPL", 10, 150.00))

        # # My bag actions
        print(self.my_bag_actions("nID1"))


# Run test if script is executed directly
if __name__ == "__main__":
    TransactionsService().test()
