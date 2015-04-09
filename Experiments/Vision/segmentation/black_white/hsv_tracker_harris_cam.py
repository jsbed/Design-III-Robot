# -*- coding: utf-8 -*-


import cv2
import os

import numpy as np


DATA_DIRECTORY = "Data-HSV"

if not os.path.exists(DATA_DIRECTORY):
    os.makedirs(DATA_DIRECTORY)

DATA_COUNT = len(os.listdir(DATA_DIRECTORY))


def nothing(x):
    pass

# Create a black image, a window
cv2.namedWindow('mask')
cv2.namedWindow('dst')

# create trackbars for color change
cv2.createTrackbar('Low-H', 'mask', 0, 180, nothing)
cv2.createTrackbar('High-H', 'mask', 0, 180, nothing)
cv2.createTrackbar('Low-S', 'mask', 0, 255, nothing)
cv2.createTrackbar('High-S', 'mask', 0, 255, nothing)
cv2.createTrackbar('Low-V', 'mask', 0, 255, nothing)
cv2.createTrackbar('High-V', 'mask', 0, 255, nothing)

cv2.createTrackbar('block-size', 'dst', 1, 25, nothing)
cv2.createTrackbar('aperture', 'dst', 1, 25, nothing)
cv2.createTrackbar('k-harris', 'dst', 1, 100, nothing)
cv2.createTrackbar('red-dot', 'dst', 1, 100, nothing)

cap = cv2.VideoCapture(1)

while True:
    ret, img_bgr = cap.read()
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

    # (harris)
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    block_size = cv2.getTrackbarPos('block-size', 'dst')
    aperture = cv2.getTrackbarPos('aperture', 'dst')
    k = cv2.getTrackbarPos('k-harris', 'dst') / 100
    red_dot = cv2.getTrackbarPos('red-dot', 'dst') / 100

    dst = cv2.cornerHarris(gray, block_size, int(aperture), k)

    # result is dilated for marking the corners, not important
    dst = cv2.dilate(dst, None)

    # Threshold for an optimal value, it may vary depending on the image.
    new = res.copy()
    new[dst > red_dot * dst.max()] = [0, 0, 255]

    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    cv2.imshow('dst', new)

    cc = cv2.waitKey(10)  # Necessaire pour l'affichage effectif des images

    if cc == 10:  # Touche Enter (save data)
        with open(os.path.join(DATA_DIRECTORY, "data_{}.txt".format(str(DATA_COUNT))), "w") as file:
            file.write(
                ", ".join(map(str, [low_h, low_s, low_v, high_h, high_s, high_v])) + "\n")
            file.write(", ".join(map(str, [block_size, aperture, k, red_dot])))

        print("saved : data_{}.txt".format(str(DATA_COUNT)))
        DATA_COUNT += 1

    if cc == 27:  # Touche Echap quitte
        break

cv2.destroyAllWindows()
