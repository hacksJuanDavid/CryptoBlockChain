import json


# Class for manage transactions
class Transactions:
    # List of bag actions
    bag_actions = [
        {
            "user_id": "nID1",
            "operation_type": "buy",
            "stock_name": "AAPL",
            "quantity": 10,
            "price": 150.00,
        },
        {
            "user_id": "nID2",
            "operation_type": "sell",
            "stock_name": "GOOGL",
            "quantity": 5,
            "price": 2800.00,
        },
        {
            "user_id": "nID3",
            "operation_type": "buy",
            "stock_name": "AMZN",
            "quantity": 2,
            "price": 3300.00,
        },
        {
            "user_id": "nID4",
            "operation_type": "buy",
            "stock_name": "TSLA",
            "quantity": 8,
            "price": 700.00,
        },
        {
            "user_id": "nID5",
            "operation_type": "sell",
            "stock_name": "MSFT",
            "quantity": 12,
            "price": 305.00,
        },
        {
            "user_id": "nID6",
            "operation_type": "buy",
            "stock_name": "AAPL",
            "quantity": 10,
            "price": 150.00,
        },
        {
            "user_id": "nID7",
            "operation_type": "sell",
            "stock_name": "GOOGL",
            "quantity": 5,
            "price": 2800.00,
        },
        {
            "user_id": "nID8",
            "operation_type": "buy",
            "stock_name": "AMZN",
            "quantity": 2,
            "price": 3300.00,
        },
        {
            "user_id": "nID9",
            "operation_type": "buy",
            "stock_name": "TSLA",
            "quantity": 8,
            "price": 700.00,
        },
        {
            "user_id": "nID10",
            "operation_type": "sell",
            "stock_name": "MSFT",
            "quantity": 12,
            "price": 305.00,
        },
    ]

    # Constructor
    def __init__(self, blockchain):
        # Instance of blockchain
        self.blockchain = blockchain

    # Function to list bag actions
    def list_bag_actions(self):
        return self.bag_actions

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
        # Create new block
        self.blockchain.create_block(
            proof=self.blockchain.proof_of_work(
                self.blockchain.get_previous_block()["proof"]
            ),
            data={
                "user_id": user_id,
                "operation_type": "buy",
                "stock_name": stock_name,
                "quantity": quantity,
                "price": price,
            },
            previous_hash=self.blockchain.get_previous_hash(),
        )
        # Return buy action
        return json.dumps(
            self.blockchain.get_previous_block(), sort_keys=True, indent=4
        )

    # Function to sell
    def sell_action(self, user_id, stock_name, quantity, price):
        # Create new block
        self.blockchain.create_block(
            proof=self.blockchain.proof_of_work(
                self.blockchain.get_previous_block()["proof"]
            ),
            data={
                "user_id": user_id,
                "operation_type": "sell",
                "stock_name": stock_name,
                "quantity": quantity,
                "price": price,
            },
            previous_hash=self.blockchain.get_previous_hash(),
        )
        # Return sell action
        return json.dumps(
            self.blockchain.get_previous_block(), sort_keys=True, indent=4
        )

    # Function to test class
    def test(self):
        # List bag actions
        self.list_bag_actions()

        # My transactions
        self.my_transactions("nID1")

        # Buy action
        self.buy_action("nID1", "AAPL", 10, 150.00)

        # Sell action
        self.sell_action("nID1", "AAPL", 10, 150.00)

        # My bag actions
        self.my_bag_actions()


# Run test if script is executed directly
if __name__ == "__main__":
    Transactions().test()
