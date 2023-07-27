# Importing the required libraries
from pynput.keyboard import Key, Listener
import pyautogui
import time
import random

# Defining the cursor control points
points = [(2994.80859375, 642.9765625), (1851.9609375, 708.765625)]
# Boolean flag to cancel the script if needed
cancel_script = False
# Combination of keys to cancel the script
cancel_combination = {Key.cmd, Key.alt, Key.ctrl}

# Function to handle on key press events
def on_press(key):
    global cancel_script
    try:
        # If the key is part of cancel_combination, cancel the script
        if key in cancel_combination:
            cancel_script = True
    except AttributeError:
        # Ignoring any attribute errors
        pass
    # If escape key is pressed, end the listener
    if key == Key.esc:
        return False

# Starting a Listener for keyboard events
listener = Listener(on_press=on_press)
listener.start()

# Main loop that runs until cancel_script is True
while True:
    # If cancel_script is True, break the loop
    if cancel_script:
        break
    # Choose a random point for the cursor to move to
    point = random.choice(points)
    # Add randomness to the points within a 50 pixel radius
    point = (point[0] + random.randint(-50, 50), point[1] + random.randint(-50, 50))
    pyautogui.moveTo(point)
    pyautogui.click()
    # Sleep for a random time between 3 and 7 seconds
    time.sleep(random.uniform(3, 7))

# Stop the keyboard listener
listener.stop()