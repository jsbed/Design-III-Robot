# -*- coding: utf-8 -*-

import cv2
import numpy as np
import argparse


parser = argparse.ArgumentParser()
parser.add_argument('img')
parser.add_argument('depth')
args = parser.parse_args()

img_bgr = cv2.imread(args.img, cv2.IMREAD_COLOR)
img_depth = np.load(args.depth)

def nothing(x):
    pass

def MouseEventCallback(event, x, y, flag, data):
    if event == cv2.EVENT_LBUTTONDOWN:        
        #print(x)
        #print(y)
        print(img_depth[y, x])

# Create a black image, a window
cv2.namedWindow("image")

# bind mouse events
cv2.setMouseCallback("image", MouseEventCallback);

cv2.imshow("image", img_bgr);

while True:
    cc = cv2.waitKey(10)
    
    if cc == 1048603: # Touche Echap quitte
        break

cv2.destroyAllWindows()
