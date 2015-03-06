import cv2
import numpy

from Robot.configuration.config import Config
from Robot.game_cycle.objects.color import Color
from Robot.game_cycle.objects.cube import Cube
from Robot.locators.contour import contours_finder
from Robot.locators.extractors import cube_extractor_factory
from Robot.resources import Camera


def localize(cube):
    original_image = Camera.get_data()
    extractor = cube_extractor_factory.create_cube_extractor(cube.get_color())
    extracted_cube = extractor.extract_cube(original_image)

    contours = contours_finder.find_contours(extracted_cube)
    #point_a, point_b = _extract_orientation_line_from_contours(contours)
    point_a, point_b = None, None

    # TODO : EXTRACT CUBE LOCALIZATION
    showImg(extracted_cube, contours, point_a, point_b)


def _extract_orientation_line_from_contours(contours):
    # Reduce contours points with approxPolyDP
    contours = numpy.squeeze(numpy.concatenate(contours))
    epsilon = 0.05 * cv2.arcLength(contours, True)
    approx = numpy.squeeze(cv2.approxPolyDP(contours, epsilon, True))
    #contours = numpy.squeeze(numpy.concatenate(contours))

    # Lowest Y point
    max_y_index = numpy.argmax(approx, axis=0)[1]
    point_a = approx[max_y_index]

    threshold = 0.01
    point_b = point_a
    min_slope = float("inf")
    max_distance = float("-inf")
    print(point_a)
    print()
    for i in range(len(approx)):
        distance = numpy.linalg.norm(approx[i] - point_a)
        delta_x = approx[i][0] - point_a[0]
        delta_y = approx[i][1] - point_a[1]

        if delta_x == 0:
            continue

        slope = abs(delta_y / delta_x)
        print(approx[i])
        print(distance)
        print(slope)

        if (slope <= min_slope - threshold and distance > 20):
            print("new min:", slope)
            point_b = approx[i]
            min_slope = slope
            max_distance = distance

        print()

    return (point_a[0], point_a[1]), (point_b[0], point_b[1])


def showImg(img, contours, point_a, point_b):
    #counter = 0
    new = img.copy()
    #cv2.drawContours(new, contours, -1, (0, 255, 0), 3)
    #contours = numpy.squeeze(numpy.concatenate(contours))
    #epsilon = 0.05 * cv2.arcLength(contours, True)
    #approx = cv2.approxPolyDP(contours, epsilon, True)
    #cv2.drawContours(new, approx, -1, (0, 255, 0), 3)
    #cv2.line(new, point_a, point_b, (0, 0, 255), 5)
    #cv2.circle(new, (point_a[0], point_a[1]), 5, (0, 0, 255))
    #contours = numpy.squeeze(numpy.concatenate(contours))
    #approx = numpy.squeeze(approx)
    while True:

        cv2.imshow("yolo", new)

        c = cv2.waitKey()

        if c == 1048603:  # ESC
            break

        if c == 1048608:  # SPACE
            pass
            #point = approx[counter]
            #cv2.circle(new, (point[0], point[1]), 5, (0, 0, 255))
            #counter += 1

    cv2.destroyAllWindows()

Config("../config.ini").load_config()
localize(Cube(Color.WHITE, None))
