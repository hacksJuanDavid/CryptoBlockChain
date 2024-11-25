from uuid import uuid4
from server.cryptography.cryptography import Cryptography
from server.generateKeys.publicKey import PublicKey
from server.services.usersService import UsersService
from server.models.userModel import UserModel


# Class for register user in blockchain using PKI
class RegisterUser:
    # Constructor
    def __init__(self):
        # Instance of users
        self.users = UsersService()
        # Instance of PublicKey
        self.public_key_server = PublicKey()
        # Instance of Cryptography
        self.cryptography = Cryptography()

    # Function to generate uuid
    def generate_uuid(self):
        return str(uuid4())

    # Function register user
    def register_user(self, user_name, user_email, user_password):
        # Encrypt data
        encrypted_name = self.cryptography.encrypt_data_server(user_name)
        encrypted_email = self.cryptography.hash_email(user_email)
        encrypted_password = self.cryptography.hash_password(user_password)
        # Check email exist in users
        user = self.users.get_user_by_email(encrypted_email)
        # If exist user return False
        if user is not None:
            response = "User already exist"
            return response
        # New user
        new_user = UserModel(
            user_uuid=self.generate_uuid(),
            user_name=encrypted_name,
            user_email=encrypted_email,
            user_password=encrypted_password,
        )
        # Save user
        self.users.add_user(new_user)
        # Response
        response = "User created with success"
        return response

    # Function to test
    def test(self):
        # register user
        self.register_user("John Doe", "7V2tE@example.com", "password123")


# test
if __name__ == "__main__":
    RegisterUser().test()
