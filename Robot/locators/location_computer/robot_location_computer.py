'''
Pink________| |________Blue
    |                  |
    |                  |
    |                  |
    |                  |
    |                  |
    |                  |
    |__________________|
Orange                 Pink

Gripper facing upwards is 0 degrees
'''

from numpy import arctan, degrees, cos, sin, pi

from Robot.configuration import config
from Robot.cycle.objects.color import Color
from Robot.locators.localization import Localization
from Robot.path_finding.point import Point


def compute(close_corner, far_corner):
    robot_radius = config.Config().get_robot_radius()

    if ((close_corner.location.x >= far_corner.location.x) and
            (close_corner.color == Color.ORANGE and
             far_corner.color == Color.PINK) or
            (close_corner.color == Color.PINK and
             far_corner.color == Color.BLUE) or
            (1)):
        pass
    else:
        middle_point = Point(close_corner.location.x +
                             (far_corner.location.x -
                              close_corner.location.x) / 2,
                             close_corner.location.y +
                             (far_corner.location.y -
                              close_corner.location.y) / 2)

        orientation = arctan((far_corner.location.y - close_corner.location.y) /
                             (far_corner.location.x - close_corner.location.x))

        location = Point(middle_point.x - robot_radius * cos(pi / 2 - orientation),
                         middle_point.y + robot_radius * sin(pi / 2 - orientation))

        if (middle_point.x < close_corner.location.x):
            orientation *= -1

        exact_orientation = _find_exact_orientation_from_corner_colors(
            orientation, close_corner, far_corner)

    return Localization(location, exact_orientation)


def _find_exact_orientation_from_corner_colors(orientation, close_corner, far_corner):
    if (close_corner.color == Color.ORANGE and far_corner.color == Color.PINK):
        if (close_corner.location.x < far_corner.location.x):
            orientation = pi / 2 - orientation
    elif (close_corner.color == Color.PINK and far_corner.color == Color.BLUE):
        orientation = pi - orientation
    elif (close_corner.color == Color.BLUE and far_corner.color == Color.PINK):
        orientation += pi
    elif (close_corner.color == Color.PINK and far_corner.color == Color.ORANGE):
        if (close_corner.location.x < far_corner.location.x):
            orientation = 2 * pi - orientation
        else:
            orientation += pi / 2

    return degrees(orientation)
