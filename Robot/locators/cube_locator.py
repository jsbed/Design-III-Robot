import cv2
import numpy

from Robot.color import Color
from Robot.configuration.config import Config
from Robot.cube import Cube
from Robot.locators.contour import contours_finder
from Robot.locators.segmentation import cube_segmentor_factory
from Robot.resources import Camera


def localize(cube):
    original_image = Camera.get_data()
    segmentor = cube_segmentor_factory.create_cube_segmentor(cube.get_color())
    extracted_cube = segmentor.extract_cube(original_image)

    contours = contours_finder.find_contours(extracted_cube)
    point_a, point_b = _extract_orientation_line_from_contours(contours)
    #point_a, point_b = None, None

    # TODO : EXTRACT CUBE LOCALIZATION
    showImg(original_image, contours, point_a, point_b)


def _extract_orientation_line_from_contours(contours):
    contours = numpy.squeeze(numpy.concatenate(contours))

    # Lowest Y point
    #print(contours)
    max_y_index = numpy.argmax(contours, axis=0)[1]
    point_a = contours[max_y_index]

    # Replace Lower point for dump values
    contours = numpy.copy(contours)
    contours[max_y_index][0] = -1
    contours[max_y_index][1] = -1

    # 2nd Lowest Y point
    max_y_index = numpy.argmax(contours, axis=0)[1]
    point_b = contours[max_y_index]

    return (point_a[0], point_a[1]), (point_b[0], point_b[1])


def showImg(img, contours, point_a, point_b):
    while True:
        new = img.copy()
        cv2.drawContours(new, contours, -1, (0, 255, 0), 3)
        #cv2.drawContours(new, cv2.convexHull(numpy.concatenate(contours)), -1, (0, 255, 0), 3)
        cv2.line(new, point_a, point_b, (0, 0, 255), 5)

        cv2.imshow("yolo", new)

        c = cv2.waitKey()

        if c == 1048608:  # SPACE
            break

    cv2.destroyAllWindows()

Config().loadConfig()
localize(Cube(Color.GREEN, None, None, None))
