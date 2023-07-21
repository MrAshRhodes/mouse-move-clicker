# Python Mouse Control Scripts

This repository contains two Python scripts that interact with your mouse: `get_mouse_coordinates.py` and `mouse_move.py`. 

## Prerequisites

To run these scripts, you need the following Python packages installed:

- pyautogui
- pynput
- pygame
- time
- random

You can install these dependencies using pip:

```
pip install pyautogui pynput pygame
```

## `get_mouse_coordinates.py`

This script is used to get the current position of the mouse cursor on your screen. It prints the position every second in an infinite loop. 

To stop the script, simply terminate it using your preferred method (e.g., Control-C in the terminal).

Usage:

```bash
python get_mouse_coordinates.py
```

## `mouse_move.py`

This script automatically moves the mouse cursor to specific points on the screen and performs a click action. It also opens a Pygame window and listens for keyboard events. The script can be terminated by pressing a combination of keys or closing the Pygame window.

The points to which the cursor moves are defined in the `points` variable at the top of the script. You can change these coordinates as per your requirements.

The script can be cancelled by pressing the `Command`, `Alt`, and `Control` keys simultaneously. Alternatively, you can terminate the script by closing the Pygame window that opens when the script starts running.

Usage:

```bash
python mouse_move.py
```