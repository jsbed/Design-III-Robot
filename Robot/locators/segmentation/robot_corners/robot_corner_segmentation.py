import cv2
import numpy


class RobotCornerSegmentor():

    def __init__(self):
        self._lower_hsv_values = [0, 0, 0]
        self._upper_hsv_values = [0, 0, 0]

    def set_lower_hsv_values(self, value):
        self._lower_hsv_values = value

    def set_upper_hsv_values(self, value):
        self._upper_hsv_values = value

    def segment_robot_corner(self, img):
        # Apply median blur to extend colors
        img = cv2.medianBlur(img, 11)

        # Convert BGR image to HSV
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # define range of yellow color in HSV
        lower = numpy.array(self._lower_hsv_values)
        upper = numpy.array(self._upper_hsv_values)

        # Threshold the HSV image to get only yellow colors
        mask = cv2.inRange(img_hsv, lower, upper)

        # Apply erosion + opening
        closing_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        mask = cv2.erode(cv2.dilate(mask, closing_kernel), closing_kernel)
        opening_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        mask = cv2.dilate(cv2.erode(mask, opening_kernel), opening_kernel)

        # Bitwise-AND mask and original image
        extracted_corner = cv2.bitwise_and(img, img, mask=mask)

        return extracted_corner
