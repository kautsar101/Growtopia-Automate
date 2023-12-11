import pyautogui as pg
import keyboard
import time
for i in range (227,400,):
    while True:
        if keyboard.is_pressed("1") and keyboard.is_pressed("2"):
            print(i)
            pg.click(497,278)
            time.sleep(0.5)
            pg.hotkey("backspace")
            time.sleep(0.5)
            pg.write(f":{i}")
            time.sleep(0.5)
            pg.click(511,577)
            break
