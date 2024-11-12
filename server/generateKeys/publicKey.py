import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from server.generateKeys.privateKey import PrivateKey


# Class to create a public key using PKI
class PublicKey:
    # Constructor
    def __init__(self):
        # Get the private key
        self.private_key = PrivateKey().get_private_key()

        # Generate the public key object (not bytes yet)
        self.public_key = self.private_key.public_key()

    # Function save the public key to a file
    def save_public_key(self):
        # Path to save the public key file
        directory_path = os.path.join(
            "/home/hacksjuanda/Desktop/ProjectsDeveloment/CryptoBlockChain/server/keys",
            "public_key.pem",
        )

        # Convert the public key to bytes and save it
        with open(directory_path, "wb") as file:
            file.write(
                self.public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
            )
        print("Public key saved in public_key.pem")

    # Function to get public key from file
    def get_public_key(self):
        # Path to the public key file
        directory_path = os.path.join(
            "/home/hacksjuanda/Desktop/ProjectsDeveloment/CryptoBlockChain/server/keys",
            "public_key.pem",
        )

        # Load the public key from the file
        with open(directory_path, "rb") as file:
            public_key = serialization.load_pem_public_key(
                file.read(), backend=default_backend()
            )

        # Return the public key
        return public_key

    # Function for test
    def test(self):
        # Save the public key
        self.save_public_key()

        # Retrieve and print the public key
        self.get_public_key()


# Run test if script is executed directly
if __name__ == "__main__":
    PublicKey().test()
