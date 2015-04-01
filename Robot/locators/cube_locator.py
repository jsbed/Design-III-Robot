import cv2
import numpy
import time

from Robot.configuration.config import Config
from Robot.cycle.objects.color import Color
from Robot.locators.contour import contours_finder
from Robot.locators.extractors.cube import cube_extractor_factory
from Robot.locators.localization import Localization
from Robot.locators.location_computer import cube_location_computer
from Robot.resources.camera import Camera
from Robot.resources.kinect import Kinect


def localize_with_camera(cube_color):
    original_image = Camera().get_data()
    extractor = cube_extractor_factory.create_cube_extractor(cube_color)
    extracted_cube = extractor.extract_cube(original_image)

    corners = contours_finder.find_cube_corners_contours(extracted_cube)
    # TODO : EXTRACT CUBE LOCALIZATION
    cube_location_computer.compute(corners)
    #cv2.imwrite("test.jpg", extracted_cube)

    for a in corners:
        cv2.circle(extracted_cube, (a[0], a[1]), 3, (0, 0, 255))

    cv2.imshow("cube", extracted_cube)
    #cv2.imwrite("with_contour.jpg", extracted_cube)

# Does not work with a White or Black cube


def localize_with_kinect(cube_color):
    try:
        img_bgr, img_cloud = Kinect().get_data()
        cube_extractor = cube_extractor_factory.create_cube_extractor(
            cube_color)
        extracted_cube = cube_extractor.extract_cube(img_bgr)

        return cube_location_computer.compute(extracted_cube, img_cloud)
    except:
        return Localization(None, None, unknown=True)


Config("../../config.ini").load_config()

Camera().start()

time.sleep(1.5)

while 1:
    cc = cv2.waitKey(2)

    if cc == 27:
        break
    else:
        localize_with_camera(Color.YELLOW)

Camera().stop()
