from server.services.usersService import UsersService
from server.authentication.loginUser import LoginUser
from server.authentication.registerUser import RegisterUser
from server.services.blockchainService import BlockchainService
from server.services.transactionsService import TransactionsService
from server.generateKeys.publicKey import PublicKey


# Class for manage users
class Manager:
    def __init__(self):
        self.users = UsersService()  # Instance of users
        self.blockchain = BlockchainService()  # Instance of blockchain
        self.public_key_server = PublicKey()  # Instance of public key server
        self.login_user = LoginUser()  # Instance of login user
        self.register_user = RegisterUser()  # Instance of register user
        self.transactions = TransactionsService()  # Instance of transactions
        self.authenticated_user = None  # Track logged-in user

    # Function for get public key server
    def get_public_key_server(self):
        # Get public key from server
        public_key = self.public_key_server.display_public_key_server()
        # Response public key
        response = {"status": "success", "public_key": public_key}
        # Return response
        return response

    # Function for set public key client
    def set_public_key_client(self, public_key_client):
        # Save public key
        public_key_client = self.public_key_server.save_public_key_client(
            public_key_client
        )
        # Response
        response = {"status": "success", "message": public_key_client}
        # Return response
        return response

    # Function to register user
    def register(self, user_name, user_email, user_password):
        # Register user
        message = self.register_user.register_user(user_name, user_email, user_password)
        # Response success
        response = {"status": "success", "message": message}
        # Return response
        return response

    # Function to login user
    def login(self, user_email, user_password):
        #  Login user
        message = self.authenticated_user = self.login_user.login_user(
            user_email, user_password
        )
        # Check if user is authenticated
        if self.authenticated_user:
            # Response success
            response = {"status": "success", "message": "User logged in"}
        else:
            # Response error
            response = {"status": "error", "message": message}
        # Return response
        return response

    # Function for help
    def help(self):
        # Response
        response = {
            "status": "success",
            "commands": {
                "get_public_key_server": "Get the public key of a user is method connected",
                "set_public_key_client": "Set the public key of a user is method connected",
                "check_connection": "Check connection between server and client",
                "register": "Register a new user",
                "login": "Login a user",
                "list_bag_actions": "List bag actions",
                "view_blockchain": "View the blockchain",
                "validate_blockchain": "Validate the blockchain",
                "my_transactions": "Show my transactions",
                "my_bag_actions": "Show my bag actions",
                "buy_action": "Buy an action",
                "sell_action": "Sell an action",
                "help": "Show help",
                "exit": "Exit",
            },
        }
        # Return response
        return response

    # Function for exit
    def exit(self):
        # Reset authenticated user
        self.authenticated_user = None
        # Response
        response = {"status": "success", "message": "Exit"}
        # Return response
        return response

    # Function for handling commands from client
    def handle_command(self, command, data):
        # Default response
        response = {"status": "error", "message": "Unknown command"}
        # Public commands
        # Help command
        if command == "help":
            # Get help
            response = self.help()
        # Register command
        elif command == "register":
            # Get user name, email and password
            user_name = data.get("user_name")
            user_email = data.get("user_email")
            user_password = data.get("user_password")
            # Register user
            response = self.register(user_name, user_email, user_password)
        # Login command
        elif command == "login":
            # Get user email and password
            user_email = data.get("user_email")
            user_password = data.get("user_password")
            # Login user
            response = self.login(user_email, user_password)
        # Get public key server command
        elif command == "get_public_key_server":
            # Get public key
            response = self.get_public_key_server()
        # Set public key client command
        elif command == "set_public_key_client":
            # Get public key
            public_key_client = data.get("public_key")
            # Set public key
            response = self.set_public_key_client(public_key_client)
        # Exit command
        elif command == "exit":
            # Exit
            response = self.exit()
        # Protected commands (require authentication)
        elif self.authenticated_user:
            # List bag actions command
            if command == "list_bag_actions":
                response = {
                    "status": "success",
                    "bag_actions": self.transactions.list_bag_actions(),
                }
            # View blockchain command
            elif command == "view_blockchain":
                response = {
                    "status": "success",
                    "blockchain": self.blockchain.get_chain(),
                }
            # Validate blockchain command
            elif command == "validate_blockchain":
                response = {
                    "status": "success",
                    "is_valid": self.blockchain.is_chain_valid(
                        self.blockchain.get_chain()
                    ),
                }
            # My transactions command
            elif command == "my_transactions":
                response = {
                    "status": "success",
                    "transactions": self.transactions.my_transactions(
                        self.authenticated_user
                    ),
                }
            # My bag actions command
            elif command == "my_bag_actions":
                response = {
                    "status": "success",
                    "bag_actions": self.transactions.my_bag_actions(
                        self.authenticated_user
                    ),
                }
            # Buy action command
            elif command == "buy_action":
                # Get data
                stock_name = data.get("stock_name")
                quantity = data.get("quantity")
                price = data.get("price")
                # Buy action
                self.transactions.buy_action(
                    self.authenticated_user, stock_name, quantity, price
                )
                # Response
                response = {"status": "success", "message": "Action bought"}
            # Sell action command
            elif command == "sell_action":
                # Get data
                stock_name = data.get("stock_name")
                quantity = data.get("quantity")
                price = data.get("price")
                # Sell action
                self.transactions.sell_action(
                    self.authenticated_user, stock_name, quantity, price
                )
                # Response
                response = {"status": "success", "message": "Action sold"}
            # Get users command
            elif command == "get_users":
                response = {
                    "status": "success",
                    "users": self.users.get_users(),
                }
        # If user is not logged in
        else:
            # If user tries to access protected commands without being logged in
            response = {
                "status": "error",
                "message": "Please log in to access this command",
            }
        # Return response
        return response
