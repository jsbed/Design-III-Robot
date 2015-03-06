from numpy import arctan, degrees, cos, sin, pi

from Robot.configuration import config
from Robot.locators.localization import Localization
from Robot.path_finding.point import Point


def compute(close_corner, far_corner):
    robot_radius = config.Config().get_robot_radius()
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

    return Localization(location, degrees(orientation))
