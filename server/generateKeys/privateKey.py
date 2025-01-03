import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa


# Class for create a private key using PKI
class PrivateKey:
    # Constructor
    def __init__(self):
        # Generate private key
        self.private_key_server = rsa.generate_private_key(
            public_exponent=65537, key_size=2048, backend=default_backend()
        )

    # Function to save private key server in a file
    def save_private_key_server(self, private_key_server):
        # Path folder
        directory_path = os.path.join(
            "/home/hacksjuanda/Desktop/ProjectsDeveloment/CryptoBlockChain/server/keys",
            "private_key_server.pem",
        )
        # Save private key in a file
        with open(directory_path, "wb") as file:
            file.write(
                private_key_server.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption(),
                )
            )
        # Return response
        response = "Private key saved in private_key_server.pem"
        return response

    # Function to get private key server from a file
    def get_private_key_server(self):
        # Path folder
        directory_path = os.path.join(
            "/home/hacksjuanda/Desktop/ProjectsDeveloment/CryptoBlockChain/server/keys",
            "private_key_server.pem",
        )
        # Load private key
        with open(directory_path, "rb") as file:
            private_key = serialization.load_pem_private_key(
                file.read(), password=None, backend=default_backend()
            )
        # Return private key server
        return private_key

    # Function for test
    def test(self):
        # Save private key
        self.save_private_key_server(self.private_key_server)

        # Get private key
        self.get_private_key_server()


# Run test if script is executed directly
if __name__ == "__main__":
    PrivateKey().test()
