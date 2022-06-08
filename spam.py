import pyautogui
import time

time.sleep(0.1)
with open("Texts.txt","r",encoding="utf-8") as f:
    for line in f:
        pyautogui.typewrite(line)
