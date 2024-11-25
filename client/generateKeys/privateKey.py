import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


# Class for create a private key using PKI
class PrivateKey:
    # Constructor
    def __init__(self):
        # Generate private key
        self.private_key_client = rsa.generate_private_key(
            public_exponent=65537, key_size=2048, backend=default_backend()
        )

    # Function to access to directory keys and file private_key_client.pem
    def access_keys_client(self):
        # Base dirt folder project
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # Access to folder keys
        keys_dir = os.path.join(base_dir, "..", "keys")
        # Access to file private_key_client.pem
        private_key_client_path = os.path.join(keys_dir, "private_key_client.pem")
        # Return path
        return private_key_client_path

    # Function to save private key in a file
    def save_private_key_client(self, private_key_client):
        # Access to file private_key_client.pem
        private_key_client_path = self.access_keys_client()
        # Save private key
        with open(private_key_client_path, "wb") as file:
            file.write(
                private_key_client.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption(),
                )
            )
        # Return response
        response = "Private key saved in private_key_client.pem"
        return response

    # Function to get private key
    def get_private_key_client(self):
        # Access to file private_key_client.pem
        private_key_client_path = self.access_keys_client()
        # Load private key
        with open(private_key_client_path, "rb") as file:
            private_key = serialization.load_pem_private_key(
                file.read(), password=None, backend=default_backend()
            )
        # Return private key
        return private_key

    # Function for test
    def test(self):
        # Save private key
        self.save_private_key_client(self.private_key_client)

        # Get private key
        self.get_private_key_client()


# Run test if script is executed directly
if __name__ == "__main__":
    PrivateKey().test()
