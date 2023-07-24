from pynput.mouse import Listener, Button
import pyautogui

def on_click(x, y, button, pressed):
    if button == Button.left and pressed:
        print('You clicked at coordinates:', (x,y))

with Listener(on_click=on_click) as listener:
    listener.join()
