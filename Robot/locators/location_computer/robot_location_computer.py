'''
Pink________| |________Blue
    |                  |
    |                  |
    |                  |
    |                  |
    |                  |
    |                  |
    |__________________|
Orange                 Cyan

Gripper facing upwards is 0 degrees
'''

from numpy import arctan, degrees, cos, sin, pi

from Robot.configuration import config
from Robot.cycle.objects.color import Color
from Robot.locators.localization import Localization
from Robot.path_finding.point import Point


def compute(close_corner, far_corner):
    if _corners_are_from_reversed_side(close_corner, far_corner):
        location, orientation = _compute_localization_for_reversed_side(
            close_corner, far_corner)
    else:
        location, orientation = _compute_standard_localization(
            close_corner, far_corner)

    exact_orientation = _find_exact_orientation_from_corner_colors(
        orientation, close_corner, far_corner)

    return Localization(location, exact_orientation)


def _compute_standard_localization(close_corner, far_corner):
    robot_radius = config.Config().get_robot_radius()
    right_corner = min(close_corner.location.x, far_corner.location.x)
    left_corner = max(close_corner.location.x, far_corner.location.x)

    middle_point = Point(right_corner +
                         (left_corner - right_corner) / 2,
                         close_corner.location.y +
                         (far_corner.location.y -
                          close_corner.location.y) / 2)

    orientation = arctan((far_corner.location.y - close_corner.location.y) /
                         (far_corner.location.x - close_corner.location.x))

    location = Point(middle_point.x - robot_radius * sin(orientation),
                     middle_point.y + robot_radius * cos(orientation))

    if (middle_point.x < close_corner.location.x):
        orientation *= -1

    return location, orientation


def _compute_localization_for_reversed_side(close_corner, far_corner):
    robot_radius = config.Config().get_robot_radius()

    middle_point = Point(close_corner.location.x +
                         (far_corner.location.x -
                          close_corner.location.x) / 2,
                         close_corner.location.y +
                         (far_corner.location.y -
                          close_corner.location.y) / 2)

    orientation = arctan((far_corner.location.x - close_corner.location.x) /
                         (far_corner.location.y - close_corner.location.y))

    location = Point(middle_point.x + robot_radius * cos(orientation),
                     middle_point.y - robot_radius * sin(orientation))

    return location, orientation


def _find_exact_orientation_from_corner_colors(orientation, close_corner, far_corner):
    if (close_corner.color == Color.BLUE and far_corner.color == Color.CYAN):
        orientation = 3 * pi / 2 - orientation
    elif (close_corner.color == Color.CYAN and far_corner.color == Color.BLUE):
        if (close_corner.location.x > far_corner.location.x):
            orientation += 3 * pi / 2
    elif (close_corner.color == Color.PINK and far_corner.color == Color.BLUE):
        orientation = pi - orientation
    elif (close_corner.color == Color.BLUE and far_corner.color == Color.PINK):
        if (close_corner.location.x > far_corner.location.x):
            orientation += pi
        else:
            orientation += 3 * pi / 2
    elif (close_corner.color == Color.CYAN and far_corner.color == Color.ORANGE):
        orientation = 2 * pi - orientation
    elif (close_corner.color == Color.ORANGE and far_corner.color == Color.CYAN):
        if (close_corner.location.x < far_corner.location.x):
            orientation += pi / 2
    elif (close_corner.color == Color.ORANGE and far_corner.color == Color.PINK):
        orientation = pi / 2 - orientation
    elif (close_corner.color == Color.PINK and far_corner.color == Color.ORANGE):
        if (close_corner.location.x < far_corner.location.x):
            orientation += pi
        else:
            orientation += pi / 2

    return degrees(orientation)


def _corners_are_from_reversed_side(close_corner, far_corner):
    return ((close_corner.location.x < far_corner.location.x) and
            ((close_corner.color == Color.ORANGE and
              far_corner.color == Color.CYAN) or
             (close_corner.color == Color.CYAN and
                far_corner.color == Color.BLUE) or
             (close_corner.color == Color.BLUE and
                far_corner.color == Color.PINK) or
             (close_corner.color == Color.PINK and
                far_corner.color == Color.ORANGE)))
