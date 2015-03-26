from numpy import arctan, degrees
from unittest.mock import patch, MagicMock, Mock
import unittest

from Robot.cycle.objects.color import Color
from Robot.locators.location_computer import robot_location_computer
from Robot.locators.robot_corners.robot_corner import RobotCorner
from Robot.path_finding.point import Point


ROBOT_RADIUS = 8.5

EXPECTED_POSITION_WHEN_ROBOT_IS_AT_LEFT = Point(53.5, 61.5)
EXPECTED_POSITION_WHEN_ROBOT_IS_AT_RIGHT = Point(46.5, 61.5)

EXPECTED_ORIENTATION_WHEN_ROBOT_IS_AT_LEFT_IN_FIRST_QUADRANT = 90 - \
    degrees(arctan(8 / 15))
EXPECTED_ORIENTATION_WHEN_ROBOT_IS_AT_LEFT_IN_SECOND_QUADRANT = 180 - \
    degrees(arctan(8 / 15))
EXPECTED_ORIENTATION_WHEN_ROBOT_IS_AT_LEFT_IN_THIRD_QUADRANT = 270 - \
    degrees(arctan(8 / 15))
EXPECTED_ORIENTATION_WHEN_ROBOT_IS_AT_LEFT_IN_FOURTH_QUADRANT = 360 - \
    degrees(arctan(8 / 15))
EXPECTED_ORIENTATION_WHEN_ROBOT_IS_AT_RIGHT_IN_FIRST_QUADRANT = degrees(
    arctan(8 / 15))
EXPECTED_ORIENTATION_WHEN_ROBOT_IS_AT_RIGHT_IN_SECOND_QUADRANT = degrees(
    arctan(8 / 15)) + 90
EXPECTED_ORIENTATION_WHEN_ROBOT_IS_AT_RIGHT_IN_THIRD_QUADRANT = degrees(
    arctan(8 / 15)) + 180
EXPECTED_ORIENTATION_WHEN_ROBOT_IS_AT_RIGHT_IN_FOURTH_QUADRANT = degrees(
    arctan(8 / 15)) + 270


@patch("Robot.configuration.config.Config")
class TestRobotLocationComputer(unittest.TestCase):

    def _setup_config_mock(self, mock):
        a_mock = MagicMock()
        a_mock.get_robot_radius = Mock(return_value=ROBOT_RADIUS)

        mock.return_value = a_mock

    def test_compute_when_robot_is_at_left_should_have_expected_position(self, config_mock):
        close_corner = RobotCorner(Point(50, 50), Color.NONE)
        far_corner = RobotCorner(Point(65, 58), Color.NONE)
        self._setup_config_mock(config_mock)

        actual_position = robot_location_computer.compute(close_corner,
                                                          far_corner).position

        self.assertEqual(actual_position,
                         EXPECTED_POSITION_WHEN_ROBOT_IS_AT_LEFT)

    def test_compute_when_robot_is_at_right_should_have_expected_position(self, config_mock):
        close_corner = RobotCorner(Point(50, 50), Color.NONE)
        far_corner = RobotCorner(Point(35, 58), Color.NONE)
        self._setup_config_mock(config_mock)

        actual_position = robot_location_computer.compute(close_corner,
                                                          far_corner).position

        self.assertEqual(actual_position,
                         EXPECTED_POSITION_WHEN_ROBOT_IS_AT_RIGHT)

    def test_compute_when_robot_is_at_left_in_first_quadrant_should_have_expected_orientation(self, config_mock):
        close_corner = RobotCorner(Point(50, 50), Color.ORANGE)
        far_corner = RobotCorner(Point(65, 58), Color.PINK)
        self._setup_config_mock(config_mock)

        actual_orientation = robot_location_computer.compute(
            close_corner, far_corner).orientation

        self.assertEqual(
            actual_orientation,
            EXPECTED_ORIENTATION_WHEN_ROBOT_IS_AT_LEFT_IN_FIRST_QUADRANT)

    def test_compute_when_robot_is_at_left_in_second_quadrant_should_have_expected_orientation(self, config_mock):
        close_corner = RobotCorner(Point(50, 50), Color.PINK)
        far_corner = RobotCorner(Point(65, 58), Color.BLUE)
        self._setup_config_mock(config_mock)

        actual_orientation = robot_location_computer.compute(
            close_corner, far_corner).orientation

        self.assertEqual(
            actual_orientation,
            EXPECTED_ORIENTATION_WHEN_ROBOT_IS_AT_LEFT_IN_SECOND_QUADRANT)

    def test_compute_when_robot_is_at_left_in_third_quadrant_should_have_expected_orientation(self, config_mock):
        close_corner = RobotCorner(Point(50, 50), Color.BLUE)
        far_corner = RobotCorner(Point(65, 58), Color.PINK)
        self._setup_config_mock(config_mock)

        actual_orientation = robot_location_computer.compute(
            close_corner, far_corner).orientation

        self.assertEqual(
            actual_orientation,
            EXPECTED_ORIENTATION_WHEN_ROBOT_IS_AT_LEFT_IN_THIRD_QUADRANT)

    def test_compute_when_robot_is_at_left_in_fourth_quadrant_should_have_expected_orientation(self, config_mock):
        close_corner = RobotCorner(Point(50, 50), Color.PINK)
        far_corner = RobotCorner(Point(65, 58), Color.ORANGE)
        self._setup_config_mock(config_mock)

        actual_orientation = robot_location_computer.compute(
            close_corner, far_corner).orientation

        self.assertEqual(
            actual_orientation,
            EXPECTED_ORIENTATION_WHEN_ROBOT_IS_AT_LEFT_IN_FOURTH_QUADRANT)

    def test_compute_when_robot_is_at_right_in_first_quadrant_should_have_expected_orientation(self, config_mock):
        close_corner = RobotCorner(Point(50, 50), Color.ORANGE)
        far_corner = RobotCorner(Point(35, 58), Color.PINK)
        self._setup_config_mock(config_mock)

        actual_orientation = robot_location_computer.compute(
            close_corner, far_corner).orientation

        self.assertEqual(
            actual_orientation,
            EXPECTED_ORIENTATION_WHEN_ROBOT_IS_AT_RIGHT_IN_FIRST_QUADRANT)

    def test_compute_when_robot_is_at_right_in_second_quadrant_should_have_expected_orientation(self, config_mock):
        close_corner = RobotCorner(Point(50, 50), Color.PINK)
        far_corner = RobotCorner(Point(35, 58), Color.ORANGE)
        self._setup_config_mock(config_mock)

        actual_orientation = robot_location_computer.compute(
            close_corner, far_corner).orientation

        self.assertEqual(
            actual_orientation,
            EXPECTED_ORIENTATION_WHEN_ROBOT_IS_AT_RIGHT_IN_SECOND_QUADRANT)

    def test_compute_when_robot_is_at_right_in_third_quadrant_should_have_expected_orientation(self, config_mock):
        close_corner = RobotCorner(Point(50, 50), Color.BLUE)
        far_corner = RobotCorner(Point(35, 58), Color.PINK)
        self._setup_config_mock(config_mock)

        actual_orientation = robot_location_computer.compute(
            close_corner, far_corner).orientation

        self.assertEqual(
            actual_orientation,
            EXPECTED_ORIENTATION_WHEN_ROBOT_IS_AT_RIGHT_IN_THIRD_QUADRANT)

    def test_compute_when_robot_is_at_right_in_fourth_quadrant_should_have_expected_orientation(self, config_mock):
        close_corner = RobotCorner(Point(50, 50), Color.PINK)
        far_corner = RobotCorner(Point(35, 58), Color.BLUE)
        self._setup_config_mock(config_mock)

        actual_orientation = robot_location_computer.compute(
            close_corner, far_corner).orientation

        self.assertEqual(
            actual_orientation,
            EXPECTED_ORIENTATION_WHEN_ROBOT_IS_AT_RIGHT_IN_FOURTH_QUADRANT)
