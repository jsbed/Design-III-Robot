# -*- coding: utf-8 -*-

import cv2, os
import numpy as np
import argparse

DATA_DIRECTORY = "Data-HSV" 

if not os.path.exists(DATA_DIRECTORY):
    os.makedirs(DATA_DIRECTORY)

DATA_COUNT = len(os.listdir(DATA_DIRECTORY))


parser = argparse.ArgumentParser()
parser.add_argument('img')
args = parser.parse_args()


img_bgr = cv2.imread(args.img, cv2.IMREAD_COLOR)

def nothing(x):
    pass

# Create a black image, a window
cv2.namedWindow('mask')

# create trackbars for color change
cv2.createTrackbar('Low-H','mask',0,255,nothing)
cv2.createTrackbar('High-H','mask',0,255,nothing)

cv2.imshow("real", img_bgr);

while True:
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    img_gray = (img_gray - 255)
    cv2.imshow('gray', img_gray)

    
    # get current positions of trackers
    low_h = cv2.getTrackbarPos('Low-H','mask')
    high_h = cv2.getTrackbarPos('High-H','mask')
    
    # define range of blue color in HSV
    lower = np.array([low_h])
    upper = np.array([high_h])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(img_gray, lower, upper)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img_bgr,img_bgr, mask= mask)

    cv2.imshow('mask',mask)
    cv2.imshow('res', res)    


    cc = cv2.waitKey(10) # Necessaire pour l'affichage effectif des images
    if cc == 1048586: # Touche Enter (save data)
        print("no ss taken")
        #with open(os.path.join(DATA_DIRECTORY, "data_{}.txt".format(str(DATA_COUNT))), "w") as file:
        #    file.write(", ".join(map(str, [low_h, low_s, low_v, high_h, high_s, high_v])))
        
        #print("saved : data_{}.txt".format(str(DATA_COUNT)))
        #DATA_COUNT += 1

    if cc == 1048603: # Touche Echap quitte
        break

cv2.destroyAllWindows()
