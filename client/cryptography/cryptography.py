from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from client.generateKeys.publicKey import PublicKey
from client.generateKeys.privateKey import PrivateKey


# Class for cryptography using PKI and RSA
class Cryptography:
    # Constructor
    def __init__(self):
        # Instance of public key server
        self.public_key_server = PublicKey().get_public_key_server()
        # Instance of public key client
        self.public_key_client = PublicKey().get_public_key_client()
        # Instance of private key client
        self.private_key_client = PrivateKey().get_private_key_client()

    # Function to encrypt data client (handling large data)
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

    # Function to decrypt data client
    def decrypt_data_client(self, data):
        # Decrypt data in chunks
        decrypted_data = b""
        chunk_size = self.private_key_client.key_size // 8
        for i in range(0, len(data), chunk_size):
            chunk = data[i : i + chunk_size]
            decrypted_chunk = self.private_key_client.decrypt(
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

    # Function to encrypt data server (handling large data)
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

    # Function to test
    def test(self):
        # Encrypt data and print result
        print(self.encrypt_data_client("Hello world"))

        # Encrypt data client
        key_test_encrypt_client = self.encrypt_data_client(
            """
-----BEGIN PUBLIC KEY-----
MIIBIjANBgkqhkiG9w0BAQEFAAOCAQ8AMIIBCgKCAQEAvUtse2rp38OXnlXXCzWu
isYXbKYB9dQZ77+t6mwP810x+VxEW3T5tmgctjYfp9yE29y/IfxxGBbl/2EuRAtn
R6jQcBe6c5LJED8MA/ecuEYdJx25F/ejee6gIanM0Mkz8yMJm/pL0AM7FtTZ9BG+
Q2P2DJQgXfYNiOQyFBiQbygceSZNLxnkmJ1PnkpblfO3lElEluc6+SThU96QXLHP
3xZ73VhQQWcR41E00dXgA27Wx0MTGzTn++9V+WSQ8DvC4cqZS+7lg+GcIYr1KGzs
MnMKHCMBOTiJz1ZOUhPRkIRai4UklwyhbuEpsEHJyVSTYb+Zf9auKfTPaGGS5bm5
8QIDAQAB
-----END PUBLIC KEY-----
"""
        )
        print(key_test_encrypt_client)

        # Decrypt data and print result
        print(self.decrypt_data_client(self.encrypt_data_client("Hello world")))

        # Decrypt data client
        key_test_decrypt_client = self.decrypt_data_client(key_test_encrypt_client)
        print(key_test_decrypt_client)

        # Encrypt data and print result
        print(self.encrypt_data_server("Hello world"))


# Run test if script is executed directly
if __name__ == "__main__":
    Cryptography().test()
