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
cv2.createTrackbar('R','mask',0,255,nothing)
cv2.createTrackbar('G','mask',0,255,nothing)
#cv2.createTrackbar('B','image',0,255,nothing)

cv2.imshow("real", img_bgr);

while True:
    img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)
    cv2.imshow('gray', img_gray)

    
    # get current positions of trackers
    r = cv2.getTrackbarPos('R','mask')
    g = cv2.getTrackbarPos('G','mask')
    #b = cv2.getTrackbarPos('B','image')
    
    # define range of blue color in HSV

    ret,gray = cv2.threshold(img_gray, r, g, 0)
    
    gray2 = gray.copy()
    mask = np.zeros(gray.shape,np.uint8)

    cv2.imshow('mask', mask)
    cv2.imshow('new-gray', gray2)


    cc = cv2.waitKey(10) # Necessaire pour l'affichage effectif des images
    if cc == 1048586: # Touche Enter (save data)
        print("no ss taken")
        #with open(os.path.join(DATA_DIRECTORY, "data_{}.txt".format(str(DATA_COUNT))), "w") as file:
            #file.write(", ".join(map(str, [low_h, low_s, low_v, high_h, high_s, high_v])))
        
        #print("saved : data_{}.txt".format(str(DATA_COUNT)))
        #DATA_COUNT += 1

    if cc == 1048603: # Touche Echap quitte
        break

cv2.destroyAllWindows()
