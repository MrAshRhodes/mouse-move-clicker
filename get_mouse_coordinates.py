# Import necessary libraries
from pynput import mouse, keyboard
import pyautogui

# Define the combination of keys that will cancel the listener
cancel_combination = {keyboard.Key.cmd, keyboard.Key.alt, keyboard.Key.ctrl}

# Define a function that will be called when the mouse is clicked
def on_click(x, y, button, pressed):
    """
    This function is called when the mouse is clicked. If the right mouse button is clicked, it prints the coordinates of the click.
    """
    if button == mouse.Button.right and pressed:
        print('You clicked at coordinates:', (x,y))

# Define a function that will be called when a key is pressed
def on_press(key):
    """
    This function is called when a key is pressed. If the cancel combination is pressed, it stops the listener.
    """
    if key in cancel_combination:
        listener.stop()
        return False

# Create a mouse listener and a keyboard listener
with mouse.Listener(on_click=on_click) as listener:
    with keyboard.Listener(on_press=on_press) as keyboard_listener:
        # Start the listeners
        listener.join()
        keyboard_listener.join()
