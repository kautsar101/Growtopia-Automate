import pyautogui
import time
import keyboard
import threading
from pynput.mouse import Controller, Button
from pynput.keyboard import Listener, KeyCode
import random


TakeY = [
"time.sleep(2)",    
"pyautogui.click(541, 658)", 
"time.sleep(1)",
"pyautogui.click(217, 316)", 
"time.sleep(2)",
"pyautogui.click(543, 368)", 
"time.sleep(2)",
"pyautogui.click(551, 461)", 
"time.sleep(1.25)",
]

TakeB = [  
"pyautogui.click(541, 658)", 
"time.sleep(1)",
"pyautogui.click(217, 223)", 
"time.sleep(2)",
"pyautogui.click(543, 368)", 
"time.sleep(2)",
"pyautogui.click(551, 461)", 
"time.sleep(1.25)",
"pyautogui.click(541, 658)", 
"time.sleep(1)",
]    

Choice1234 = [
"pyautogui.click(412,247)",
"pyautogui.click(412,310)",
"pyautogui.click(412,379)",
"pyautogui.click(412,446)",
]

random.seed(time.time())
Random1234 = random.choice(Choice1234)

LootG = [
"time.sleep(1)",
"pyautogui.click(541, 658)", 
"time.sleep(1)",
"pyautogui.click(541, 658)", 
"time.sleep(1)",
"pyautogui.click(304, 391)",
"time.sleep(2.5)",
"pyautogui.click(214, 396)",
"time.sleep(2.5)",
"eval(Random1234)",
"time.sleep(1.5)",
"pyautogui.keyDown('left')",
"time.sleep(3)",
"pyautogui.keyUp('left')",
"time.sleep(2)",
"pyautogui.keyDown('right')",
"time.sleep(2)",
"pyautogui.keyUp('right')",
"time.sleep(1)",
"pyautogui.press('esc')",
"time.sleep(1.5)",
"pyautogui.click(678,217)",
"time.sleep(4)",
"pyautogui.click(214, 396)",
"time.sleep(2.5)",
"pyautogui.click (198, 321,)",
"time.sleep(1.25)",
]
    
Combine = [
"time.sleep(1)",
"pyautogui.click(541, 658)", 
"time.sleep(1)",
"pyautogui.click (207, 385)",
"time.sleep(1.75)",
"pyautogui.keyDown ('left')",
"time.sleep(0.5)",
"pyautogui.keyUp ('left')",
"time.sleep(1)",
"pyautogui.click (207, 385)",
"time.sleep(1.75)",
# INVENTORY OPEN
"pyautogui.click (692, 607,)",
"time.sleep(1)",
# DROP CHEM Y
"pyautogui.click (714, 524,)",
"time.sleep(1)",
"pyautogui.click (1058, 620,)",
"time.sleep(1.75)",
"pyautogui.click (674, 448,)",
"time.sleep(2)",
# DROP CHEM B
"pyautogui.click (705, 516,)",
"time.sleep(1)",
"pyautogui.click (1035, 629,)",
"time.sleep(1.75)",
"pyautogui.click (699, 454,)",
"time.sleep(2)",
# DROP CHEM P
"pyautogui.click (704, 505,)",
"time.sleep(1)",
"pyautogui.click (1042, 630,)",
"time.sleep(1.75)",
"pyautogui.click (689, 447,)",
"time.sleep(2)",
# INVENTORY CLOSE
"pyautogui.click (676, 266,)",
"time.sleep(1)",
# PUNCH LAB
"pyautogui.click (207, 385,)",
"time.sleep(1.75)",
"pyautogui.click (207, 385,)",
"time.sleep(1.75)",
# TAKE CHEM M
"pyautogui.keyDown ('left')",
"time.sleep(0.5)",
"pyautogui.keyUp ('left')",
"time.sleep(0.25)",
"pyautogui.keyDown('right')",
"time.sleep(0.5)",
"pyautogui.keyUp('right')",
"time.sleep(0.25)",
"pyautogui.click (198, 321,)",
"time.sleep(1.25)",
]

Combine2 = [
"time.sleep(1)",
"pyautogui.click (207, 385)",
"time.sleep(1.75)",
"pyautogui.keyDown ('left')",
"time.sleep(0.5)",
"pyautogui.keyUp ('left')",
"time.sleep(1)",
"pyautogui.click (207, 385)",
"time.sleep(1.75)",
# INVENTORY OPEN
"pyautogui.click (692, 607,)",
"time.sleep(1)",
# DROP CHEM G
"pyautogui.click (507, 511,)",
"time.sleep(1)",
"pyautogui.click (1058, 620,)",
"time.sleep(1.75)",
"pyautogui.click (674, 448,)",
"time.sleep(2)",
# DROP CHEM B
"pyautogui.click (704, 516,)",
"time.sleep(1)",
"pyautogui.click (1035, 629,)",
"time.sleep(1.75)",
"pyautogui.click (699, 454,)",
"time.sleep(2)",
# DROP CHEM M
"pyautogui.click (806, 520,)",
"time.sleep(1)",
"pyautogui.click (1042, 630,)",
"time.sleep(1.75)",
"pyautogui.click (582, 443,)",
"time.sleep(2)",
# INVENTORY CLOSE
"pyautogui.click (676, 266,)",
"time.sleep(1)",
# PUNCH LAB
"pyautogui.click (207, 385,)",
"time.sleep(1.75)",
"pyautogui.click (207, 385,)",
"time.sleep(1.75)",
# TAKE FUEL
"pyautogui.keyDown ('left')",
"time.sleep(0.5)",
"pyautogui.keyUp ('left')",
"time.sleep(0.25)",
"pyautogui.keyDown('right')",
"time.sleep(0.5)",
"pyautogui.keyUp('right')",
"time.sleep(0.25)",
"pyautogui.click (198, 321,)",
"time.sleep(1.25)",
]



MakeFuelAndM = [TakeY,Combine,TakeY,Combine,TakeB,TakeY,Combine,TakeY,Combine,TakeB,Combine2,LootG,Combine2]
MakeM = [TakeY,Combine,TakeY,Combine,TakeB,TakeY,Combine,TakeY,Combine]
MakeF = [TakeB,Combine2,LootG,Combine2]
Gawian = input("ulah apa:")


if Gawian == ("f") :
    print("5 gasan mulai fuel")
    print("6 gasan tuntung")
    while True:
        if keyboard.is_pressed('5'):
            for a in MakeF :
                for b in a :
                    exec(b)
                    if keyboard.is_pressed('6'):
                        break
                if keyboard.is_pressed('6'):
                    break
            if keyboard.is_pressed('6'):
                print ("=" * 110)
                break
        if keyboard.is_pressed('7'):
            break

elif Gawian == ("m") :
    print("5 gasan mulai mysterious")
    print("6 gasan tuntung")
    while True:
        if keyboard.is_pressed('5'):
            for a in MakeM :
                for b in a :
                    exec(b)
                    if keyboard.is_pressed('6'):
                        break               
                if keyboard.is_pressed('6'):
                    print ("=" * 110)
                    break
            if keyboard.is_pressed('7'):
                break

elif Gawian == ("fm") or ("mf") :
    print("5 gasan mulai fuel dan mysterious")
    print("6 gasan tuntung")
    while True:
        if keyboard.is_pressed('5'):
            for a in MakeFuelAndM :
                for b in a :
                    exec(b)
                    if keyboard.is_pressed('6'):
                        break
                if keyboard.is_pressed('6'):
                    break
            if keyboard.is_pressed('6'):
                print ("=" * 110)
                break
        if keyboard.is_pressed('7'):
            break

else: print("meulah apa ituuuu, tulis bebujur")




print ("-" * 110)