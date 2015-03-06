from Robot.game_cycle.objects.color import Color
from Robot.locators.robot_corners.robot_corner import RobotCorner
from Robot.path_finding.point import Point


def locate(img):
    return RobotCorner(Point(0, 0), Color.NONE), RobotCorner(Point(0, 0),
                                                             Color.NONE)
