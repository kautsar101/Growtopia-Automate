import pyautogui as pg
import time
import tkinter as tk
import keyboard
import threading


start = False
spamming = True
back = True
wrong_enter = False
price = input("enter price:")


while True:
    if keyboard.is_pressed("1") and  keyboard.is_pressed("0"):
        start = True
        break

def spam():
    global price
    global wrong_enter
    global start
    global spamming
    global back

    while True:
        while start:
            if spamming:
                print("spammmmmmmmmmmmmmmmmmmmmm")
                time.sleep(1)
                pg.press("enter")
                time.sleep(0.25)
                pg.write(f"Sell Fuel Pack {price}/1 At `1EXLOD `w(no link)")
                time.sleep(0.25)
                pg.press("enter")
                time.sleep(6.5)

def disconnected():
    print("disc called")
    global spamming
    global start
    while True:
        while start:
            if pg.locateCenterOnScreen("assets/dc.png", region=(171,27,1187,729),
                                                    grayscale=True,
                                                    confidence=0.89) is not None:
                print("disconnected")
                spamming = False
                while True:
                    if pg.locateCenterOnScreen("assets/oops.png",
                                                    region=(171,27,1187,729),
                                                    grayscale=True,
                                                    confidence=0.99) is not None:
                        pg.press("esc")
                        time.sleep(0.75)
                        pg.press("enter")
                    elif pg.locateCenterOnScreen("assets/x.png",
                                                    region=(171,27,1187,729),
                                                    grayscale=True,
                                                    confidence=0.99) is not None :
                        pg.press("esc")
                        time.sleep(0.75)
                        while True :
                            if pg.locateCenterOnScreen("assets/x.png",
                                                    region=(171,27,1187,729),
                                                    grayscale=True,
                                                    confidence=0.99) is None :
                                pg.press("space")
                                break

def stopspam():
    global spamming
    global start
    print("stopspam called")
    while True:
        while start:
            print("check 2 and 9")
            time.sleep(1)
            if keyboard.is_pressed("2") and keyboard.is_pressed("9"):
                spamming = False
                start = False
                print("spamming = false")
        else:
            print("not start")
            time.sleep(1)

def reenter():
    global spamming
    global spamming
    while True:
        while start:
            leaved = pg.locateCenterOnScreen("assets/enterworld.png",
                                                    region=(171,27,1187,729),
                                                    grayscale=True,confidence=0.95)
            if leaved is not None:
                spamming = False
                print("leaveddddddddddddddddddddd")
                time.sleep(1)
                pg.moveTo(936,639)
                pg.click()
                time.sleep(0.1)
                back = True
                while back:
                    print("scan world entered")
                    time.sleep(1)
                    entered = pg.locateCenterOnScreen("assets/enterworld.png",
                                                    region=(171,27,1187,729),
                                                    grayscale=True,
                                                    confidence=0.95) is None
                    if entered :
                        print("enteredddddddddddddddddddddddddddddd")
                        time.sleep(1)
                        while back:
                            pg.keyDown("d")
                            if pg.locateCenterOnScreen("assets/entering.png",
                                                    region=(171,27,1187,729),
                                                    grayscale=True,
                                                    confidence=0.99) is None:
                                time.sleep(2.5)
                                pg.keyUp("d")
                                back = False
                                spamming = True
                                print("gassssss")
        else : 
            print("still In the world")
            time.sleep(1)


spam_thread = threading.Thread(target=spam)
stopspam_thread = threading.Thread(target=stopspam)
reenter_thread = threading.Thread(target=reenter)
disconnected_thread = threading.Thread(target=disconnected)
reenter_thread.start()
spam_thread.start()
stopspam_thread.start()
disconnected_thread.start()













                 