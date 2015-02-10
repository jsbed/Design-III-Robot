# -*- coding: utf-8 -*-

import cv2
import numpy as np
import argparse

LOW_H = 0
LOW_S = 1
LOW_V = 2
HIGH_H = 3
HIGH_S = 4
HIGH_V = 5


parser = argparse.ArgumentParser()
parser.add_argument('data')
parser.add_argument('img')
args = parser.parse_args()


# Load image
img_bgr = cv2.imread(args.img, cv2.IMREAD_COLOR)

# Load data
with open(args.data) as file:
    data = file.readline().split(", ")
    for i in range(len(data)):
        data[i] = int(data[i])
        
print (data)


img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)



# define range of blue color in HSV
lower = np.array([data[LOW_H], data[LOW_S], data[LOW_V]])
upper = np.array([data[HIGH_H], data[HIGH_S], data[HIGH_V]])

# Threshold the HSV image to get only blue colors
img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
mask = cv2.inRange(img_hsv, lower, upper)

# Bitwise-AND mask and original image
#res = cv2.bitwise_and(frame,frame, mask= mask)

cv2.imshow("real", img_bgr);
cv2.imshow('mask',mask)
#cv2.imshow('res',res)	

while True:
    cc = cv2.waitKey(10) # Necessaire pour l'affichage effectif des images
    if cc == 1048603: # Touche Echap quitte
        break

cv2.destroyAllWindows()
