import cv2
import numpy

from Robot.configuration.config import Config
from Robot.cycle.objects.color import Color
from Robot.locators.contour import contours_finder
from Robot.locators.extractors.robot_corner import robot_corner_extractor_factory
from Robot.locators.perspective import perspective_transformation
from Robot.locators.robot_corners.robot_corner import RobotCorner
from Robot.path_finding.point import Point, Point3D


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
    corner_contours = contours_finder.find_extracted_shape_contour(
        robot_corner)

    if len(corner_contours) == 1:
        return _find_corner_position_from_contour(corner_contours, img_cloud)
    elif len(corner_contours) == 2:
        point_a = _find_corner_position_from_contour(corner_contours[0],
                                                     img_cloud)
        point_b = _find_corner_position_from_contour(corner_contours[1],
                                                     img_cloud)

        if color == Color.BLUE:
            # Returns the highest point
            point_to_return = point_a if point_a.z > point_b.z else point_b
        else:
            # Returns the closest point
            point_to_return = point_a if point_a.y < point_b.y else point_b

        # Returns the closest point
        return Point(point_to_return.x, point_to_return.y)

    else:
        raise Exception("Corner not found")


def _find_corner_position_from_contour(contour, img_cloud):
    new_contour = numpy.squeeze(numpy.concatenate(contour))
    moments = cv2.moments(new_contour)
    centroid_x = int(moments['m10'] / moments['m00'])
    centroid_y = int(moments['m01'] / moments['m00'])
    new_point = perspective_transformation.transform(img_cloud[centroid_y,
                                                               centroid_x])

    return Point3D(new_point[0] * 100, new_point[1] * 100 +
                   Config().get_robot_corner_size(), new_point[2])
