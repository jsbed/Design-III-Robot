from math import tan, radians
from statistics import mean
import cv2
import numpy

from Robot.configuration.config import Config
from Robot.locators.contour import contours_finder
from Robot.locators.localization import Localization
from Robot.locators.perspective import perspective_transformation
from Robot.path_finding.point import Point


CAMERA_FIELD_OF_VIEW_ANGLE = 70


def compute_distance_from_camera(corners):
    cube_size = _find_size_from_camera(corners)
    cube_angle = CAMERA_FIELD_OF_VIEW_ANGLE * \
        cube_size / Config().get_camera_width()

    return Config().get_cube_radius() / tan(radians(cube_angle / 2))


def compute_center_angle_from_camera(corners):
    cube_center = _find_position_from_camera(corners)

    return CAMERA_FIELD_OF_VIEW_ANGLE * cube_center / \
        Config().get_camera_width()


def compute_localization_for_kinect(extracted_cube, img_cloud):
    cube_contour = contours_finder.find_extracted_shape_contour(extracted_cube)
    cube_contour = numpy.squeeze(numpy.concatenate(cube_contour))
    x, y = contours_finder.get_central_pixel_from_contour(cube_contour)

    new_point = perspective_transformation.transform(img_cloud[y, x])

    return Localization(Point(new_point[0] * 100, new_point[1] * 100 +
                              Config().get_cube_radius()), 0)


def _find_position_from_camera(corners):
    mean_x = mean(coord[0] for coord in corners)

    return Config().get_camera_width() / 2 - mean_x


def _find_size_from_camera(corners):
    all_x = [coord[0] for coord in corners]

    return max(all_x) - min(all_x)
