from Robot.locators.segmentation.cube_segmentation import CubeSegmentator

import cv2
import numpy as np


class YellowCubeSegmentator(CubeSegmentator):

    def __init__(self):
        self._lower_hsv_values = [10, 90, 125]
        self._upper_hsv_values = [35, 255, 255]

    def extract_cube(self, img):
        # Convert BGR image to HSV
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # define range of yellow color in HSV
        lower = np.array(self._lower_hsv_values)
        upper = np.array(self._upper_hsv_values)

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(img_hsv, lower, upper)

        # Bitwise-AND mask and original image
        extracted_cube = cv2.bitwise_and(img, img, mask=mask)

        return extracted_cube
