import cv2
import numpy

from Robot.locators.corner_dectector.harris_detector import HarrisDetector


class BlackCubeHarrisDectector(HarrisDetector):

    def detect_corners(self, img):
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = numpy.float32(gray)

        block_size = 15
        aperture = 11
        k = 20 / 100
        red_dot = 30 / 100

        dst = cv2.cornerHarris(gray, block_size, int(aperture), k)

        # result is dilated for marking the corners, not important
        #dst = cv2.dilate(dst, None)

        # Threshold for an optimal value, it may vary depending on the image.
        #new = img.copy()
        #new[dst > red_dot * dst.max()] = [0, 0, 255]
        corners = (dst > red_dot * dst.max()).nonzero()
        corners = [(corners[0][i], corners[1][i])
                   for i in range(corners[0].shape[0])]

        return corners
