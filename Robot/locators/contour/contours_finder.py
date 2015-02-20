import cv2
import numpy


def find_contours(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    contours = cv2.findContours(gray, cv2.RETR_LIST,
                                cv2.CHAIN_APPROX_SIMPLE)[1]

    # perimeter = cv2.arcLength(contours, True)
    #print(contours)
    #hull = cv2.convexHull(numpy.concatenate(contours))
    #print(hull)
    print()
    return contours
