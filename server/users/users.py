# Class for user in system
class User:
    # List of users
    users = []

    # Constructor
    def __init__(self):
        pass

    # Function to get list of users
    def get_users(self):
        return self.users

    # Function to add user
    def add_user(self, user):
        self.users.append(user)

    # Function to remove user
    def remove_user(self, user):
        self.users.remove(user)

    # Function to update user
    def update_user(self, user):
        self.users[self.users.index(user)] = user

    # Function to get user by email
    def get_user_by_email(self, email):
        for user in self.users:
            if user.get("user_email") == email:
                return user
        return None

    # Function to get user by uuid
    def get_user_by_uuid(self, uuid):
        for user in self.users:
            if user.get("user_uuid") == uuid:
                return user
        return None

    # Function to get user by name
    def get_user_by_name(self, name):
        for user in self.users:
            if user.get("user_name") == name:
                return user
        return None

    # Function to get user by public key
    def get_user_by_public_key(self, public_key):
        for user in self.users:
            if user.get("user_public_key") == public_key:
                return user
        return None

    # Function to test
    def test(self):
        # Add user
        user = {
            "user_name": "John Doe",
            "user_email": "7V2tE@example.com",
            "user_password": "password123",
            "user_public_key": "public_key",
            "user_uuid": "uuid",
        }
        self.add_user(user)

        # Get user by email
        user = self.get_user_by_email("7V2tE@example.com")
        print(user)

        # Get user by uuid
        user = self.get_user_by_uuid("uuid")
        print(user)

        # Get user by name
        user = self.get_user_by_name("John Doe")
        print(user)

        # Get user by public key
        user = self.get_user_by_public_key("public_key")
        print(user)

        # Update user
        user = {
            "user_name": "John Doe",
            "user_email": "7V2tE@example.com",
            "user_password": "password123",
            "user_public_key": "public_key",
            "user_uuid": "uuid",
        }
        self.update_user(user)

        # Remove user
        user = {
            "user_name": "John Doe",
            "user_email": "7V2tE@example.com",
            "user_password": "password123",
            "user_public_key": "public_key",
            "user_uuid": "uuid",
        }
        self.remove_user(user)

        # Get list of users
        users = self.get_users()
        print(users)

        # Test done
        print("Test done")


# Run test if script is executed directly
if __name__ == "__main__":
    User().test()
