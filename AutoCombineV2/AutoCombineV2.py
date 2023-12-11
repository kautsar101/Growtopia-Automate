import pyautogui as pg
import time
import random
import keyboard

def kl(img):
    klik = pg.locateCenterOnScreen(img,grayscale=False,confidence=0.7)
    pg.click(klik)


def sc(x1, y1, x2, y2, template_image_filename,aksi,aksi2=None,aksi3=None,aksi4=None,aksi5=None,aksi6=None,aksi7=None,aksi8=None):
    if pg.locateOnScreen(template_image_filename, region=(x1,y1,x2,y2),grayscale=False,confidence=0.7):
        exec(aksi)
        if aksi2 is not None:
            exec(aksi2)
        if aksi3 is not None:
            exec(aksi3)
        if aksi4 is not None:
            exec(aksi4)
        if aksi5 is not None:
            exec(aksi5)
        if aksi6 is not None:
            exec(aksi6)
        if aksi7 is not None:
            exec(aksi7)
        if aksi8 is not None:
            exec(aksi8)
        
        return True
    

Choice1234 = [
"pg.click(412,247)",
"pg.click(412,310)",
"pg.click(412,379)",
"pg.click(412,446)",
]

random.seed(time.time())
Random1234 = random.choice(Choice1234)

# template
# while True:
#   if sc(,,,,'.png',"time.sleep(1)","pg.click(,)"):break

count = 0
while keyboard.is_pressed('6') == False:

    while True:
        if keyboard.is_pressed('5'):
            pg.click(692, 607)
            time.sleep(1)
            pg.click(232,425)
            time.sleep(1)
            pg.click(338,427)
            time.sleep(1)
            pg.keyDown('backspace')
            time.sleep(1)
            pg.keyUp('backspace')
            pg.typewrite('chemi')
            pg.press('enter')
            time.sleep(1)
            pg.click(676, 266)
            time.sleep(1)
            pg.keyDown('up')
            pg.keyUp('up')
            break

    while True:
        if sc(173,264,250,306,'nol.png',"time.sleep(1)","pg.click(207, 394)"): break
    # ========================= LOOT G ============================ #
    while True:  
        if sc(257,265,330,303,'satu.png',"time.sleep(1)","pg.click(304,403)"): break
    while True:    
        if sc(170,519,262,609,'batu.png',"time.sleep(1.5)","pg.click(217,361)"): break
    while True: 
        if sc(397,556,548,623,'cancel.png',"time.sleep(1.5)","eval(Random1234)"): break
    while True:
        if sc(244,380,279,419,'water.png',"pg.keyDown('left')","time.sleep(3)",
        "pg.keyUp('left')","pg.keyDown('right')","time.sleep(3)","pg.keyUp('right')",
        "pg.press('esc')"): break
    while True:
        if sc(591,186,773,241,'respawn.png',"time.sleep(1)","pg.click(678,217)"): break
    while True:
            if sc(173,264,250,306,'nol.png',"time.sleep(1.5)","pg.click(207, 394)"): break
    while True:  
            if sc(257,265,330,303,'satu.png',"time.sleep(1)","pg.click(207,385)"): break  
    while True:
        if sc(175,266,445,310,'need3.png',"pg.keyDown ('left')",
        "time.sleep(1)","pg.keyUp ('left')","pg.click(207,385)"):break  
    # ========================= LOOT G END ============================= #  

    # =========================== TAKE Y ========================== #
    while True:
        if sc(171,357,242,446,'mt.png',"time.sleep(1)","pg.click(541, 658)",
        "time.sleep(1)","pg.click(217, 316)"):break
    while True:
        if sc(393,282,963,426,'retrievei.png',"time.sleep(1)","pg.click(543, 368)"):break
    while True:
        if sc(483,429,652,492,'retrieve.png',"time.sleep(1)","pg.click(551, 461)"):break       
    # ================================= TAKE Y END ================================== #

    # =========================== MAKE M ============================ #
    while True:
        if sc(171,357,242,446,'mt.png',"time.sleep(1)","pg.click(692, 607)","time.sleep(1.5)",
        "pg.click (714, 524,)","time.sleep(1)","pg.click (1058, 620,)"): break
    while True:
        if sc(645,420,731,486,'ok.png',"time.sleep(1)","pg.click(674, 448)"):break
    while True:
        if sc(657,469,744,557,'droppedy.png',"time.sleep(1)","pg.click(714, 524)",
        "time.sleep(1)","pg.click (1058, 620,)"):break
    while True:
        if sc(645,420,731,486,'ok.png',"time.sleep(1)","pg.click(674, 448)"):break
    while True:
        if sc(657,469,744,557,'droppedb.png',"time.sleep(1)","pg.click(714, 524)",
        "time.sleep(1)","pg.click (1058, 620,)"):break
    while True:
        if sc(645,420,731,486,'ok.png',"time.sleep(1)","pg.click(674, 448)"):break
    while True:
        if sc(657,469,744,557,'droppedp.png',"time.sleep(1)","pg.click(676, 266)",
        "time.sleep(1)","pg.click(207, 385)"):break
    while True:
        if sc(171,357,242,466,'lab.png',"time.sleep(1)","pg.click(207, 385)"):break
    while True:
        if sc(171,357,242,446,'m.png',"time.sleep(1)","pg.keyDown('left')","time.sleep(1)",
        "pg.keyUp('left')","pg.keyDown('right')","time.sleep(1)","pg.keyUp('right')"):break
    # ================================= MAKE M END ===================================== #

    # =============================== POSITIONING ================================= #
    while True:  
            if sc(171,357,242,446,'mt.png',"time.sleep(1)","pg.click(207,385)"): break  
    while True:
        if sc(175,266,445,310,'need3.png',"pg.keyDown ('left')",
        "time.sleep(1)","pg.keyUp ('left')","pg.click(207,385)"):break 
    # =========================== POSITIONING END ================================ #

    # =========================== TAKE Y 2 ========================== #
    while True:
        if sc(171,357,242,446,'mt.png',"time.sleep(1)","pg.click(541, 658)",
        "time.sleep(1)","pg.click(217, 316)"):break
    while True:
        if sc(393,282,963,426,'retrievei.png',"time.sleep(1)","pg.click(543, 368)"):break
    while True:
        if sc(483,429,652,492,'retrieve.png',"time.sleep(1)","pg.click(551, 461)"):break       
    # ================================= TAKE Y END ================================== #

    # =========================== MAKE M 2 ============================ #
    while True:
        if sc(171,357,242,446,'mt.png',"time.sleep(1)","pg.click(692, 607)","time.sleep(1.5)",
        "pg.click (714, 524,)","time.sleep(1)","pg.click (1058, 620,)"): break
    while True:
        if sc(645,420,731,486,'ok.png',"time.sleep(1)","pg.click(674, 448)"):break
    while True:
        if sc(657,469,744,557,'droppedy.png',"time.sleep(1)","pg.click(714, 524)",
        "time.sleep(1)","pg.click (1058, 620,)"):break
    while True:
        if sc(645,420,731,486,'ok.png',"time.sleep(1)","pg.click(674, 448)"):break
    while True:
        if sc(657,469,744,557,'droppedb.png',"time.sleep(1)","pg.click(714, 524)",
        "time.sleep(1)","pg.click (1058, 620,)"):break
    while True:
        if sc(645,420,731,486,'ok.png',"time.sleep(1)","pg.click(674, 448)"):break
    while True:
        if sc(657,469,744,557,'droppedp.png',"time.sleep(1)","pg.click(676, 266)",
        "time.sleep(1)","pg.click(207, 385)"):break
    while True:
        if sc(171,357,242,466,'lab.png',"time.sleep(1)","pg.click(207, 385)"):break
    while True:
        if sc(171,357,242,446,'m.png',"time.sleep(1)","pg.keyDown('left')","time.sleep(1)",
        "pg.keyUp('left')","pg.keyDown('right')","time.sleep(1)","pg.keyUp('right')"):break
    # ================================= MAKE M END ===================================== #

    # =============================== POSITIONING 2 ================================= #
    while True:  
            if sc(171,357,242,446,'mt.png',"time.sleep(1)","pg.click(207,385)"): break  
    while True:
        if sc(175,266,445,310,'need3.png',"pg.keyDown ('left')",
        "time.sleep(1)","pg.keyUp ('left')","pg.click(207,385)"):break 
    # =========================== POSITIONING END ================================ #

    # =========================== TAKE Y 3 ========================== #
    while True:
        if sc(171,357,242,446,'mt.png',"time.sleep(1)","pg.click(541, 658)",
        "time.sleep(1)","pg.click(217, 316)"):break
    while True:
        if sc(393,282,963,426,'retrievei.png',"time.sleep(1)","pg.click(543, 368)"):break
    while True:
        if sc(483,429,652,492,'retrieve.png',"time.sleep(1)","pg.click(551, 461)"):break       
    # ================================= TAKE Y END ================================== #

    # ============================== TAKE B ============================ #
    while True:
        if sc(171,357,242,446,'mt.png',"time.sleep(1)","pg.click(217, 223)"):break
    while True:
        if sc(393,282,963,426,'retrievei.png',"time.sleep(1)","pg.click(543, 368)"):break
    while True:
        if sc(483,429,652,492,'retrieve.png',"time.sleep(1)","pg.click(551, 461)"):break       
    # ================================= TAKE B END ================================== #

    # =========================== MAKE M 3 ============================ #
    while True:
        if sc(171,357,242,446,'mt.png',"time.sleep(1)","pg.click(692, 607)","time.sleep(1.5)",
        "pg.click (714, 524,)","time.sleep(1)","pg.click (1058, 620,)"): break
    while True:
        if sc(645,420,731,486,'ok.png',"time.sleep(1)","pg.click(674, 448)"):break
    while True:
        if sc(657,469,744,557,'droppedy.png',"time.sleep(1)","pg.click(714, 524)",
        "time.sleep(1)","pg.click (1058, 620,)"):break
    while True:
        if sc(645,420,731,486,'ok.png',"time.sleep(1)","pg.click(674, 448)"):break
    while True:
        if sc(657,469,744,557,'droppedb.png',"time.sleep(1)","pg.click(714, 524)",
        "time.sleep(1)","pg.click (1058, 620,)"):break
    while True:
        if sc(645,420,731,486,'ok.png',"time.sleep(1)","pg.click(674, 448)"):break
    while True:
        if sc(657,469,744,557,'droppedp.png',"time.sleep(1)","pg.click(676, 266)",
        "time.sleep(1)","pg.click(207, 385)"):break
    while True:
        if sc(171,357,242,466,'lab.png',"time.sleep(1)","pg.click(207, 385)"):break
    while True:
        if sc(171,357,242,446,'m.png',"time.sleep(1)","pg.keyDown('left')","time.sleep(1)",
        "pg.keyUp('left')","pg.keyDown('right')","time.sleep(1)","pg.keyUp('right')"):break
    # ================================= MAKE M END ===================================== #

    # =============================== POSITIONING 3 ================================= #
    while True:  
            if sc(171,357,242,446,'mt.png',"time.sleep(1)","pg.click(207,385)"): break  
    while True:
        if sc(175,266,445,310,'need3.png',"pg.keyDown ('left')",
        "time.sleep(1)","pg.keyUp ('left')","pg.click(207,385)"):break 
    # =========================== POSITIONING END ================================ #

    # =========================== TAKE Y 4 ========================== #
    while True:
        if sc(171,357,242,446,'mt.png',"time.sleep(1)","pg.click(541, 658)",
        "time.sleep(1)","pg.click(217, 316)"):break
    while True:
        if sc(393,282,963,426,'retrievei.png',"time.sleep(1)","pg.click(543, 368)"):break
    while True:
        if sc(483,429,652,492,'retrieve.png',"time.sleep(1)","pg.click(551, 461)"):break       
    # ================================= TAKE Y END ================================== #

    # =========================== MAKE M 4 ============================ #
    while True:
        if sc(171,357,242,446,'mt.png',"time.sleep(1)","pg.click(692, 607)","time.sleep(1.5)",
        "pg.click (714, 524,)","time.sleep(1)","pg.click (1058, 620,)"): break
    while True:
        if sc(645,420,731,486,'ok.png',"time.sleep(1)","pg.click(674, 448)"):break
    while True:
        if sc(657,469,744,557,'droppedy.png',"time.sleep(1)","pg.click(714, 524)",
        "time.sleep(1)","pg.click (1058, 620,)"):break
    while True:
        if sc(645,420,731,486,'ok.png',"time.sleep(1)","pg.click(674, 448)"):break
    while True:
        if sc(657,469,744,557,'droppedb.png',"time.sleep(1)","pg.click(714, 524)",
        "time.sleep(1)","pg.click (1058, 620,)"):break
    while True:
        if sc(645,420,731,486,'ok.png',"time.sleep(1)","pg.click(674, 448)"):break
    while True:
        if sc(657,469,744,557,'droppedp.png',"time.sleep(1)","pg.click(676, 266)",
        "time.sleep(1)","pg.click(207, 385)"):break
    while True:
        if sc(171,357,242,466,'lab.png',"time.sleep(1)","pg.click(207, 385)"):break
    while True:
        if sc(171,357,242,446,'m.png',"time.sleep(1)","pg.keyDown('left')","time.sleep(1)",
        "pg.keyUp('left')","pg.keyDown('right')","time.sleep(1)","pg.keyUp('right')"):break
    # ================================= MAKE M END ===================================== #

    # =============================== POSITIONING 4 ================================= #
    while True:  
            if sc(171,357,242,446,'mt.png',"time.sleep(1)","pg.click(207,385)",): break  
    while True:
        if sc(175,266,445,310,'need3.png',"pg.keyDown ('left')",
        "time.sleep(1)","pg.keyUp ('left')","pg.click(207,385)"):break 
    # =========================== POSITIONING END ================================ #

    # =========================== TAKE B 2 ========================== #
    while True:
        if sc(171,357,242,446,'mt.png',"time.sleep(1)","pg.click(541, 658)",
        "time.sleep(1)","pg.click(217, 223)"):break
    while True:
        if sc(393,282,963,426,'retrievei.png',"time.sleep(1)","pg.click(543, 368)"):break
    while True:
        if sc(483,429,652,492,'retrieve.png',"time.sleep(1)","pg.click(551, 461)"):break       
    # ================================= TAKE B END ================================== #

    # ============================ MAKE F ================================ #
    while True:
        if sc(171,357,242,446,'mt.png',"time.sleep(1)","pg.click(692, 607)","time.sleep(1.5)",
        "time.sleep(1)","pg.click(507, 511)","time.sleep(1)","pg.click (1058, 620,)"):break
    while True:
        if sc(645,420,731,486,'ok.png',"time.sleep(1)","pg.click(674, 448)"):break
    while True:
        if sc(462,473,550,560,'droppedg.png',"time.sleep(1)","pg.click(704,506)",
        "time.sleep(1)","pg.click (1058, 620,)"):break
    while True:
        if sc(645,420,731,486,'ok.png',"time.sleep(1)","pg.click(674, 448)"):break
    while True:
        if sc(661,471,748,556,'droppedb.png',"time.sleep(1)","pg.click(806, 520)",
        "time.sleep(1)","pg.click (1058, 620)"):break
    while True:
        if sc(550,427,625,485,'ok.png',"time.sleep(1)","pg.click(590, 455)"):break
    while True:
        if sc(171,357,242,446,'m.png',"time.sleep(1)","pg.click(676, 266)",
        "time.sleep(1)","pg.click(207, 385)"):break
    while True:
        if sc(171,357,242,466,'lab.png',"time.sleep(1)","pg.click(207,385)"):break
    while True:
        if sc(171,357,242,446,'fuel.png',"pg.keyDown('left')","time.sleep(1)",
        "pg.keyUp('left')","pg.keyDown('right')","time.sleep(1)","pg.keyUp('right')"):break
    # ================================= MAKE F END ================================= #

    
    # ============================= LOOT G 2 ================================== #
    while True:  
        if sc(257,265,330,303,'satu.png',"time.sleep(1)","pg.click(304,403)"): break
    while True:    
        if sc(170,519,262,609,'batu.png',"time.sleep(1.5)","pg.click(217,361)"): break
    while True: 
        if sc(397,556,548,623,'cancel.png',"time.sleep(1)","eval(Random1234)"): break
    while True:
        if sc(244,380,279,419,'water.png',"pg.keyDown('left')","time.sleep(3)",
        "pg.keyUp('left')","pg.keyDown('right')","time.sleep(3)","pg.keyUp('right')",
        "pg.press('esc')"): break
    while True:
        if sc(591,186,773,241,'respawn.png',"time.sleep(1)","pg.click(678,217)"): break
    while True:
            if sc(173,264,250,306,'nol.png',"time.sleep(1.5)","pg.click(207, 394)"): break
    while True:  
            if sc(257,265,330,303,'satu.png',"time.sleep(1)","pg.click(207,385)"): break  
    while True:
        if sc(175,266,445,310,'need3.png',"pg.keyDown ('left')",
        "time.sleep(1)","pg.keyUp ('left')","pg.click(207,385)"):break  
    # ========================= LOOT G END ============================= # 

    # ============================ MAKE F 2 ================================ #
    while True:
        if sc(171,357,242,446,'mt.png',"time.sleep(1)","pg.click(692, 607)","time.sleep(1.5)",
        "time.sleep(1)","pg.click(507, 511)","time.sleep(1)","pg.click (1058, 620,)"):break
    while True:
        if sc(645,420,731,486,'ok.png',"time.sleep(1)","pg.click(674, 448)"):break
    while True:
        if sc(462,473,550,560,'droppedg.png',"time.sleep(1)","pg.click(704,506)",
        "time.sleep(1)","pg.click (1058, 620,)"):break
    while True:
        if sc(645,420,731,486,'ok.png',"time.sleep(1)","pg.click(674, 448)"):break
    while True:
        if sc(661,471,748,556,'droppedb.png',"time.sleep(1)","pg.click(806, 520)",
        "time.sleep(1)","pg.click (1058, 620,)"):break
    while True:
        if sc(550,427,625,485,'ok.png',"time.sleep(1)","pg.click(590, 455)"):break
    while True:
        if sc(171,357,242,446,'m.png',"time.sleep(1)","pg.click(676, 266)",
        "time.sleep(1)","pg.click(207, 385)"):break
    while True:
        if sc(171,357,242,466,'lab.png',"time.sleep(1)","pg.click(207,385)"):break
    while True:
        if sc(171,357,242,446,'fuel.png',"pg.keyDown('left')","time.sleep(1)",
        "pg.keyUp('left')","pg.keyDown('right')","time.sleep(1)","pg.keyUp('right')"):break
    # ================================= MAKE F END ================================= #

    # ================================== PUT F ====================================== #
    while True:
        if sc(171,357,242,446,'mt.png',"time.sleep(1)","pg.click(304,403)",):break
    while True:    
        if sc(170,519,262,609,'batu.png',"time.sleep(1.5)","pg.click(217,361)"): break
    while True: 
        if sc(397,556,548,623,'cancel.png',"time.sleep(1)","pg.click(417,510)"): break
    
    
    
    patokan = 20
    count += 1
    if count < patokan :
        continue
    elif count == patokan :
        break

print("tuntung"*10)


# 

