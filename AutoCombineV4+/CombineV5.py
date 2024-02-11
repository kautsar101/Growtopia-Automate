from ss import ss 
import cv2 as cv 
import pyautogui as pg
import numpy as np
from time import time,sleep
import tkinter as tk 
import threading as thd
import win32api
from C5 import actions

gt = ss("Growtopia")
found = False
x,y = 0,0
start = False
doing = ""
doing_alt=""
xy_change = True
strt_2=0
costtime = []
world_count = 0
worlds = ["" ]

def toggle():
    global start
    while True:
        if  win32api.GetKeyState(0x02) < 0:
            start = not(start)
            sleep(0.75)

def action(act,alt=None):
    global x,y,doing,doing_alt
    if act != "confirmer" :
        doing = act
        doing_alt = alt
    if act == "click":
        if alt is not None:
            x,y=alt[0],alt[1]
            doing_alt = (x,y)
        pg.click(gt.offset_x+x,gt.offset_y+y)
    elif act == "left":
        if alt is not None: hold = alt
        else: hold = 0.2
        pg.keyDown("a")
        sleep(0.2)
        pg.keyUp("a")
    elif act == "right":
        if alt is not None: hold = alt
        else: hold = 0.2
        pg.keyDown("d")
        sleep(hold)
        pg.keyUp("d")
    elif act == "write":
        pg.write(alt)
    elif act == "self":
        pg.keyDown("f")
        sleep(0.1)
        pg.keyUp("f")
    elif act == "backspace": pg.press("backspace",presses=5)
    elif act == "breaker" : doing = None
    else: print(f"action : {act} not found")
    
def find(img,tolerance:float,reverse):
    global screenn,found,x,y
    img = cv.imread(img)
    img_w = img.shape[1]
    img_h = img.shape[0]
    matching = cv.matchTemplate(screenn,img,cv.TM_CCOEFF_NORMED)
    locations = np.where(matching >= tolerance)
    locations = list(zip(*locations[::-1]))
    found = len(locations) > 0 
    if found and xy_change:
        top_left= locations[-1]
        bottom_right = top_left[0]+img_w,top_left[1]+img_h
        mid_x = top_left[0] + img_w//2 
        mid_y = top_left[1] + img_h//2
        x = mid_x
        y = mid_y
    if reverse: found = not(found)

def main(steps:list):
    global world_count,strt_2,found,doing_alt,doing,x,y,start,screenn,xy_change,worlds
    for step in steps:
        sleeping = 0.2
        img = f"assets_2\\{step[0]}.png"
        tolerance = step[1]
        revrs = step[2]
        act = step[3]
        if step[4] == "world": alt = f"{worlds[world_count]}0"
        else : alt = step[4]
        print(f"{step[0]} ")
        if any(adj in img for adj in ["oven","storeitems","punched"]) : sleeping = 0.65
        if act == "confirmer" or act == "if": xy_change = False
        else : xy_change = True
        while True:
            if start:
                sleep(sleeping)
                screenn = gt.get_screenshot()
                find(img,tolerance,revrs)
                print(step[0],found)
                if act == "if":
                    if found:
                        print(f"rekursif ",alt)
                        main(alt)
                    break
                if found:
                    print(f"{act}, {alt}")   
                    action(act,alt)
                    strt_2 = time()
                    break
                else:
                    if time() - strt_2 >= 1:
                        print(f"{doing}, {doing_alt} (past) ,{int(time() -strt_2)}")   
                        action(doing,doing_alt)

if __name__ == "__main__":
    thd.Thread(target=toggle).start()
    start_world = int(input("Start :"))
    finish_world = int(input("Finish :"))
    for i in range(start_world,finish_world+1):
        strt = time()
        world_count = i
        main(actions)
        print(f"done:{time()-strt}")
        costtime.append(time()-strt)
    

        print(f"avg : {np.array(costtime)}")
        print(f"avg : {np.mean(costtime)}")
        print(f"avg : {np.median(costtime)}")
    

