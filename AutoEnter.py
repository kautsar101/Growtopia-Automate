import pyautogui as pg
import keyboard 
import time
while True:
    if keyboard.is_pressed("1") and keyboard.is_pressed("0"):
        while True:
            if pg.locateCenterOnScreen("assets/enterworld.png",
                                                region=(171,27,1187,729),
                                                grayscale=True,confidence=0.95) is not None:
                time.sleep(1)
                pg.moveTo(936,639)
                pg.click()
                time.sleep(1)
                if pg.locateCenterOnScreen("assets/enterworld.png",
                                                region=(171,27,1187,729),
                                                grayscale=True,confidence=0.95) is None:
                    pg.keyDown("a")
                    time.sleep(1)
                    pg.keyUp("a")
                else:continue
            elif keyboard.is_pressed("2") and keyboard.is_pressed("9"):
                break
print("done")
