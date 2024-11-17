import socket
import json
from server.cryptography.cryptography import Cryptography
from server.interface.manager import Manager


# Class for config server and start server
class ConfigServer:
    # Constructor
    def __init__(self):
        self.cryptography = Cryptography()

    # Function for start server
    def start_server(self, manager: Manager):
        # Config server
        host = "localhost"
        port = 12345
        # Create socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))  # Bind the socket to the host and port
        server_socket.listen(10)  # Listen for incoming connections
        print(f"Server in execution {host}:{port}")
        # Handle client requests
        while True:
            # Accept client connection
            client_socket, addr = server_socket.accept()
            print(f"Client connected {addr}")
            # Handle client requests
            try:
                # Handle client requests and send responses
                encrypted_data = client_socket.recv(4096)
                decrypted_data = self.cryptography.decrypt_data_server(encrypted_data)
                # Parse request
                request = json.loads(decrypted_data)
                command = request.get("command")
                params = request.get("data", {})
                # Handle command
                response = manager.handle_command(command, params)
                # Send response
                encrypted_response = self.cryptography.encrypt_data_client(
                    json.dumps(response)
                )
                # Send response 
                client_socket.sendall(encrypted_response)
            # Handle exceptions
            except Exception as e:
                # Handle exceptions
                print("Error:", e)
                error_response = json.dumps({"status": "error", "message": str(e)})
                client_socket.sendall(
                    self.cryptography.encrypt_data_client(error_response)
                )
            # Close client socket
            client_socket.close()


# Start server  
if __name__ == "__main__":
    # Instance of Manager
    manager = Manager()
    # Instance of ConfigServer
    config_server = ConfigServer()
    # Start server
    config_server.start_server(manager)
