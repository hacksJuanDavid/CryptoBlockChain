import hashlib
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from server.generateKeys.publicKey import PublicKey
from server.generateKeys.privateKey import PrivateKey


# Class for cryptography using PKI and RSA
class Cryptography:
    # Constructor
    def __init__(self):
        # Instance of public key client
        self.public_key_client = PublicKey().get_public_key_client()
        # Instance of public key server
        self.public_key_server = PublicKey().get_public_key_server()
        # Instance of private key server
        self.private_key_server = PrivateKey().get_private_key_server()

    # Function for encrypt data server
    def encrypt_data_server(self, data):
        # Check if data is already bytes; if not, encode to bytes
        if not isinstance(data, bytes):
            data = data.encode("utf-8")
        # Maximum size for RSA encryption (depends on key size and padding)
        max_chunk_size = self.public_key_server.key_size // 8 - 2 * 32 - 2
        # Split data into chunks and encrypt each chunk
        encrypted_data = b""
        for i in range(0, len(data), max_chunk_size):
            chunk = data[i : i + max_chunk_size]
            encrypted_chunk = self.public_key_server.encrypt(
                chunk,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
            encrypted_data += encrypted_chunk
        # Return encrypted data as bytes
        return encrypted_data

    # Function for decrypt data server
    def decrypt_data_server(self, data):
        # Decrypt data in chunks
        decrypted_data = b""
        chunk_size = self.private_key_server.key_size // 8
        for i in range(0, len(data), chunk_size):
            chunk = data[i : i + chunk_size]
            decrypted_chunk = self.private_key_server.decrypt(
                chunk,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
            decrypted_data += decrypted_chunk
        # Return decrypted data as string
        return decrypted_data.decode("utf-8")

    # Function for encrypt data client
    def encrypt_data_client(self, data):
        # Check if data is already bytes; if not, encode to bytes
        if not isinstance(data, bytes):
            data = data.encode("utf-8")
        # Maximum size for RSA encryption (depends on key size and padding)
        max_chunk_size = self.public_key_client.key_size // 8 - 2 * 32 - 2
        # Split data into chunks and encrypt each chunk
        encrypted_data = b""
        for i in range(0, len(data), max_chunk_size):
            chunk = data[i : i + max_chunk_size]
            encrypted_chunk = self.public_key_client.encrypt(
                chunk,
                padding.OAEP(
                    mgf=padding.MGF1(algorithm=hashes.SHA256()),
                    algorithm=hashes.SHA256(),
                    label=None,
                ),
            )
            encrypted_data += encrypted_chunk
        # Return encrypted data as bytes
        return encrypted_data

    # Function for hash email
    def hash_email(self, email):
        return hashlib.sha256(email.encode("utf-8")).hexdigest()

    # Function for verify hash email
    def verify_hash_email(self, email, hash_email):
        return hashlib.sha256(email.encode("utf-8")).hexdigest() == hash_email

    # Function for hash password
    def hash_password(self, password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest()

    # Function for verify hash password
    def verify_hash_password(self, password, hash_password):
        return hashlib.sha256(password.encode("utf-8")).hexdigest() == hash_password

    # Function to test
    def test(self):
        # Encrypt data and print result
        print(self.encrypt_data_server("Hello world"))

        # Hash email and print result
        print(self.hash_email("7V2tE@example.com"))

        # Verify hash email and print result
        print(
            self.verify_hash_email(
                "7V2tE@example.com", self.hash_email("7V2tE@example.com")
            )
        )
        # Hash password and print result
        print(self.hash_password("password"))

        # Verify hash password and print result
        print(self.verify_hash_password("password", self.hash_password("password")))

        # Encrypt data and print result
        print(self.encrypt_data_client("Hello world"))

        # Decrypt data and print result
        print(self.decrypt_data_server(self.encrypt_data_server("Hello world")))


# Run test if script is executed directly
if __name__ == "__main__":
    Cryptography().test()
