import cv2


def find_contours(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    contours = cv2.findContours(gray, cv2.RETR_LIST,
                                cv2.CHAIN_APPROX_SIMPLE)[1]

    return contours
