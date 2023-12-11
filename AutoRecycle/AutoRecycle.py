import time
import keyboard
import pyautogui as pg
import random
import numpy as np
import cv2

def click():
    time.sleep(0.5)
    pg.click()

def middle (img):
        start = pg.locateCenterOnScreen(img,region=(171,27,1187,729),grayscale=True,confidence=0.8)
        if start is not None:
            pg.moveTo(start)
            time.sleep(0.5)
            click()
            time.sleep(0.5)


while True:
    if keyboard.is_pressed("1"):
        while True :
            middle('RED.png') 
            middle("recycle.png")
            time.sleep(0.5)
            pg.write("200")
            middle('ok.png')
            if keyboard.is_pressed("0"):
                break