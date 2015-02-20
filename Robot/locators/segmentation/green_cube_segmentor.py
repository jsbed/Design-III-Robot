import cv2

from Robot.configuration.config import Config
from Robot.locators.segmentation.cube_segmentation import CubeSegmentor
import numpy as np


class GreenCubeSegmentor(CubeSegmentor):

    def __init__(self):
        self._lower_hsv_values = Config().get_low_green_hsv_values()
        self._upper_hsv_values = Config().get_high_green_hsv_values()

    def extract_cube(self, img):
        # Convert BGR image to HSV
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # define range of green color in HSV
        lower = np.array(self._lower_hsv_values)
        upper = np.array(self._upper_hsv_values)

        # Threshold the HSV image to get only green colors
        mask = cv2.inRange(img_hsv, lower, upper)

        # Apply erosion + opening
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
        mask = cv2.dilate(cv2.erode(mask, kernel), kernel)

        # Bitwise-AND mask and original image
        extracted_cube = cv2.bitwise_and(img, img, mask=mask)

        return extracted_cube
