import tkinter as tk
import time 
import threading as thrd 
import pyautogui as pg

spam = False

def start():
    print("button start ")
    global spam
    spam = True

def stop():
    print("button stop ")
    global spam
    spam = False

def spamming():
    global spam
    while True:
        if spam:
            print("spam")
            time.sleep(1)
            pg.press("enter")
            time.sleep(0.25)
            pg.write(f"Sell Fuel Pack {price.get()}/1 At `1EXLOD `w(no link)")
            time.sleep(0.25)
            pg.press("enter")
            time.sleep(7.25) 

def disconnected():
    print("disc called")
    dc = True
    global spam
    while True:
        if spam:
            print("dc")
            if pg.locateCenterOnScreen("assets/dc.png", region=(171,27,1187,729),
                                                    grayscale=True,
                                                    confidence=0.89) is not None:
                print("disconnected")
                spam = False
                while dc:
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
                        while dc :
                            if pg.locateCenterOnScreen("assets/x.png",
                                                    region=(171,27,1187,729),
                                                    grayscale=True,
                                                    confidence=0.99) is None :
                                pg.press("space")
                                dc = False
                                spam = True
                                

thrd.Thread(target=spamming).start()
# thrd.Thread(target=disconnected).start()

root = tk.Tk()
root.title("spam")

price = tk.Entry(root,width=20)
price.pack(pady=10)
print(price.get())

start_button = tk.Button(root, text="Start", command=start)
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop", command=stop)
stop_button.pack(pady=5)

root.mainloop()