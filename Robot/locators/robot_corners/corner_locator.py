import cv2
import numpy

from Robot.configuration.config import Config
from Robot.game_cycle.objects.color import Color
from Robot.locators.contour import contours_finder
from Robot.locators.perspective import perspective_transformation
from Robot.locators.robot_corners.robot_corner import RobotCorner
from Robot.locators.segmentation.robot_cornors.robot_corner_segmentation import RobotCornerSegmentor
from Robot.path_finding.point import Point


def locate(img_bgr, img_cloud):
    blue_corner = Point(500, 500)
    green_corner = Point(500, 500)
    pink_corner = Point(500, 500)

    try:  # Try extracting a blue corner
        blue_corner = _extract_robot_corner_position(
            img_bgr, img_cloud,
            Config().get_robot_low_blue_hsv_values(),
            Config().get_robot_high_blue_hsv_values())
    except:
        pass

    try:  # Try extracting a green corner
        green_corner = _extract_robot_corner_position(
            img_bgr, img_cloud,
            Config().get_robot_low_green_hsv_values(),
            Config().get_robot_high_green_hsv_values())
    except:
        pass

    try:  # Try extracting a pink corner
        pink_corner = _extract_robot_corner_position(
            img_bgr, img_cloud,
            Config().get_robot_low_pink_hsv_values(),
            Config().get_robot_high_pink_hsv_values())
    except:
        pass

    corners = sorted([RobotCorner(blue_corner, Color.BLUE),
                      RobotCorner(green_corner, Color.GREEN),
                      RobotCorner(pink_corner, Color.PINK)],
                     key=lambda x: x[0][1])

    return corners[0], corners[1]


def _extract_robot_corner_position(img_bgr, img_cloud, low_hsv_value, high_hsv_values):
    segmentor = RobotCornerSegmentor()
    segmentor.set_lower_hsv_values(low_hsv_value)
    segmentor.set_upper_hsv_values(high_hsv_values)

    robot_corner = segmentor.segment_robot_corner(img_bgr)
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
