import socket
import json
from server.cryptography.cryptography import Cryptography
from server.interface.manager import Manager


# Class for config server and start server
class ConfigServer:
    # Constructor
    def __init__(self):
        # Instance of Cryptography
        self.cryptography = Cryptography()

    # Function for handle get_public_key_server and set_public_key_client
    def initialize_secure_connection(self, command, data, manager: Manager):
        try:
            # If command is get_public_key_server send public key
            if command == "get_public_key_server":
                response = manager.get_public_key_server()
            # If command is set_public_key_client save public key
            elif command == "set_public_key_client":
                response = manager.set_public_key_client(data.get("public_key_client"))
            # If command not found
            else:
                response = {"status": "error", "message": "Unknown command"}
            return response
        except Exception as e:
            error_response = {"status": "error", "message": str(e)}
            return error_response

    # Function for start server
    def start_server(self, manager):
        # Server configuration
        host = "localhost"
        port = 12345
        # Create and configure the server socket
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((host, port))
        server_socket.listen(10)
        print(f"Server in execution {host}:{port}")
        # Loop to accept client connections
        try:
            while True:
                # Accept client connection
                client_socket, addr = server_socket.accept()
                print(f"Client connected {addr}")
                # Loop to receive and send data from the client
                try:
                    # Receive data from the client
                    data = client_socket.recv(4096)
                    if not data:
                        raise ValueError("Empty data received")
                    # Attempt to decode and parse JSON
                    try:
                        request = json.loads(data.decode("utf-8"))
                        command = request.get("command")
                        params = request.get("data")
                    except (UnicodeDecodeError, json.JSONDecodeError):
                        # Handle encrypted data
                        decrypted_data = self.cryptography.decrypt_data_server(data)
                        request = json.loads(decrypted_data)
                        command = request.get("command")
                        params = request.get("data", {})
                    # Handle specific commands
                    if command in ["get_public_key_server", "set_public_key_client"]:
                        response = self.initialize_secure_connection(
                            command, params, manager
                        )
                        client_socket.sendall(json.dumps(response).encode("utf-8"))
                    else:
                        # Handle secure commands
                        response = manager.handle_command(command, params)
                        encrypted_response = self.cryptography.encrypt_data_client(
                            json.dumps(response)
                        )
                        client_socket.sendall(encrypted_response)
                # Handle exceptions
                except Exception as e:
                    # Log the error and send an error response
                    print("Error:", e)
                    error_response = {"status": "error", "message": str(e)}
                    client_socket.sendall(json.dumps(error_response).encode("utf-8"))
                # Handle client disconnection
                finally:
                    # Always close the client socket
                    client_socket.close()
        # Handle KeyboardInterrupt
        except KeyboardInterrupt:
            print("Server shutting down")
        finally:
            # Close the server socket when the server is stopped
            server_socket.close()


# Start server
if __name__ == "__main__":
    # Instance of Manager
    manager = Manager()
    # Instance of ConfigServer
    config_server = ConfigServer()
    # Start server
    config_server.start_server(manager)
