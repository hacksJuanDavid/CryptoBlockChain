from server.cryptography.cryptography import Cryptography
from server.services.usersService import UsersService


# Class for login user in system
class LoginUser:
    # Constructor
    def __init__(self):
        # Instance of users
        self.users = UsersService()
        # Instance of cryptography
        self.cryptography = Cryptography()

    # Function to login user
    def login_user(self, user_email, user_password):
        # Encrypt the input email and password
        encrypted_email = self.cryptography.hash_email(user_email)
        # Get user by email
        user = self.users.get_user_by_email(encrypted_email)
        # If user not found
        if user is None:
            print("User not found")
            return False
        # Verify the password by hashing
        password_hash = user.user_password
        verified = self.cryptography.verify_hash_password(user_password, password_hash)
        # Verify the password by hashing
        if verified:
            response = "User logged in successfully"
            return user.user_uuid
        else:
            response = "Incorrect password"
            return response

    # Function to test
    def test(self):
        # Login user
        self.login_user("7V2tE@example.com", "password123")


# Run test if script is executed directly
if __name__ == "__main__":
    LoginUser().test()
