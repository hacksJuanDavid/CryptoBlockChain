import socket
import json
from client.generateKeys.publicKey import PublicKey
from client.cryptography.cryptography import Cryptography


# Class for manage
class Manager:
    # Constructor
    def __init__(self):
        self.public_key_client = PublicKey()  # Instance of public key
        self.config_server = ConfigClient()  # Instance of ConfigServer
        self.user_uuid = None  # Track logged-in user
        self.connection_configured = False  # Track connection configured
        self.authenticated_user = False  # Track logged-in user

    # Get public key server
    def get_public_key_server(self):
        # Get public key from server
        response = self.config_server.send_request("get_public_key_server")
        # Imprimir la respuesta para depuración
        print("Respuesta del servidor:", response)
        # Check if the response contains a valid public key
        if isinstance(response, dict) and "public_key_server" in response:
            public_key_server = response["public_key_server"]  # Get the public key
        else:
            raise ValueError("Invalid response from server not found public key")
        # Save public key
        self.public_key_client.save_public_key_server(public_key_server)
        # Return public key
        return public_key_server

    # Set public key client
    def set_public_key_client(self):
        # Get public key from client
        public_key_client = self.public_key_client.display_public_key_client()
        # Response public key
        request = self.config_server.send_request(
            "set_public_key_client",
            {"public_key_client": public_key_client},
        )
        print(public_key_client)
        # Print request
        print(request)
        # Return response
        return public_key_client

    # Register user
    def register(self, user_name, user_email, user_password):
        return self.config_server.send_request(
            "register",
            {
                "user_name": user_name,
                "user_email": user_email,
                "user_password": user_password,
            },
        )

    # Login user
    def login(self, user_email, user_password):
        return self.config_server.send_request(
            "login", {"user_email": user_email, "user_password": user_password}
        )

    # Function to check if the public key client is exist in server
    def check_public_key_client(self):
        return self.config_server.send_request("check_public_key_client")

    # Check connection
    def check_connection(self):
        # Check connection
        if not self.connection_configured:
            # Check public key server
            check_public_key_server = self.public_key_client.check_public_key_server()
            # Check public key client
            check_public_key_client = self.check_public_key_client()
            # If check public key server is True and check public key client is True
            if check_public_key_server and check_public_key_client:
                # Print  Connection configured
                print("")
                print("---------------*Connection configured successfully*------------")
                print("")
                # Save public key client
                self.connection_configured = True
            else:
                # Print Connection not configured
                print("")
                print("---------------*Connection not configured*------------")
                print("")
                self.connection_configured = False

    # Funciton list_bag_actions
    def list_bag_actions(self):
        return self.config_server.send_request("list_bag_actions")

    # View blockchain
    def view_blockchain(self):
        return self.config_server.send_request("view_blockchain")

    # Validate blockchain
    def validate_blockchain(self):
        return self.config_server.send_request("validate_blockchain")

    # My transactions
    def my_transactions(self):
        return self.config_server.send_request("my_transactions")

    # My bag actions
    def my_bag_actions(self):
        return self.config_server.send_request("my_bag_actions")

    # Buy bag action
    def buy_action(self, user_id, stock_name, quantity, price):
        return self.config_server.send_request(
            "buy_action",
            {
                "user_id": user_id,
                "stock_name": stock_name,
                "quantity": quantity,
                "price": price,
            },
        )

    # Sell bag action
    def sell_action(self, user_id, stock_name, quantity, price):
        return self.config_server.send_request(
            "sell_action",
            {
                "user_id": user_id,
                "stock_name": stock_name,
                "quantity": quantity,
                "price": price,
            },
        )

    # Get users
    def get_users(self):
        return self.config_server.send_request("get_users")

    # Logout
    def exit(self):
        return self.config_server.send_request("exit")

    # Help
    def help(self):
        return self.config_server.send_request("help")

    # Function to response
    def response(self, response):
        print(json.dumps(response, sort_keys=True, indent=4))

    # Intercambia claves públicas con el servidor
    def initialize_secure_connection(self):
        # Get public key server and save it
        self.get_public_key_server()
        # Set public key client
        self.set_public_key_client()

    # Function for menu config connection
    def menu_config_connection(self):
        # Menu
        while True:
            print("")
            print("-------*Menu for config connection*---------")
            print("1. Initialize secure connection")
            print("2. Check connection")
            print("3. Help")
            print("4. Exit")
            print("-------*****************************---------")
            print("")

            # Enter choice
            choice = input("Enter your choice:")
            # If choice are
            if choice == "1":
                print("")
                print("------------*Initialize secure connection*------------")
                # Initialize secure connection
                self.initialize_secure_connection()
                print("")
                print("------------*****************************------------")
                print("")

            elif choice == "2":
                # Print
                print("")
                print("------------*Check connection*------------")
                # Check connection
                self.check_connection()
                # If connection is True
                if self.connection_configured:
                    # Menu authenticated user
                    self.menu_users()
                print("")
                print("------------*****************************------------")
                print("")

            elif choice == "3":
                print("")
                print("------------*Help*------------")
                # Help
                self.response(self.help())
                print("")
                print("------------*****************************------------")
                print("")

            elif choice == "4":
                # Exit
                self.response(self.exit())
                break

            else:
                print("Invalid choice")

    # Function for menu users
    def menu_users(self):
        # Menu
        while True:
            print("")
            print("-------*Menu for authenticated user*---------")
            print("1. Register user")
            print("2. Login user")
            print("3. Help")
            print("4. Exit")
            print("-------*****************************---------")
            print("")

            # Enter choice
            choice = input("Enter your choice:")
            # If choice are
            if choice == "1":
                # Register user
                print("")
                print("-------*Register user*---------")
                # Enter user name
                user_name = input("Enter user name: ")
                # Enter user email
                user_email = input("Enter user email: ")
                # Enter user password
                user_password = input("Enter user password: ")
                # Register user
                register = self.register(user_name, user_email, user_password)
                # Print response
                self.response(register)
                print("")
                print("-------*****************************---------")
                print("")

            elif choice == "2":
                # Login user
                print("")
                print("-------*Login user*---------")
                # Enter user email
                user_email = input("Enter user email: ")
                # Enter user password
                user_password = input("Enter user password: ")
                # Login user
                login = self.user_uuid = self.login(user_email, user_password)
                # Print response
                self.response(login)
                print("")
                print("-------*****************************---------")
                print("")

                # Authenticated user
                self.authenticated_user = True
                # If user is authenticated
                if (
                    self.authenticated_user == True
                    and login["message"] == "User logged in"
                ):
                    # Menu authenticated user
                    self.menu_authenticated_user()

            elif choice == "3":
                print("")
                print("-------*Help*---------")
                # Help
                self.response(self.help())
                print("")
                print("-------*****************************---------")
                print("")

            elif choice == "4":
                # Exit
                self.response(self.exit())
                # Menu config connection
                self.menu_config_connection()

            else:
                print("Invalid choice")

    # Function for menu for authenticated user
    def menu_authenticated_user(self):
        # If user is authenticated
        if self.authenticated_user == True:
            # Menu
            while True:
                print("")
                print("-------*Welcome to CryptoBlockChain*---------")
                print("-------*Menu for authenticated user*---------")
                print("1. List Bag actions")
                print("2. View Blockchain")
                print("3. Validate Blockchain")
                print("4. My Transactions")
                print("5. My Bag actions")
                print("6. Buy Bag action")
                print("7. Sell Bag action")
                print("8. Get users")
                print("9. Help")
                print("10. Exit")
                print("-------*****************************---------")
                print("")

                # Enter choice
                choice = input("Enter your choice:")
                # If choice are
                if choice == "1":
                    print("")
                    print("------------*List bag actions*------------")
                    # List bag actions
                    self.response(self.list_bag_actions())
                    print("")
                    print("-------*****************************---------")
                    print("")

                elif choice == "2":
                    print("")
                    print("------------*View blockchain*------------")
                    # View blockchain
                    self.response(self.view_blockchain())
                    print("")
                    print("-------*****************************---------")
                    print("")

                elif choice == "3":
                    print("")
                    print("------------*Validate blockchain*------------")
                    # Validate blockchain
                    self.response(self.validate_blockchain())
                    print("")
                    print("-------*****************************---------")
                    print("")

                elif choice == "4":
                    print("")
                    print("------------*My transactions*------------")
                    # My transactions
                    self.response(self.my_transactions())
                    print("")
                    print("-------*****************************---------")
                    print("")

                elif choice == "5":
                    print("")
                    print("------------*My bag actions*------------")
                    # My bag actions
                    self.response(self.my_bag_actions())
                    print("")
                    print("-------*****************************---------")
                    print("")

                elif choice == "6":
                    # Buy action
                    print("")
                    print("------------*Buy action*------------")
                    # Get user id
                    user_id = self.user_uuid
                    # Enter stock name
                    stock_name = input("Enter stock name: ")
                    # Enter quantity
                    quantity = input("Enter quantity: ")
                    # Enter price
                    price = input("Enter price: ")
                    # Buy action
                    buy = self.buy_action(user_id, stock_name, quantity, price)
                    # Print response
                    self.response(buy)

                    print("")
                    print("-------*****************************---------")
                    print("")

                elif choice == "7":
                    # Sell action
                    print("")
                    print("------------*Sell action*------------")
                    # Get user id
                    user_id = self.user_uuid
                    # Enter stock name
                    stock_name = input("Enter stock name: ")
                    # Enter quantity
                    quantity = input("Enter quantity: ")
                    # Enter price
                    price = input("Enter price: ")
                    # Sell action
                    sell = self.sell_action(user_id, stock_name, quantity, price)
                    # Print response
                    self.response(sell)

                    print("")
                    print("-------*****************************---------")
                    print("")

                elif choice == "8":
                    print("")
                    print("------------*Get users*------------")
                    # Get users
                    print(self.get_users)
                    print("")
                    print("-------*****************************---------")
                    print("")

                elif choice == "9":
                    print("")
                    print("------------*Help*------------")
                    # Help
                    self.response(self.help())
                    print("")
                    print("-------*****************************---------")
                    print("")

                elif choice == "10":
                    # Exit
                    self.response(self.exit())
                    # Menu config connection
                    self.menu_config_connection()

                else:
                    print("Invalid choice")

    # Function for menu
    def menu(self):
        while True:
            if not self.connection_configured:
                self.menu_config_connection()
            elif not self.authenticated_user:
                self.menu_users()
            elif self.authenticated_user:
                self.menu_authenticated_user()


# Class for config client
class ConfigClient:
    # Constructor
    def __init__(self):
        self.cryptography = Cryptography()

    # Send request
    def send_request(self, command, data=None):
        host = "localhost"
        port = 12345
        try:
            client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client_socket.connect((host, port))
            # Prepare request
            request = {"command": command, "data": data or {}}
            # Send non-encrypted commands
            if command in ["get_public_key_server", "set_public_key_client"]:
                client_socket.sendall(json.dumps(request).encode("utf-8"))
            else:
                # Encrypt the request
                encrypted_request = self.cryptography.encrypt_data_server(
                    json.dumps(request)
                )
                client_socket.sendall(encrypted_request)
            # Receive response
            response_data = client_socket.recv(4096)
            if command in ["get_public_key_server", "set_public_key_client"]:
                # Parse non-encrypted response
                response = json.loads(response_data.decode("utf-8"))
            else:
                # Decrypt the response
                decrypted_response = self.cryptography.decrypt_data_client(
                    response_data
                )
                response = json.loads(decrypted_response)
            # Close client socket
            client_socket.close()
            # Return response
            return response
        # Handle exceptions
        except Exception as e:
            print(f"Error: {e}")
            return {"status": "error", "message": str(e)}
        # Close client socket
        finally:
            if client_socket:
                client_socket.close()

    # Start client
    def start_client(self):
        manager = Manager()
        manager.menu()


# Run test if script is executed directly
if __name__ == "__main__":
    ConfigClient().start_client()
