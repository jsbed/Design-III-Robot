import cv2

from Robot.configuration.config import Config
from Robot.cycle.objects.color import Color
from Robot.locators.contour import contours_finder
from Robot.locators.extractors.cube import cube_extractor_factory
from Robot.locators.localization import Localization
from Robot.locators.location_computer import cube_location_computer
from Robot.resources.camera import Camera
from Robot.resources.kinect import Kinect


def find_cube_distance_from_camera(cube_color):
    cube_corners = _find_cube_corners_from_camera(cube_color)

    return cube_location_computer.compute_distance_from_camera(cube_corners)


def find_cube_center_angle_from_camera(cube_color):
    cube_corners = _find_cube_corners_from_camera(cube_color)

    return cube_location_computer.compute_center_angle_from_camera(cube_corners)


def localize_with_kinect(cube_color):
    if Color.is_segmentable(cube_color):
        return _localicalize_with_kinect(cube_color)
    else:
        return Localization(None, None, unknown=True)


def _localicalize_with_kinect(cube_color):
    try:
        img_bgr, img_cloud = Kinect().get_data()
        extractor = cube_extractor_factory.create_cube_extractor(cube_color)
        extracted_cube = extractor.extract_cube(img_bgr)

        return cube_location_computer.compute_localization_for_kinect(
            extracted_cube, img_cloud)
    except:
        return Localization(None, None, unknown=True)


def _find_cube_corners_from_camera(cube_color):
    original_image = Camera().get_data()
    extractor = cube_extractor_factory.create_cube_extractor(cube_color)
    extracted_cube = extractor.extract_cube(original_image)

    return contours_finder.find_cube_corners_contours(extracted_cube)


Config("../../config.ini").load_config()

img = Camera().get_data("ss_42.jpg")
extractor = cube_extractor_factory.create_cube_extractor(Color.YELLOW)
extracted_cube = extractor.extract_cube(img)
corners = contours_finder.find_cube_corners_contours(extracted_cube)

for a in corners:
    cv2.circle(extracted_cube, (a[0], a[1]), 3, (0, 0, 255))

while 1:
    cc = cv2.waitKey(10)

    cv2.imshow("real", extracted_cube)

    if cc == 1048603:
        break
