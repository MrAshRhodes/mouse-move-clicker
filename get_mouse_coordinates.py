import pyautogui  # import the pyautogui module
import time  # import the time module

while True:  # enter an infinite loop
    time.sleep(1)  # pause the execution for 1 second
    print(pyautogui.position())  # print the current position of the mouse cursor