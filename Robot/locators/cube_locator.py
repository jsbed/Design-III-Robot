import cv2
import os

from Robot.cycle.objects.color import Color
from Robot.locators.contour import contours_finder
from Robot.locators.corner_dectector import harris_detector_factory
from Robot.locators.extractors.cube import cube_extractor_factory
from Robot.locators.localization import Localization
from Robot.locators.location_computer import cube_location_computer
from Robot.resources.camera import Camera
from Robot.resources.kinect import Kinect


ss_folder_name = "run_screenshots"


def find_cube_distance_from_camera(cube_color):
    cam_img = Camera().get_data()

    try:
        cube_corners = _find_cube_corners_from_camera(cam_img, cube_color)
        distance = cube_location_computer.compute_distance_from_camera(
            cube_corners, cube_color)

        cv2.imwrite(os.path.join(ss_folder_name, str(abs(distance)) +
                                 "_cube_distance.jpg"), cam_img)

        return distance
    except Exception as e:
        cv2.imwrite(os.path.join(ss_folder_name,
                                 "_last_cube_distance_fail.jpg"), cam_img)
        raise Exception("Cube distance not found : ", str(e))


def find_cube_center_angle_from_camera(cube_color):
    cam_img = Camera().get_data()

    try:
        cube_corners = _find_cube_corners_from_camera(cam_img, cube_color)
        angle = cube_location_computer.compute_center_angle_from_camera(
            cube_corners)

        cv2.imwrite(os.path.join(ss_folder_name, str(abs(angle)) +
                                 "_cube_angle.jpg"), cam_img)

        return angle
    except Exception as e:
        cv2.imwrite(os.path.join(ss_folder_name,
                                 "_last_cube_angle_fail.jpg"), cam_img)
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


def _find_cube_corners_from_camera(cam_img, cube_color):
    if Color.is_segmentable(cube_color):
        return _find_cube_corners_for_segmentable_colors(cam_img,
                                                         cube_color)
    else:
        return _find_cube_corners_for_non_segmentable_colors(cam_img,
                                                             cube_color)


def _find_cube_corners_for_segmentable_colors(cam_img, cube_color):
    extractor = cube_extractor_factory.create_cube_extractor(cube_color)
    extracted_cube = extractor.extract_cube(cam_img)

    return contours_finder.find_cube_corners_contours(extracted_cube)


# For White and Black cubes
def _find_cube_corners_for_non_segmentable_colors(cam_img, cube_color):
    corner_dectector = harris_detector_factory.create_detector(cube_color)

    return corner_dectector.detect_corners(cam_img)