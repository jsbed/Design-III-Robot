import cv2

from Robot.cycle.objects.color import Color
from Robot.locators.contour import contours_finder
from Robot.locators.extractors.cube import cube_extractor_factory
from Robot.locators.localization import Localization
from Robot.locators.location_computer import cube_location_computer
from Robot.resources.camera import Camera
from Robot.resources.kinect import Kinect


def find_cube_distance_from_camera(cube_color):
    try:
        cube_corners = _find_cube_corners_from_camera(cube_color)

        return cube_location_computer.compute_distance_from_camera(cube_corners)
    except Exception as e:
        raise Exception("Cube distance not found : ", str(e))


def find_cube_center_angle_from_camera(cube_color):
    try:
        cube_corners = _find_cube_corners_from_camera(cube_color)

        return cube_location_computer.compute_center_angle_from_camera(cube_corners)
    except Exception as e:
        raise Exception("Cube center angle not found : ", str(e))


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
    cv2.imwrite("last_cube_img.jpg")
    extractor = cube_extractor_factory.create_cube_extractor(cube_color)
    extracted_cube = extractor.extract_cube(original_image)

    return contours_finder.find_cube_corners_contours(extracted_cube)
