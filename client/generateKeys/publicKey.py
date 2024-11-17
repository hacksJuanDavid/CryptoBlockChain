import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from client.generateKeys.privateKey import PrivateKey


# Class to create a public key using PKI
class PublicKey:
    # Constructor
    def __init__(self):
        # Get the private key
        self.private_key_client = PrivateKey().get_private_key_client()
        # Generate the public key client object (not bytes yet)
        self.public_key_client = self.private_key_client.public_key()

    # Function save the public key to a file
    def save_public_key_client(self):
        # Path to save the public key file
        directory_path = os.path.join(
            "/home/hacksjuanda/Desktop/ProjectsDeveloment/CryptoBlockChain/client/keys",
            "public_key_client.pem",
        )
        # Convert the public key to bytes and save it
        with open(directory_path, "wb") as file:
            file.write(
                self.public_key_client.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
            )
        # Return the response
        response = "Public key saved in public_key.pem"
        return response

    # Function to save the public key server to a file
    def save_public_key_server(self, public_key_server):
        # Remove any leading/trailing whitespace and ensure proper newline formatting
        public_key_server = public_key_server.strip()
        # Convert the public key string to bytes
        public_key_server_bytes = public_key_server.encode("utf-8")
        # Deserialize the public key from bytes
        public_key_server_obj = serialization.load_pem_public_key(
            public_key_server_bytes, backend=default_backend()
        )
        # Path to save the public key file
        directory_path = os.path.join(
            "/home/hacksjuanda/Desktop/ProjectsDeveloment/CryptoBlockChain/client/keys",
            "public_key_server.pem",
        )
        # Save the public key to the file
        with open(directory_path, "wb") as file:
            file.write(
                public_key_server_obj.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
            )
        # Return the response
        response = "Public key saved in public_key_server.pem"
        return response

    # Function to get public key client from file
    def get_public_key_client(self):
        # Path to the public key file
        directory_path = os.path.join(
            "/home/hacksjuanda/Desktop/ProjectsDeveloment/CryptoBlockChain/client/keys",
            "public_key_client.pem",
        )
        # Load the public key from the file
        with open(directory_path, "rb") as file:
            public_key = serialization.load_pem_public_key(
                file.read(), backend=default_backend()
            )
        # Return the public key
        return public_key

    # Function to get public key server from file
    def get_public_key_server(self):
        # Path to the public key file
        directory_path = os.path.join(
            "/home/hacksjuanda/Desktop/ProjectsDeveloment/CryptoBlockChain/client/keys",
            "public_key_server.pem",
        )
        # Load the public key from the file
        with open(directory_path, "rb") as file:
            public_key = serialization.load_pem_public_key(
                file.read(), backend=default_backend()
            )
        # Return the public key server
        return public_key

    # Function to display the public key client
    def display_public_key_client(self):
        # Get the public key
        public_key_client = self.get_public_key_client()
        # Transform the public key object to string
        public_key_client = public_key_client.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        ).decode("utf-8")
        # Return the public key client
        return public_key_client

    # Function to display the public key server
    def display_public_key_server(self):
        # Get the public key
        public_key_server = self.get_public_key_server()
        # Transform the public key object to string
        public_key_server = public_key_server.public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo,
        ).decode("utf-8")
        # Return the public key server
        return public_key_server

    # Function to chek if the public key server is valid and exists
    def check_public_key_server(self):
        # Path to the public key file
        directory_path = os.path.join(
            "/home/hacksjuanda/Desktop/ProjectsDeveloment/CryptoBlockChain/client/keys",
            "public_key_server.pem",
        )
        # Check if the file exists
        if os.path.exists(directory_path):
            return True
        else:
            return False

    # Function for test
    def test(self):
        # Save the public key client
        self.save_public_key_client()

        # Retrieve and print the public key
        self.get_public_key_client()

        # Save the public key server
        self.save_public_key_server(
            """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvUtse2rp38OXnlXXCzWu
isYXbKYB9dQZ77+t6mwP810x+VxEW3T5tmgctjYfp9yE29y/IfxxGBbl/2EuRAtn
R6jQcBe6c5LJED8MA/ecuEYdJx25F/ejee6gIanM0Mkz8yMJm/pL0AM7FtTZ9BG+
Q2P2DJQgXfYNiOQyFBiQbygceSZNLxnkmJ1PnkpblfO3lElEluc6+SThU96QXLHP
3xZ73VhQQWcR41E00dXgA27Wx0MTGzTn++9V+WSQ8DvC4cqZS+7lg+GcIYr1KGzs
MnMKHCMBOTiJz1ZOUhPRkIRai4UklwyhbuEpsEHJyVSTYb+Zf9auKfTPaGGS5bm5
8QIDAQAB
-----END PUBLIC KEY-----"""
        )

        # Retrieve and print the public key
        self.get_public_key_server()

        # Display the public key
        self.display_public_key_server()

        # Display the public key
        self.display_public_key_client()


# Run test if script is executed directly
if __name__ == "__main__":
    PublicKey().test()
