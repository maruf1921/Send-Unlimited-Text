import pyautogui
import time

for i in range(5):
    time.sleep(2)
    pyautogui.typewrite("Edit here what you want to write")
    pyautogui.press("enter")