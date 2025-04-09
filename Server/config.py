# Server Configuration (C2 Server)
HOST = "0.0.0.0"  # Bind to all available network interfaces (for external access, use your public IP)
PORT = 9999       # Port to listen on (ensure this port is open on firewall)
BUFFER_SIZE = 4096  # Size of the buffer for receiving data

# Logging Configuration
LOG_FILE = "server_activity.log"  # Log file where the server's activity will be stored
