from server.users.users import User
from server.users.loginUser import LoginUser
from server.users.registerUser import RegisterUser
from server.blockchain.blockchain import Blockchain
from server.transactions.transactions import Transactions


# Class for manage users
class Manager:
    def __init__(self):
        self.users = User()
        self.blockchain = Blockchain()
        self.login = LoginUser(self.users)
        self.register = RegisterUser(self.users)
        self.transactions = Transactions(self.blockchain)
        self.authenticated_user = None

    # Function menu for access users
    def menu_users(self):
        while True:
            print("-------*Menu for authenticated user*---------")
            print("1. Register user")
            print("2. Login user")
            print("3. Exit")
            print("-------*****************************---------")
            print("")

            # Enter choice
            choice = input("Enter your choice: ")
            # If choice are
            if choice == "1":
                print("")
                print("-------*Register user*---------")

                # Enter user name
                user_name = input("Enter user name: ")

                # Enter user email
                user_email = input("Enter user email: ")

                # Enter user password
                user_password = input("Enter user password: ")

                print("")

                # Register user
                self.register.register_user(user_name, user_email, user_password)

                print("-------*****************************---------")
                print("")

            elif choice == "2":
                print("")
                print("-------*Login user*---------")

                # Enter user email
                user_email = input("Enter user email: ")

                # Enter user password
                user_password = input("Enter user password: ")

                print("")

                # Login user
                self.authenticated_user = self.login.login_user(
                    user_email, user_password
                )

                print("-------*****************************---------")
                print("")

                # If authenticated user
                if self.authenticated_user is False:
                    self.menu_users()
                else:
                    # Menu authenticated user
                    self.menu_authenticated_user()

            elif choice == "3":
                # Exit
                break

    # Function menu for access authenticated user
    def menu_authenticated_user(self):
        while True:
            print("-------*Welcome to CryptoBlockChain*---------")
            print("-------*Menu for authenticated user*---------")
            print("1. List Bag actions")
            print("2. View Blockchain")
            print("3. Validate Blockchain")
            print("4. My Transactions")
            print("5. My Bag actions")
            print("6. Buy Bag action")
            print("7. Sell Bag action")
            print("8. Exit")
            print("-------*****************************---------")
            print("")

            # Enter choice
            choice = input("Enter your choice: ")
            # If choice are
            if choice == "1":
                # List Bag actions
                self.transactions.list_bag_actions()

            elif choice == "2":
                # View Blockchain
                self.blockchain.get_chain()

            elif choice == "3":
                # Check Blockchain
                self.blockchain.is_chain_valid(self.blockchain.get_chain())

            elif choice == "4":
                # My Transactions
                self.transactions.my_transactions()

            elif choice == "5":
                # My Bag actions
                self.transactions.my_bag_actions()

            elif choice == "6":
                # Buy Bag action
                self.transactions.buy_action()

            elif choice == "7":
                # Sell Bag action
                self.transactions.sell_action()

            elif choice == "8":
                # Exit
                break


# Call menu
manager = Manager()
manager.menu_users()
