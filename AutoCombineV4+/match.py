import cv2 as cv
import numpy as np
import pyautogui as pg
from ss import ss
# import os



wincap = ss('Growtopia')
needle_img = cv.imread("assets\\bluechem.png")
threshold = 0.01

while True:
    haystack_img = wincap.get_screenshot()
    result = cv.matchTemplate(haystack_img, needle_img, cv.TM_CCOEFF_NORMED)
    locations = np.where(result <= threshold)
    locations = list(zip(*locations[::-1]))

    if locations:
        print('Found needle.')
        needle_w = needle_img.shape[1]
        needle_h = needle_img.shape[0]
        green_clr = (0, 255, 0)
        blue_clr = (255,0,0)
        red_clr = (0,0,255)
        line_type = cv.LINE_4
        
        # Loop over all the locations and draw their rectangle
        for loc in locations:
            # Determine the box positions
            top_left = loc
            bottom_right = (top_left[0] + needle_w, top_left[1] + needle_h)
            middle = loc[0] + needle_w/2, loc[1] + needle_h/2

            # Draw the box
            cv.rectangle(haystack_img, top_left, bottom_right, green_clr, line_type)
            cv.circle(haystack_img,(int(middle[0]),int(middle[1])),7,(blue_clr),-1)
            cv.line(haystack_img,(loc[0]+needle_w//2,loc[1]),(loc[0]+needle_w//2,loc[1]+needle_h),red_clr,2,line_type,0)
            cv.line(haystack_img,(loc[0],loc[1]+needle_h//2),(loc[0]+needle_w,loc[1]+needle_h//2),red_clr,2,line_type,0)
        
    cv.imshow('Matches', haystack_img)
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
    

