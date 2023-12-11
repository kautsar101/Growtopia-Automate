
import time
import keyboard
import pyautogui as pg
import random
import numpy as np
import cv2


rndm = [247,310,379,446]
random.seed(time.time())
ry = random.choice(rndm)

rndm2 = [0.5,1,1.5,2,2.5]
random.seed(time.time())
rt = random.choice(rndm2)

count = 0

def click():
    pg.click()

def middle (img):
    while True:
        start= pg.locateCenterOnScreen(img,region=(171,27,1187,729),grayscale=True,confidence=0.8)
        if start is not None:
            pg.moveTo(start)
            time.sleep(0.5)
            click()
            time.sleep(0.5)
            break
        

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

def tap2 (img,*coor):
    x1=coor[0]
    y1=coor[1]
    x2=coor[2]
    y2=coor[3]
    x3=coor[4]
    y3=coor[5]
    x4=coor[6]
    y4=coor[7]
    while True :
        if pg.locateOnScreen(img,region=(x1,y1,x2,y2),grayscale=False,confidence=0.7):
            time.sleep(0.75)
            pg.click(x3,y3)
            time.sleep(0.5)
            time.sleep(0.75)
            pg.click(x4,y4)
            time.sleep(0.5)
            break
        
def scan(img):
    while True:
        if pg.locateOnScreen(img,region=(459,469,958,572), grayscale=False ,confidence=0.95):
            return True
        else :
            return False

def scan2(img):
    while True:
        if pg.locateOnScreen(img, grayscale=False ,confidence=0.90):
            return True

def need3 (img,x1,y1,x2,y2):
    while True :
        if pg.locateOnScreen(img,region=(x1,y1,x2,y2),grayscale=False,confidence=0.7):
            pg.keyDown('left')
            time.sleep(0.5)
            pg.keyUp('left')
            pg.click(207,385)
            time.sleep(0.5)
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

def indoor():
    while True:
        if 0 <= count < 5:
            pg.keyDown('right')
            time.sleep(0.5)
            pg.keyUp('right')
            time.sleep(0.5)
            pg.click(695,410)
            time.sleep(1.25)
            tap('cancel.png',397,556,548,623,412,247+(66*count))
            break
        elif 5 <= count < 10:
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
            tap('cancel.png',397,556,548,623,412,247+(66*(count-5)))
            break
        elif 10 <= count < 15:
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
            tap('cancel.png',397,556,548,623,412,247+(66*(count-10)))
            break
        elif 15 <= count < 20:
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
            tap('cancel.png',397,556,548,623,412,247+(66*(count-15)))
            break

def chemi (img):
    while True:
        time.sleep(0.5)
        if pg.locateOnScreen(img,region=(297,406,471,450), grayscale=False ,confidence=0.95):
            time.sleep(0.5)
            pg.click(676, 266)
            time.sleep(0.5)
            break
        else :
            time.sleep(0.5)
            pg.click(232,425)
            time.sleep(0.1)
            pg.click(338,427)
            time.sleep(0.1)
            pg.typewrite('chemi')
            time.sleep(0.1)
            pg.press('enter')
            continue

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

def trio2 (img):
    while True:
        screen = pg.screenshot()
        screencv = cv2.cvtColor(np.array(screen),cv2.COLOR_RGB2BGR)
        target_image = cv2.imread(img)
        result= cv2.matchTemplate(screencv,target_image,cv2.TM_CCOEFF_NORMED)
        min_val,max_val,min_loc,max_loc = cv2.minMaxLoc(result)
        if max_val >= 0.9 :
            return True
        else :
            return False

def loot():
    tap('satu.png',257,265,330,303,304,403)
    tap('batu.png',170,519,262,609,217,361)
    tap('cancel.png',397,556,548,623,412,ry)
    tap('bedrock.png',308,484,482,584,692,607)
    while True:
        if scan('GREEN.png'):
            time.sleep(0.5)
            pg.click(676, 266)
            time.sleep(0.5)
            pg.press('esc')
            time.sleep(0.5)
            middle('respawn.png')
            time.sleep(0.5)
            tap('nol.png',173,264,250,306,207,394)
            break
        else:
            time.sleep(rt)
            pg.keyDown('right')
            time.sleep(rt)
            pg.keyUp('right')
            time.sleep(rt)
            pg.keyDown('left')
            time.sleep(rt)
            pg.keyUp('left')
            time.sleep(rt)
            continue

def lootg():
    tap('satu.png',257,265,330,303,304,403)
    tap('batu.png',170,519,262,609,217,361)
    tap('cancel.png',397,556,548,623,412,ry)
    tap('bedrock.png',308,484,482,584,692,607)
    while True:
        if scan('PINK.png') and scan('BLUE.png') and scan('GREEN.png'):
            time.sleep(0.5)
            pg.click(676, 266)
            time.sleep(0.5)
            pg.press('esc')
            time.sleep(0.5)
            middle('respawn.png')
            time.sleep(0.5)
            tap('nol.png',173,264,250,306,207,394)
            break
        elif not scan('PINK.png')  or not scan('BLUE.png')  or not scan('GREEN.png') or not scan('GREEN.png'):
            time.sleep(rt)
            pg.keyDown('right')
            time.sleep(rt)
            pg.keyUp('right')
            time.sleep(rt)
            pg.keyDown('left')
            time.sleep(rt)
            pg.keyUp('left')
            time.sleep(rt)
            continue

def positon():
    tap('mt.png',171,357,242,446,207,385)
    need3('need3.png',175,266,445,310)

def takeY():
    tap2('mt.png',171,357,242,446,541,658,217,316)
    time.sleep(0.5)
    middle('eve.png')
    time.sleep(0.75)
    tap('close.png',315,425,445,491,551,461)

def takeB():
    tap('mt.png',171,357,242,446,217,223)
    time.sleep(0.5)
    middle('eve.png')
    time.sleep(0.75)
    tap('close.png',315,425,445,491,551,461)

def makeM():
    tap('mt.png',171,357,242,446,692,607)
    while True:
        trio('YELL.png')
        middle('drop.png')
        time.sleep(0.4)
        if scan2('cancel.png'):
            if trio2('conY.Png'):
                middle('ok.png')
                break
            else:
                middle('cancel.png')
                time.sleep(0.25)
                continue
    time.sleep(1)
    while True:
        trio('blu.png')
        middle('drop.png')
        time.sleep(0.4)
        if scan2('cancel.png'):
            if trio2('conB.png'):
                middle('ok.png')
                break
            else:
                middle('cancel.png')
                time.sleep(0.25)
                continue
    time.sleep(1)
    while True:
        trio('pin.png')
        middle('drop.png')
        time.sleep(0.4)
        if scan2('cancel.png'):
            if trio2('conP.png'):
                middle('ok.png')
                break
            else:
                middle('cancel.png')
                time.sleep(0.25)
                continue
    time.sleep(0.25)
    tap2('droppedp.png',657,469,744,557,676,266,207,385)
    middle('lab.png')
    collect('colabb.png',171,357,242,446)

def makeF():
    tap('mt.png',171,357,242,446,692,607)
    while True:
        trio('gren.png')
        middle('drop.png')
        time.sleep(0.4)
        if scan2('cancel.png'):
            if trio2('conG.png'):
                middle('ok.png')
                break
            else:
                middle('cancel.png')
                time.sleep(0.25)
                continue
    time.sleep(1)
    while True:
        trio('blu.png')
        middle('drop.png')
        time.sleep(0.4)
        if scan2('cancel.png'):
            if trio2('conB.png'):
                middle('ok.png')
                break
            else:
                middle('cancel.png')
                time.sleep(0.25)
                continue
    time.sleep(1)
    while True:
        trio('myst.png')
        middle('drop.png')
        time.sleep(0.4)
        if scan2('cancel.png'):
            if trio2('conM.png'):
                middle('ok.png')
                break
            else:
                middle('cancel.png')
                time.sleep(0.25)
                continue
    time.sleep(1)
    pg.click(676,266)
    tap('m.png',171,357,242,446,207,385)
    middle('lab.png')
    collect('colabb.png',171,357,242,446)

def putF ():
    tap('mt.png',171,357,242,446,304,403)
    tap('batu.png',170,519,262,609,217,361)
    middle('mafff.png')
    tap2('vending.png',533,232,737,275,531,658,675,402)
    middle('addthem.png')
    tap('added.png',524,239,638,281,531,658)

def general():
    chemi('chemi.png')
    time.sleep(0.25)
    indoor()
    time.sleep(0.25)
    tap('nol.png',173,264,250,306,207, 394)
    time.sleep(0.25)   
    lootg()
    time.sleep(0.25)
    positon()
    time.sleep(0.25)
    takeY()
    time.sleep(0.25)
    makeM()
    time.sleep(0.25)
    positon()
    time.sleep(0.25)
    takeY()
    time.sleep(0.25)
    makeM()
    time.sleep(0.25)
    positon()
    time.sleep(0.25)
    takeY()
    time.sleep(0.25)
    takeB()
    time.sleep(0.25)
    makeM()
    time.sleep(0.25)
    positon()
    time.sleep(0.25)
    takeY()
    time.sleep(0.25)
    makeM()
    time.sleep(0.25)
    positon()
    time.sleep(0.25)
    pg.click(541, 658)
    time.sleep(0.25)
    takeB()
    time.sleep(0.25)
    makeF()
    time.sleep(0.25)
    loot()
    time.sleep(0.25)
    positon()
    time.sleep(0.25)
    makeF()
    time.sleep(0.25)
    putF()
    time.sleep(0.25)

world = ['UZNAF','CANVOR','KDPTW','LMIM1','TERMO91','6D1D6','PILCV','BOBDH',
        'KUGVS','XYXSW','CLIDER1','BEMZ1','LAZYCD','AM5Y','TYALAB','ZL6U',
        'POCI1','ODSEP','SCIENCZEZET','JKK00','end']
start= 'LMIM1'
starc = world.index(start)
patokan = 20 - starc
while True:
    count = starc
    if keyboard.is_pressed('5'):
        while True:
            print("="*30,world[count])
            time.sleep(1)
            pg.click(692, 607)
            general()
            count += 1
            if count < patokan :
                continue
            elif count == patokan :
                break





# 555555555555()