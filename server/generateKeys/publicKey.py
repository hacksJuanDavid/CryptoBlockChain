import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from server.generateKeys.privateKey import PrivateKey


# Class to create a public key using PKI
class PublicKey:
    # Constructor
    def __init__(self):
        # Get the private key
        self.private_key_server = PrivateKey().get_private_key_server()
        # Generate the public key object (not bytes yet)
        self.public_key_server = self.private_key_server.public_key()

    # Function to access to directory keys and file public_key_server.pem
    def access_keys_server(self):
        # Base dirt folder project
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # Access to folder keys
        keys_dir = os.path.join(base_dir, "..", "keys")
        # Access to file public_key_server.pem
        public_key_server_path = os.path.join(keys_dir, "public_key_server.pem")
        # Return path
        return public_key_server_path
    
    # Function to access to directory keys and file public_key_client.pem
    def access_keys_client(self):
        # Base dirt folder project
        base_dir = os.path.dirname(os.path.abspath(__file__))
        # Access to folder keys
        keys_dir = os.path.join(base_dir, "..", "keys")
        # Access to file public_key_client.pem
        public_key_client_path = os.path.join(keys_dir, "public_key_client.pem")
        # Return path
        return public_key_client_path

    # Function save the public key server to a file
    def save_public_key_server(self):
        # Access to directory keys and file public_key_server.pem
        public_key_server_path = self.access_keys_server()
        # Convert the public key to bytes and save it
        with open(public_key_server_path, "wb") as file:
            file.write(
                self.public_key_server.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
            )
        # Return the response
        response = "Public key saved in public_key_server.pem"
        return response

    # Function save the public key client to a file
    def save_public_key_client(self, public_key_client):
        # Remove any leading/trailing whitespace and ensure proper newline formatting
        public_key_client = public_key_client.strip()
        # Convert the public key string to bytes
        public_key_client_bytes = public_key_client.encode("utf-8")
        # Deserialize the public key from bytes
        public_key_client_obj = serialization.load_pem_public_key(
            public_key_client_bytes, backend=default_backend()
        )
        # Path to save the public key file
        public_key_client_path = self.access_keys_client()
        # Save the public key to the file
        with open(public_key_client_path, "wb") as file:
            file.write(
                public_key_client_obj.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo,
                )
            )
        # Return the response
        response = "Public key saved in public_key_client.pem"
        return response

    # Function to get public server key from file
    def get_public_key_server(self):
        # Access to directory keys and file public_key_server.pem
        public_key_server_path = self.access_keys_server()
        # Load the public key from the file
        with open(public_key_server_path, "rb") as file:
            public_key_server = serialization.load_pem_public_key(
                file.read(), backend=default_backend()
            )
        # Return the public key server
        return public_key_server

    # Function to get public key client from file
    def get_public_key_client(self):
        # Access to directory keys and file public_key_client.pem
        public_key_client_path = self.access_keys_client()
        # Load the public key from the file
        with open(public_key_client_path, "rb") as file:
            public_key_client = serialization.load_pem_public_key(
                file.read(), backend=default_backend()
            )
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

    # Function to check if the public key client is valid and exists
    def check_public_key_client(self):
        # Access to directory keys and file public_key_client.pem
        public_key_client_path = self.access_keys_client()
        # Check if the file exists
        if os.path.exists(public_key_client_path):
            return True
        else:
            return False

    # Function for test
    def test(self):
        # Save the public key
        self.save_public_key_server()

        # Retrieve and print the public key
        self.get_public_key_server()

        # Save the public key
        self.save_public_key_client(
            """-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAsgRfFazM2rSmAEzq8nVK
noqjWiEA2O+YiYk703DHNo6v56TcQ8TuRVm4xOk0LSCuhnBNn9b0salxTxOt5x4j
t9PEXUlyFobmYVYSnIEHsUh5lU+7unrYknYwCjTdYi11IA1zV9IsD7v3xbfUmRcE
CaSgKBP0piVuQ8ugDwY2dk+0vaoqFn6qRNn3ZpumW9+BZ+qBCWmK5CFN7s+aREUq
EQ6lJPS7c9w/TGOdS9Ch3ZbUulgYs/5VfE60sVjk6z4AfFOTxtt/g6XJhvRkv0m/
g3SQH31EF3o6YKA5pOmQftEc7SNvgZCIP+akWImEH1JsCVns0qdX2VxIAcciepf+
hwIDAQAB
-----END PUBLIC KEY-----"""
        )

        # Retrieve and print the public key
        self.get_public_key_client()

        # Display the public key
        self.display_public_key_server()

        # Display the public key
        self.display_public_key_client()


# Run test if script is executed directly
if __name__ == "__main__":
    PublicKey().test()
