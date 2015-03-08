from Robot.configuration.config import Config
from Robot.game_cycle.objects.color import Color
from Robot.locators.contour import contours_finder
from Robot.locators.robot_corners.robot_corner import RobotCorner
from Robot.locators.segmentation.robot_cornors.robot_corner_segmentation import RobotCornerSegmentor
from Robot.path_finding.point import Point


def locate(img_bgr, img_cloud):
    corners = _extract_robot_corners(img_bgr, img_cloud)

    return RobotCorner(Point(0, 0), Color.NONE), RobotCorner(Point(0, 0),
                                                             Color.NONE)


def _extract_robot_corners(img_bgr, img_cloud):
    blue_corner = _extract_robot_corner_position(
        img_bgr, img_cloud,
        Config().get_robot_low_blue_hsv_values(),
        Config().get_robot_high_blue_hsv_values())

    green_corner = _extract_robot_corner_position(
        img_bgr, img_cloud,
        Config().get_robot_low_green_hsv_values(),
        Config().get_robot_high_green_hsv_values())

    pink_corner = _extract_robot_corner_position(
        img_bgr, img_cloud,
        Config().get_robot_low_pink_hsv_values(),
        Config().get_robot_high_pink_hsv_values())

    corners = [blue_corner + green_corner + pink_corner]


def _extract_robot_corner_position(img_bgr, img_cloud, low_hsv_value, high_hsv_values):
    segmentor = RobotCornerSegmentor()
    segmentor.set_lower_hsv_values(low_hsv_value)
    segmentor.set_upper_hsv_values(high_hsv_values)

    robot_corner = segmentor.segment_robot_corner(img_bgr)
    contour = contours_finder.find_contours(robot_corner)
