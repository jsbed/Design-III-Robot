# -*- coding: utf-8 -*-

import cv2
from math import cos, radians, sin
import numpy
import time


captObj = cv2.VideoCapture(cv2.CAP_OPENNI)
flags, img = captObj.read()
time.sleep(1)

angleY = 21.5

rotateY = numpy.array([[cos(radians(angleY)), 0, sin(radians(angleY))],
                       [0, 1, 0],
                       [-sin(radians(angleY)), 0, cos(radians(angleY))]])

revert_x = numpy.array([[-1, 0, 0],
                        [0, 1, 0],
                        [0, 0, 1]])


virtual_coord = [(299, 407), (277, 563), (274, 313), (292, 134)]

real_data = numpy.float32(
    [[0.31, 0.23], [0.08, 1.50], [1.03, 1.50], [0.80, 0.23]])

translation_mat = numpy.array([0.12, 0.13, -0.54])

perspective_transform = numpy.load("perspective_array.npy")


def MouseEventCallback(event, x, y, flag, data):
    if event == cv2.EVENT_LBUTTONDOWN:
        # print(x)
        # print(y)
        print(y, x)
        transformed = transform((y, x))

        print("real", img_p[y, x])
        print("transformed", transformed)

        newPoint = cv2.perspectiveTransform(
            numpy.float32([[[transformed[0], transformed[2]]]]),
            perspective_transform)

        print("final", newPoint)


# Create a black image, a window
cv2.namedWindow("image")

# bind mouse events
cv2.setMouseCallback("image", MouseEventCallback)


def transform(point):
    revert = numpy.dot(revert_x, img_p[point])
    rotation_transform = numpy.dot(rotateY, revert)
    return rotation_transform + translation_mat


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

    if cc == 27:  # Touche Echap quitte
        break

    elif cc == 10:  # Touche Enter compute GetPerspective
        first_point = transform(virtual_coord[0])
        second_point = transform(virtual_coord[1])
        third_point = transform(virtual_coord[2])
        fourth_point = transform(virtual_coord[3])

        virtual_data = numpy.float32([[first_point[0],
                                       first_point[2]],
                                      [second_point[0],
                                       second_point[2]],
                                      [third_point[0],
                                       third_point[2]],
                                      [fourth_point[0],
                                       fourth_point[2]]])

        numpy.save("perspective_array",
                   cv2.getPerspectiveTransform(virtual_data, real_data))
        print("'perspective_array.npy' saved")
cv2.destroyAllWindows()
