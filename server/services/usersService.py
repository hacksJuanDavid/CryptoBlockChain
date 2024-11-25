# Class for user in system
from server.models.userModel import UserModel
from server.repositories.userRepository import UserRepository


class UsersService:
    # Constructor
    def __init__(self):
        # Instance of user repository
        self.user_repository = UserRepository()

    # Function to get list of users
    def get_users(self):
        return self.user_repository.get_users()

    # Function to get user by uuid
    def get_user_by_uuid(self, uuid):
        return self.user_repository.get_user_by_uuid(uuid)

    # Function to get user by email
    def get_user_by_email(self, email):
        return self.user_repository.get_user_by_email(email)

    # Function to add user
    def add_user(self, user):
        return self.user_repository.create_user(user)

    # Function to remove user
    def remove_user(self, user):
        return self.user_repository.delete_user(user)

    # Function to update user
    def update_user(self, user):
        return self.user_repository.update_user(user)

    # Function to test
    def test(self):
        # Add user
        new_user = UserModel(
            user_uuid="uuid1233231321",
            user_name="David Jimenez",
            user_email="Jimenez.doe@example.com",
            user_password="securepassword",
        )

        self.add_user(new_user)

        # # Get user by email
        user = self.get_user_by_email("Jimenez.doe@example.com")
        print(user)

        # Get user by uuid
        user = self.get_user_by_uuid("uuid1233231321")
        print(user)

        # Update user
        user = UserModel(
            user_uuid="uuid1233231321",
            user_name="David Jimenez",
            user_email="Jimenez.doe@example.com",
            user_password="securepassword",
        )
        self.update_user(user)

        # Remove user
        user = UserModel(
            user_uuid="uuid1233231321",
            user_name="David Jimenez",
            user_email="Jimenez.doe@example.com",
            user_password="securepassword",
        )
        self.remove_user(user)

        # Get list of users
        users = self.get_users()
        print(users)

        # Test done
        print("Test done")


# Run test if script is executed directly
if __name__ == "__main__":
    UsersService().test()
