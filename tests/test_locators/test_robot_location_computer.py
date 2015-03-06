from numpy import arctan, degrees
from unittest.mock import patch, MagicMock, Mock
import unittest

from Robot.game_cycle.objects.color import Color
from Robot.locators.localization import Localization
from Robot.locators.location_computer import robot_location_computer
from Robot.locators.robot_corners.robot_corner import RobotCorner
from Robot.path_finding.point import Point


ROBOT_RADIUS = 8.5

EXPECTED_LOCALIZATION_WHEN_ROBOT_IS_AT_LEFT = Localization(
    Point(53.5, 61.5), degrees(arctan(8 / 15)))

EXPECTED_LOCALIZATION_WHEN_ROBOT_IS_AT_RIGHT = Localization(
    Point(46.5, 61.5), degrees(arctan(8 / 15)))


@patch("Robot.configuration.config.Config")
class TestRobotLocationComputer(unittest.TestCase):

    def _setup_config_mock(self, mock):
        a_mock = MagicMock()
        a_mock.get_robot_radius = Mock(return_value=ROBOT_RADIUS)

        mock.return_value = a_mock

    def test_compute_when_robot_is_at_left(self, config_mock):
        close_corner = RobotCorner(Point(50, 50), Color.NONE)
        far_corner = RobotCorner(Point(65, 58), Color.NONE)
        self._setup_config_mock(config_mock)

        actual_localization = robot_location_computer.compute(close_corner,
                                                              far_corner)

        self.assert_localization_equal(
            actual_localization, EXPECTED_LOCALIZATION_WHEN_ROBOT_IS_AT_LEFT)

    def test_compute_when_robot_is_at_right(self, config_mock):
        close_corner = RobotCorner(Point(50, 50), Color.NONE)
        far_corner = RobotCorner(Point(35, 58), Color.NONE)
        self._setup_config_mock(config_mock)

        actual_localization = robot_location_computer.compute(close_corner,
                                                              far_corner)

        self.assert_localization_equal(
            actual_localization, EXPECTED_LOCALIZATION_WHEN_ROBOT_IS_AT_RIGHT)

    def assert_localization_equal(self, actual_localization,
                                  expected_localization):
        self.assertEqual(actual_localization.position.x,
                         expected_localization.position.x)
        self.assertEqual(actual_localization.position.y,
                         expected_localization.position.y)
        self.assertEqual(actual_localization.orientation,
                         expected_localization.orientation)
