from server.users.users import User
from server.users.loginUser import LoginUser
from server.users.registerUser import RegisterUser
from server.generateKeys.publicKey import PublicKey
from server.generateKeys.privateKey import PrivateKey


# Class for manage users
class Manager:
    def __init__(self):
        self.users = User()
        self.login = LoginUser(self.users)
        self.register = RegisterUser(self.users)

    # Function to menu
    def menu(self):
        while True:
            print("1. Register user")
            print("2. Login user")
            print("3. Get users")
            print("4. Exit")

            choice = input("Enter your choice: ")
            if choice == "1":
                # Enter user name
                user_name = input("Enter user name: ")

                # Enter user email
                user_email = input("Enter user email: ")

                # Enter user password
                user_password = input("Enter user password: ")

                # Register user
                self.register.register_user(user_name, user_email, user_password)

            elif choice == "2":
                # Enter user email
                user_email = input("Enter user email: ")

                # Enter user password
                user_password = input("Enter user password: ")

                # Login user
                self.login.login_user(user_email, user_password)

            elif choice == "3":
                # Get users
                self.users.get_users()

            elif choice == "4":
                # Exit
                break


# Call menu
manager = Manager()
manager.menu()
