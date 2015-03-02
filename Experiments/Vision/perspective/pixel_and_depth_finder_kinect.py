# -*- coding: utf-8 -*-

import cv2
from math import cos, radians, sin
import numpy
import time


captObj = cv2.VideoCapture(cv2.CAP_OPENNI)
flags, img = captObj.read()
time.sleep(1)

angleZ = -24
angleX = -24
angleY = -24.5

rotateZ = numpy.array([[cos(radians(angleZ)), -sin(radians(angleZ)), 0],
                       [sin(radians(angleZ)), cos(radians(angleZ)), 0],
                       [0, 0, 1]])

rotateY = numpy.array([[cos(radians(angleY)), 0, sin(radians(angleY))],
                       [0, 1, 0],
                       [-sin(radians(angleY)), 0, cos(radians(angleY))]])

rotateX = numpy.array([[1, 0, 0],
                       [0, cos(radians(angleX)), -sin(radians(angleX))],
                       [0, sin(radians(angleX)), cos(radians(angleX))]])

revert_x = numpy.array([[-1, 0, 0],
                        [0, 1, 0],
                        [0, 0, 1]])


def MouseEventCallback(event, x, y, flag, data):
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(x)
        # print(y)
        rotation_transform = numpy.dot(rotateY, img_p[y, x])
        point = numpy.dot(revert_x, rotation_transform)
        translate = point + numpy.array([0, 0, - 0.56])

        print("real", img_p[y, x])
        print("transform", point)
        print("translate", translate)


# Create a black image, a window
cv2.namedWindow("image")

# bind mouse events
cv2.setMouseCallback("image", MouseEventCallback)

while True:
    # On recupere une nouvelle image
    captObj.grab()

    # On va chercher les infos
    flags_i, img_i = captObj.retrieve(None, cv2.CAP_OPENNI_BGR_IMAGE)
    flags_p, img_p = captObj.retrieve(None, cv2.CAP_OPENNI_POINT_CLOUD_MAP)

    # Pas d'image, peut se produire si on boucle trop vite
    if not flags_i or not flags_p:
        continue

    cv2.imshow("image", img_i)
    cv2.imshow("cloud", img_p)

    cc = cv2.waitKey(10)

    if cc == 1048603:  # Touche Echap quitte
        break

cv2.destroyAllWindows()
