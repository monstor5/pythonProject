import pyautogui
import time

while(True):
    screen = pyautogui.screenshot('Test.png')
    print(screen)
    time.sleep(5)

