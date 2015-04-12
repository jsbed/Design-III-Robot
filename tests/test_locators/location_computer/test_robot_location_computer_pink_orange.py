from numpy import arctan, degrees
from unittest.mock import patch, MagicMock, Mock
import unittest

from Robot.cycle.objects.color import Color
from Robot.locators.localization import Localization
from Robot.locators.location_computer import robot_location_computer
from Robot.locators.robot_corners.robot_corner import RobotCorner
from Robot.path_finding.point import Point


@patch("Robot.configuration.config.Config")
class TestRobotLocationComputerPinkOrange(unittest.TestCase):

    ROBOT_RADIUS = 8.5

    EXPECTED_LOCALIZATION_WITH_LEFT_CORNERS_AT_RIGHT = Localization(
        Point(53.5, 61.5), 90 - degrees(arctan(8 / 15)))
    EXPECTED_LOCALIZATION_WITH_RIGHT_CORNERS_AT_RIGHT = Localization(
        Point(53.5, 61.5), 180 - degrees(arctan(8 / 15)))
    EXPECTED_LOCALIZATION_WITH_LEFT_CORNERS_AT_LEFT = Localization(
        Point(46.5, 61.5), degrees(arctan(8 / 15)))
    EXPECTED_LOCALIZATION_WITH_FRONT_CORNERS_AT_LEFT = Localization(
        Point(46.5, 61.5), 90 + degrees(arctan(8 / 15)))
    EXPECTED_LOCALIZATION_WITH_RIGHT_CORNERS_AT_LEFT = Localization(
        Point(46.5, 61.5), 180 + degrees(arctan(8 / 15)))

    def _setup_config_mock(self, mock):
        a_mock = MagicMock()
        a_mock.get_robot_radius = Mock(return_value=self.ROBOT_RADIUS)

        mock.return_value = a_mock

    def test_pink_orange_left_corners_when_robot_at_right(self, config_mock):
        self._setup_config_mock(config_mock)
        close_corner = RobotCorner(Point(50, 50), Color.ORANGE)
        far_corner = RobotCorner(Point(65, 58), Color.PINK)

        actual_localization = robot_location_computer.compute(close_corner,
                                                              far_corner)

        self._assert_localization(
            actual_localization,
            self.EXPECTED_LOCALIZATION_WITH_LEFT_CORNERS_AT_RIGHT)

    def test_pink_orange_right_corners_when_robot_at_right(self, config_mock):
        self._setup_config_mock(config_mock)
        close_corner = RobotCorner(Point(50, 50), Color.PINK)
        far_corner = RobotCorner(Point(42, 65), Color.ORANGE)

        actual_localization = robot_location_computer.compute(close_corner,
                                                              far_corner)

        self._assert_localization(
            actual_localization,
            self.EXPECTED_LOCALIZATION_WITH_RIGHT_CORNERS_AT_RIGHT)

    def test_pink_orange_left_corners_when_robot_at_left(self, config_mock):
        self._setup_config_mock(config_mock)
        close_corner = RobotCorner(Point(50, 50), Color.ORANGE)
        far_corner = RobotCorner(Point(58, 65), Color.PINK)

        actual_localization = robot_location_computer.compute(close_corner,
                                                              far_corner)

        self._assert_localization(
            actual_localization,
            self.EXPECTED_LOCALIZATION_WITH_LEFT_CORNERS_AT_LEFT)

    def test_pink_orange_front_corners_when_robot_at_left(self, config_mock):
        self._setup_config_mock(config_mock)
        close_corner = RobotCorner(Point(50, 50), Color.PINK)
        far_corner = RobotCorner(Point(35, 58), Color.ORANGE)

        actual_localization = robot_location_computer.compute(close_corner,
                                                              far_corner)

        self._assert_localization(
            actual_localization,
            self.EXPECTED_LOCALIZATION_WITH_FRONT_CORNERS_AT_LEFT)

    def test_pink_orange_right_corners_when_robot_at_left(self, config_mock):
        self._setup_config_mock(config_mock)
        close_corner = RobotCorner(Point(35, 58), Color.PINK)
        far_corner = RobotCorner(Point(43, 73), Color.ORANGE)

        actual_localization = robot_location_computer.compute(close_corner,
                                                              far_corner)

        self._assert_localization(
            actual_localization,
            self.EXPECTED_LOCALIZATION_WITH_RIGHT_CORNERS_AT_LEFT)

    def _assert_localization(self, actual_localization, expected_localization):
        self.assertEqual(actual_localization.position,
                         expected_localization.position)
        self.assertAlmostEqual(actual_localization.orientation,
                               expected_localization.orientation,
                               delta=0.001)
