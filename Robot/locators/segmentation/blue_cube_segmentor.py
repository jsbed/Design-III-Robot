from Robot.locators.segmentation.cube_segmentation import CubeSegmentor

import cv2
import numpy as np


class BlueCubeSegmentor(CubeSegmentor):

    def __init__(self):
        self._lower_hsv_values = [70, 140, 49]
        self._upper_hsv_values = [120, 255, 255]

    def extract_cube(self, img):
        # Convert BGR image to HSV
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # define range of blue color in HSV
        lower = np.array(self._lower_hsv_values)
        upper = np.array(self._upper_hsv_values)

        # Threshold the HSV image to get only blue colors
        mask = cv2.inRange(img_hsv, lower, upper)

        # Bitwise-AND mask and original image
        extracted_cube = cv2.bitwise_and(img, img, mask=mask)

        return extracted_cube
