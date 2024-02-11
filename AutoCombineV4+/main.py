import cv2 as cv
import numpy as np
import os
from time import time
from ss import ss
from vision import Vision

# Change the working directory to the folder this script is in.
# Doing this because I'll be putting the files from each video in their own folder on GitHub
# os.chdir(os.path.dirname(os.path.abspath(__file__)))


# initialize the WindowCapture class
wincap = ss('Growtopia')
# initialize the Vision class
for c in ["red","green","yellow","blue","pink"]:
    vision_limestone = Vision(f'assets_2\\droppedP.png')
    loop_time = time()
    while(True):

        # get an updated image of the game
        screenshot = wincap.get_screenshot()
        # display the processed image
        points = vision_limestone.find(screenshot, 0.725, 'rectangles')
        print(points)
        #points = vision_gunsnbottle.find(screenshot, 0.7, 'points')
        # debug the loop rate
        print('FPS {}'.format(1 / (time() - loop_time)))
        loop_time = time()
        # press 'q' with the output window focused to exit.
        # waits 1 ms every loop to process key presses
        if cv.waitKey(1) == ord('q'):
            cv.destroyAllWindows()
            break

print('Done.')