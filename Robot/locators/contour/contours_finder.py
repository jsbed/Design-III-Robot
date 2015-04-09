import cv2
import numpy


def find_extracted_shape_contour(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    contours = cv2.findContours(gray, cv2.RETR_LIST,
                                cv2.CHAIN_APPROX_SIMPLE)[1]

    return contours


def find_cube_corners_contours(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    contours = cv2.findContours(gray, cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)[1]

    return _extract_corners_from_contours(contours)


def _extract_corners_from_contours(contours):
    biggest = None
    max_area = 0
    for i in contours:
        area = cv2.contourArea(i)
        if area > 100:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 * peri, True)
            if area > max_area and len(approx) < 8:
                biggest = approx
                max_area = area

    return numpy.squeeze(biggest)
