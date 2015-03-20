import numpy

from Robot.configuration.config import Config
from Robot.cycle.objects.color import Color
from Robot.locators.contour import contours_finder
from Robot.locators.extractors.robot_corner import robot_corner_extractor_factory
from Robot.locators.perspective import perspective_transformation
from Robot.locators.robot_corners.robot_corner import RobotCorner
from Robot.path_finding.point import Point


def locate(img_bgr, img_cloud):
    corners = []

    try:  # Try extracting a blue corner
        blue_corner = _extract_robot_corner_position(
            img_bgr, img_cloud, Color.BLUE)

        corners.append(RobotCorner(blue_corner, Color.BLUE))
    except:
        pass

    try:  # Try extracting a orange corner
        orange_corner = _extract_robot_corner_position(
            img_bgr, img_cloud, Color.ORANGE)

        corners.append(RobotCorner(orange_corner, Color.ORANGE))
    except:
        pass

    try:  # Try extracting a pink corner
        pink_corner = _extract_robot_corner_position(
            img_bgr, img_cloud, Color.PINK)

        corners.append(RobotCorner(pink_corner, Color.PINK))
    except:
        pass

    corners.sort(key=lambda corner: corner[0][1])

    if len(corners) < 2:
        raise Exception("Not enough robot corners found.")
    else:
        return corners[0], corners[1]


def _extract_robot_corner_position(img_bgr, img_cloud, color):
    extractor = robot_corner_extractor_factory.create_robot_corner_extractor(
        color)

    robot_corner = extractor.extract(img_bgr)
    corner_contour = contours_finder.find_contours(robot_corner)

    if corner_contour:
        new_contour = numpy.squeeze(numpy.concatenate(corner_contour))
        mean_point = numpy.around(numpy.mean(new_contour, axis=0))
        new_point = perspective_transformation.transform(
            img_cloud[mean_point[1], mean_point[0]])

        return Point(new_point[0] * 100, new_point[1] * 100 + Config().
                     get_robot_corner_size())
    else:
        raise Exception("Corner not found")
