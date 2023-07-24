# Importing the required libraries
from pynput.keyboard import Key, Listener
import pyautogui
import time
import random
import pygame

# Defining the cursor control points
points = [(2957.9609375, 762.46484375), (2041.59375, 752.5703125)]
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

# Function to handle on key release events
def on_release(key):
    # If escape key is pressed, end the listener
    if key == Key.esc:
        return False

# Starting a Listener for keyboard events
listener = Listener(on_press=on_press, on_release=on_release)
listener.start()

# Initializing the pygame window
pygame.init()
win = pygame.display.set_mode((800, 600))

# Main loop that runs until cancel_script is True or pygame window is closed
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
    # Sleep for 3 seconds
    time.sleep(3)

    # Checking for pygame events
    for event in pygame.event.get():
        # If QUIT event found, set cancel_script to True
        if event.type == pygame.QUIT:
            cancel_script = True

    # Update the pygame display
    pygame.display.update()

# Stop the keyboard listener
listener.stop()

# Quit the pygame window
pygame.quit()
