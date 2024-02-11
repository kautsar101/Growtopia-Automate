import pyautogui as pg 
import time
import keyboard
import pandas as pd

start = time.time()
df = pd.read_csv("costtime.csv",header=None,delimiter="\t")
print(df.set_axis(df[0]))
    