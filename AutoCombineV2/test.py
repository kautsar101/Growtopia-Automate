import pyautogui as pg
import time
import cv2
import numpy as np
import keyboard
import string 
import tkinter as tk

def scan(img):
    while True:
        if pg.locateOnScreen(img, grayscale=False ,confidence=0.90):
            print("PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP")
        else :
            print("00000000000000000000000000000000000")
scan('cancel.png')
# 0.2
# 0.269
# 0.395
349,261,525,333
# world = ['UZNAF','CANVOR','KDPTW','LMIM1','TERMO91','6D1D6','PILCV','BOBDH',
#         'KUGVS','XYXSW','CLIDER1','BEMZ1','LAZYCD','AM5Y','TYALAB','ZL6U',
#         'POCI1','ODSEP','SCIENCZEZET','JKK00']
# start= 'UZNAF'
# patokan = world.index(start)
# print(patokan)

def tap (img,*coor):
    x1=coor[0]
    y1=coor[1]
    x2=coor[2]
    y2=coor[3]
    x3=coor[4]
    y3=coor[5]
    while True :
        if pg.locateOnScreen(img,region=(x1,y1,x2,y2),grayscale=False,confidence=0.7):
            time.sleep(0.75)
            pg.click(x3,y3)
            time.sleep(0.5)
            break
count =0
# 71

def indoor() :
    while True:
        if keyboard.is_pressed('5'):
            if 0 <= count < 5:
                print("exec1")
                pg.keyDown('right')
                time.sleep(0.5)
                pg.keyUp('right')
                time.sleep(0.5)
                pg.click(695,410)
                time.sleep(1.25)
                break
            elif 5 <= count < 10:
                print("exec2")
                if count == 5:
                    time.sleep(0.5)
                    pg.keyDown('right')
                    time.sleep(0.75)
                    pg.keyUp('right')
                    time.sleep(0.5)
                    pg.click(790,420)
                    time.sleep(0.5)
                pg.keyDown('right')
                time.sleep(0.75)
                pg.keyUp('right')
                time.sleep(0.5)
                pg.click(695,410)
                time.sleep(1.25)
                break
            elif 10 <= count < 15:
                print("exec3")
                if count == 10:
                    time.sleep(0.5)
                    pg.keyDown('right')
                    time.sleep(0.75)
                    pg.keyUp('right')
                    time.sleep(0.5)
                    pg.click(790,420)
                    time.sleep(0.5)
                pg.keyDown('right')
                time.sleep(0.75)
                pg.keyUp('right')
                time.sleep(0.5)
                pg.click(695,410)
                time.sleep(1.25)
                break
            elif 15 <= count < 20:
                print("exec4")
                if count == 15:
                    time.sleep(0.5)
                    pg.keyDown('right')
                    time.sleep(1)
                    pg.keyUp('right')
                    time.sleep(0.5)
                    pg.click(790,420)
                    time.sleep(0.5)
                pg.keyDown('right')
                time.sleep(1)
                pg.keyUp('right')
                time.sleep(0.5)
                pg.click(695,410)
                time.sleep(1.25)
                break
        
def gas():
    count =0
    while True:
        indoor()
        count += 1
        print('count=',count)
        continue
    

def click():
    pg.click()

def middle (img):
    while True:
        start= pg.locateCenterOnScreen(img,region=(171,27,1187,729),grayscale=True,confidence=0.8)
        if start is not None:
            pg.moveTo(start)
            click()
            break
        
def collect(img,x1,y1,x2,y2):
    while True :
        time.sleep(1)
        if not pg.locateOnScreen(img,region=(x1,y1,x2,y2),grayscale=True,confidence=0.8):
            pg.keyDown('left')
            time.sleep(0.5)
            pg.keyUp('left')
            pg.keyDown('right')
            time.sleep(0.5)
            pg.keyUp('right')
            time.sleep(0.5)
            break

def trio (img):
    while True:
        if img == ('myst.png'):
            tlrn=0.8
        else:
            tlrn=0.95
        screen = pg.screenshot()
        screencv = cv2.cvtColor(np.array(screen),cv2.COLOR_RGB2BGR)
        target_image = cv2.imread(img)
        result= cv2.matchTemplate(screencv,target_image,cv2.TM_CCOEFF_NORMED)
        min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)
        if max_val >= tlrn :
            pg.click(max_loc)
            time.sleep(1)
            break
    print("wowwwwwwwwww")            
        

# def tap (img,*coor):
#     x1=coor[0]
#     y1=coor[1]
#     x2=coor[2]
#     y2=coor[3]
#     x3=coor[4]
#     y3=coor[5]
#     while True :
#         if pg.locateOnScreen(img,region=(x1,y1,x2,y2),grayscale=False,confidence=0.7):
#             time.sleep(0.75)
#             pg.click(x3,y3)
#             time.sleep(0.5)
#             break

# def scan(img):
#     while True:
#         if pg.locateOnScreen(img,region=(459,469,958,572), grayscale=False ,confidence=0.95):
#             return True
#         else :
#             return False

# while True:
#         if scan('PINK.png') and scan('BLUE.png') and scan('GREEN.png'):
#             print("prercfttttttttttttttttttttttttttttttt")
#             time.sleep(0.5)
#             pg.click(676, 266)
#             time.sleep(0.5)
#             pg.press('esc')
#             time.sleep(0.5)
#             middle('respawn.png')
#             time.sleep(0.5)
#             tap('nol.png',173,264,250,306,207,394)
#             break
#         elif not scan('PINK.png')  or not scan('BLUE.png')  or not scan('GREEN.png') or not scan('GREEN.png'):
#             print("gadaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
#             time.sleep(0.5)
#             pg.keyDown('left')
#             time.sleep(1.5)
#             pg.keyUp('left')
#             time.sleep(1.5)
#             pg.keyDown('right')
#             time.sleep(1.5)
#             pg.keyUp('right')
#             time.sleep(1.5)
#             continue


# def trio (img):
#     while True:
#         screen = pg.screenshot()
#         screencv = cv2.cvtColor(np.array(screen),cv2.COLOR_RGB2BGR)
#         target_image = cv2.imread(img)
#         result= cv2.matchTemplate(screencv,target_image,cv2.TM_CCOEFF_NORMED)
#         min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)
#         if max_val >= 0.95 :
#             pg.click(max_loc)
#             break

# middle('mys.png')
# pg.click(max_loc)

# def middle (img):
#     while True:
#         getpixel(img)
#         start= pg.locateCenterOnScreen(img,region=(171,27,1187,729),grayscale=True,confidence=0.8)
#         if start is not None:
#             pg.moveTo(start)
#             break


# middle('YELL.PNG')

# pg.LOG_SCREENSHOTS
# def scan(img):
#     while True:
#         if pg.locateOnScreen(img,region=(297,406,471,450), grayscale=False ,confidence=0.95):
#             pg.click(676, 266)
#             time.sleep(0.5)
#             pg.keyDown('up')
#             pg.keyUp('up')
#             break
#         else :
#             pg.click(232,425)
#             time.sleep(0.1)
#             pg.click(338,427)
#             time.sleep(0.1)
#             pg.typewrite('chemi')
#             time.sleep(0.1)
#             pg.press('enter')
#             continue

# pg.click(692, 607)
# time.sleep(1)
# scan('chemi.png')

# time.sleep(1)
# pg.keyDown('left')
# time.sleep(1.5)
# pg.keyUp('left')
# time.sleep(1.5)
# pg.keyDown('right')
# time.sleep(1.5)
# pg.keyUp('right')
# time.sleep(1.5)

# def scan(img):
#     while True:
#         if pg.locateOnScreen(img,region=(459,469,958,572), grayscale=False ,confidence=0.95):
#             return True
#         else : 
#             return False
# def click():
#     pg.click()
# def middle (img):
#     while True:
#         start= pg.locateCenterOnScreen(img,region=(171,27,1187,729),grayscale=True,confidence=0.7)
#         if start is not None:
#             pg.moveTo(start)
#             click()
#             break


# while True:
#         if scan('PINK.png') and scan('BLUE.png') and scan('GREEN.png'):
#             pg.press('esc')
#             middle('respawn.png')
#             break
#         elif not(scan('PINK.png') or scan('BLUE.png') or scan('GREEN.png')):
#             print("ajjuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu")
#             pg.keyDown('left')
#             time.sleep(1.5)
#             pg.keyUp('left')
#             time.sleep(1.5)
#             pg.keyDown('right')
#             time.sleep(1.5)
#             pg.keyUp('right')
#             time.sleep(1.5)
#             continue
    