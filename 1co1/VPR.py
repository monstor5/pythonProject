import pytesseract
import cv2
import matplotlib.pyplot as plt
import pyautogui
from PIL import Image
import time

#screen = pyautogui.screenshot('test.png')
image = cv2.imread("test.png")
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\User\AppData\Local\Programs\Tesseract-OCR'
string = pytesseract.image_to_string(image)
print(string)
#while(True):
       #screen = pyautogui.screenshot('test.png')

       # time.sleep(5)
