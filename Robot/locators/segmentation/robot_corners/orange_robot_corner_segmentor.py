import cv2
import numpy

from Robot.configuration.config import Config
from Robot.locators.segmentation.robot_corners.robot_corner_segmentation import RobotCornerSegmentor


class OrangeRobotCornerSegmentor(RobotCornerSegmentor):

    def __init__(self):
        super().__init__()

        self.set_lower_hsv_values(Config().get_robot_low_orange_hsv_values())
        self.set_upper_hsv_values(Config().get_robot_high_orange_hsv_values())

    def segment_robot_corner(self, img):
        # Apply median blur to extend colors
        img = cv2.medianBlur(img, 11)

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

        # Apply closing and opening
        closing_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        mask = cv2.erode(cv2.dilate(mask, closing_kernel), closing_kernel)
        opening_kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
        mask = cv2.dilate(cv2.erode(mask, opening_kernel), opening_kernel)

        # Bitwise-AND mask and original image
        extracted_corner = cv2.bitwise_and(img, img, mask=mask)

        return extracted_corner
