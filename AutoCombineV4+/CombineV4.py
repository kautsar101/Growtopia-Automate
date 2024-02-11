import pyautogui as pg
import time
import cv2
import keyboard
import threading

facing = (233,226)
wrench = (535,670)
wrench_2 = (545,328)

retr_item = (528,378)
retrieve = (565,465)

ut_y = (224,226)
ut_b = (221,149)
ut_p = (303,273)
ut_g = (400,330)
ut_r = (398,255)

chem_ybp = (705,519)
chem_g = (512,513)
chem_m = (805,517)
chem_r = (406,77)
slot4 = (613,519)
slot5 = (718,519)
slot6 = (824,514)
slot7 = (902,522)

drop = (1047,628)
ok = (686,455)
ok_m = (587,450)

inv = (688,599)
close_inv = (682,257)
fav = (228,464)
combine = (224,340)
combine_2 = (220,167)

# RECYCLE RED
wrench_red = (534,324)
ut_r_top = (406,77)
chem_r = (612,528)
recycle = (1049,496)
ok_r = (634,473)
selff = (313,172)
selfff = (678,170)
enter = (436,246) 

storage = (508,173)
deposit = (443,326)
slime = (617,516)
store = (422,426)
deposit2 = (376,251)
shockinator = (506,524)
exit = (301,578)
self_input = (325,343)
self_mid = (698,356)
fuel = (260,648)
add_item = (475,579)
enter_world = (313,244)

fuels = [facing,wrench,
         ut_y,retr_item,retrieve,
         ut_b,retr_item,retrieve,
         ut_p,retr_item,retrieve,
         ut_g,retr_item,retrieve,
         inv,
         chem_ybp,drop,ok,
         chem_ybp,drop,ok,
         chem_ybp,drop,ok,
         close_inv,combine,combine,wrench,
         ut_y,retr_item,retrieve,inv,
         chem_ybp,drop,ok,
         chem_ybp,drop,ok,
         chem_ybp,drop,ok,
         close_inv,combine,combine,wrench,
         ut_y,retr_item,retrieve,
         ut_b,retr_item,retrieve,
         inv,
         chem_ybp,drop,ok,
         chem_ybp,drop,ok,
         chem_ybp,drop,ok,
         close_inv,combine,combine,wrench,
         ut_y,retr_item,retrieve,
         inv,
         chem_ybp,drop,ok,
         chem_ybp,drop,ok,
         chem_ybp,drop,ok,
         close_inv,combine,combine,wrench,
         ut_b,retr_item,retrieve,
         inv,chem_g,drop,ok,
         chem_ybp,drop,ok,
         chem_m,drop,ok_m,
         close_inv,combine,combine,wrench,
         ut_g,retr_item,retrieve,
         inv,chem_g,drop,ok,
         chem_ybp,drop,ok,
         chem_m,drop,ok_m,
         close_inv,combine,combine]

slimes = [
    wrench,
    ut_g,retr_item,retrieve,
    ut_p,retr_item,retrieve,
    inv,
    chem_g,drop,ok,
    slot5,drop,ok,
    slot5,drop,ok,
    close_inv,combine,combine,
    wrench,
    ut_p,retr_item,retrieve,
    ut_b,retr_item,retrieve,
    ut_g,retr_item,retrieve,
    inv,
    slot4,drop,ok,
    slot6,drop,ok,
    slot6,drop,ok,
    close_inv,combine,combine,
    wrench,
    ut_g,retr_item,retrieve,
    inv,
    slot4,drop,ok,
    slot6,drop,ok,
    slot6,drop,ok,
    close_inv,combine,combine,
    wrench,
    ut_g,retr_item,retrieve,
    inv,
    slot4,drop,ok,
    slot6,drop,ok,
    slot6,drop,ok,
    close_inv,combine,combine,
    ]

shockinators = [
    wrench,
    ut_r,retr_item,retrieve,
    ut_g,retr_item,retrieve,
    inv,
    slot4,drop,ok,
    slot4,drop,ok,
    slot6,drop,ok,
    close_inv,combine,combine,wrench,
    ut_g,retr_item,retrieve,
    inv,
    slot5,drop,ok,
    slot5,drop,ok,
    slot7,drop,ok,
    close_inv,combine,combine,wrench,
    ut_g,retr_item,retrieve]

recycle = [
    ut_r,retr_item,retrieve,inv,
    slot6,recycle,ok_r,wrench_red
    ,ut_r_top,retr_item,retrieve,slot6,recycle,ok_r,wrench_red
    ,ut_r_top,retr_item,retrieve,slot6,recycle,ok_r,wrench_red
    ,ut_r_top,retr_item,retrieve,slot6,recycle,ok_r,wrench_red
    ,ut_r_top,retr_item,retrieve,slot6,recycle,ok_r,wrench_red
    ,ut_r_top,retr_item,retrieve]

inputs = [
    storage,deposit,slime,store,
    deposit2,shockinator,store,exit,
    close_inv,self_input,wrench,self_mid,
    fuel,add_item,wrench,self_mid,
]


all = [fuels,slimes,shockinators,recycle,inputs]

def write_200():
    while True:
        if keyboard.is_pressed("alt"):
           pg.write("200")

w200_thrd = threading.Thread(target=write_200)
w200_thrd.start()
for execs in all:
    count = 0
    for x,y in execs :
        while True:
            
            if keyboard.is_pressed("ctrl"):
                pg.click(x,y)
                time.sleep(0.25)
                break
            elif keyboard.is_pressed("shift"):
                pg.click(execs[count-1][0],execs[count-1][1])
                continue
        count += 1

         



