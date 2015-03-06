import cv2
import numpy

from Robot.configuration.config import Config
from Robot.locators.segmentation.cube_segmentation import CubeSegmentor


class RedCubeSegmentor(CubeSegmentor):

    def __init__(self):
        super().__init__()

        self._lower_hsv_values = Config().get_low_red_hsv_values()
        self._upper_hsv_values = Config().get_high_red_hsv_values()

    def segment_cube(self, img):
        # Convert BGR image to HSV
        img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # define range of blue color in HSV
        lower = numpy.array(self._lower_hsv_values)
        lower_limit = numpy.array([180, self._upper_hsv_values[1],
                                   self._upper_hsv_values[2]])
        upper = numpy.array([0, self._lower_hsv_values[1],
                             self._lower_hsv_values[2]])
        upper_limit = numpy.array(self._upper_hsv_values)

        # Threshold the HSV image to get only red colors
        mask_lower = cv2.inRange(img_hsv, lower, lower_limit)
        mask_upper = cv2.inRange(img_hsv, upper, upper_limit)
        mask = mask_lower + mask_upper

        # Apply erosion + opening
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (10, 10))
        mask = cv2.dilate(cv2.erode(mask, kernel), kernel)

        # Bitwise-AND mask and original image
        extracted_cube = cv2.bitwise_and(img, img, mask=mask)

        return extracted_cube
