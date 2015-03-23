# -*- coding: utf-8 -*-

import argparse
import cv2
import os
import time

import numpy as np


DATA_DIRECTORY = "Data-HSV"

if not os.path.exists(DATA_DIRECTORY):
    os.makedirs(DATA_DIRECTORY)

DATA_COUNT = len(os.listdir(DATA_DIRECTORY))

parser = argparse.ArgumentParser()
parser.add_argument("low_h")
parser.add_argument("low_s")
parser.add_argument("low_v")
parser.add_argument("high_h")
parser.add_argument("high_s")
parser.add_argument("high_v")
args = parser.parse_args()


def nothing(x):
    pass

# Create a black image, a window
cv2.namedWindow('mask')

# create trackbars for color change
cv2.createTrackbar('Low-H', 'mask', 0, 180, nothing)
cv2.createTrackbar('High-H', 'mask', 0, 180, nothing)
cv2.createTrackbar('Low-S', 'mask', 0, 255, nothing)
cv2.createTrackbar('High-S', 'mask', 0, 255, nothing)
cv2.createTrackbar('Low-V', 'mask', 0, 255, nothing)
cv2.createTrackbar('High-V', 'mask', 0, 255, nothing)

if (args.data):
    # Load data
    with open(args.data) as file:
        data = file.readline().split(", ")
        for i in range(len(data)):
            data[i] = int(data[i])

    cv2.setTrackbarPos('Low-H', 'mask', args.low_h)
    cv2.setTrackbarPos('High-H', 'mask', args.low_s)
    cv2.setTrackbarPos('Low-S', 'mask', args.low_v)
    cv2.setTrackbarPos('High-S', 'mask', args.high_h)
    cv2.setTrackbarPos('Low-V', 'mask', args.high_s)
    cv2.setTrackbarPos('High-V', 'mask', args.high_v)

captObj = cv2.VideoCapture(cv2.CAP_OPENNI)
flags, img_bgr = captObj.read()
time.sleep(1)

while True:
        # On recupere une nouvelle image
    captObj.grab()

    # On va chercher les infos
    flags_i, img_bgr = captObj.retrieve(None, cv2.CAP_OPENNI_BGR_IMAGE)
    flags_p, img_p = captObj.retrieve(None, cv2.CAP_OPENNI_DEPTH_MAP)

    # Pas d'image, peut se produire si on boucle trop vite
    if not flags_i or not flags_p:
        continue

    img_hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)

    # get current positions of trackers
    low_h = cv2.getTrackbarPos('Low-H', 'mask')
    high_h = cv2.getTrackbarPos('High-H', 'mask')
    low_s = cv2.getTrackbarPos('Low-S', 'mask')
    high_s = cv2.getTrackbarPos('High-S', 'mask')
    low_v = cv2.getTrackbarPos('Low-V', 'mask')
    high_v = cv2.getTrackbarPos('High-V', 'mask')

    # define range of blue color in HSV
    lower = np.array([low_h, low_s, low_v])
    upper = np.array([high_h, high_s, high_v])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(img_hsv, lower, upper)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(img_bgr, img_bgr, mask=mask)

    cv2.imshow('mask', mask)
    cv2.imshow('res', res)

    cc = cv2.waitKey(10)  # Necessaire pour l'affichage effectif des images
    if cc == 1048586:  # Touche Enter (save data)
        with open(os.path.join(DATA_DIRECTORY, "data_{}.txt".format(str(DATA_COUNT))), "w") as file:
            file.write(
                ", ".join(map(str, [low_h, low_s, low_v, high_h, high_s, high_v])))

        print("saved : data_{}.txt".format(str(DATA_COUNT)))
        DATA_COUNT += 1

    if cc == 1048603:  # Touche Echap quitte
        break

cv2.destroyAllWindows()
