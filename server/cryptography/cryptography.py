import hashlib
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from server.generateKeys.publicKey import PublicKey
from server.generateKeys.privateKey import PrivateKey


# Class for cryptography using PKI and RSA
class Cryptography:
    # Constructor
    def __init__(self):
        # Instance of public key
        self.public_key = PublicKey().get_public_key()
        # Instance of private key
        self.private_key = PrivateKey().get_private_key()

    # Function for encrypt data
    def encrypt_data(self, data):
        # Check if data is already bytes; if not, encode to bytes
        if not isinstance(data, bytes):
            data = data.encode("utf-8")
        # Encrypt data
        return self.public_key.encrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        )

    # Function for decrypt data
    def decrypt_data(self, data):
        # decrypt data
        return self.private_key.decrypt(
            data,
            padding.OAEP(
                mgf=padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None,
            ),
        ).decode("utf-8")

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
        print(self.encrypt_data("Hello world"))
        # Decrypt data and print result
        print(self.decrypt_data(self.encrypt_data("Hello world")))
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


# Run test if script is executed directly
if __name__ == "__main__":
    Cryptography().test()
