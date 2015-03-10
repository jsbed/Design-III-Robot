import unittest

from Robot.path_finding.point import Point
from unittest.mock import MagicMock, Mock, patch
from Robot.controller.robot_controller import RobotController
from Robot.game_cycle.objects.cube import Cube
from Robot.game_cycle.objects.color import Color


class GameTest(unittest.TestCase):
    def setUp(self):
        self._cube = Cube(Color.RED, Point(0, 0))
        self._cube.set_localization_position(Point(80, 200))

    def _setup_robot_controller(self):
        self._robot_controller = RobotController()

    def _setup_config_mock(self, mock):
        a_mock = MagicMock()
        a_mock.get_height = Mock(return_value=251)
        a_mock.get_width = Mock(return_value=111)
        a_mock.get_cube_radius = Mock(return_value=4)
        a_mock.get_robot_radius = Mock(return_value=11)
        a_mock.get_atlas_zone_position = Mock(return_value=Point(95, 20))
        a_mock.get_check_points_distance = Mock(return_value=25)
        a_mock.get_distance_uncertainty = Mock(return_value=5)

        mock.return_value = a_mock

    def _setup_robot_mock(self, mock, position, orientation):
        a_mock = MagicMock()
        a_mock.get_localization_position.return_value = position
        a_mock.get_localization_orientation.return_value = orientation

        mock.return_value = a_mock
        self._setup_robot_controller()

    @patch('Robot.controller.robot_controller.Robot')
    @patch('Robot.path_finding.point_adjustor.config.Config')
    def test_get_cube(self, ConfigMock, RobotMock):
        self._setup_config_mock(ConfigMock)
        self._setup_robot_mock(RobotMock, Point(50, 30), 120)
        self.assertFalse(self._robot_controller.get_cube(self._cube))

    @patch('Robot.controller.robot_controller.Robot')
    @patch('Robot.path_finding.point_adjustor.config.Config')
    def test_get_cube_when_arrived_to_cube(self, ConfigMock, RobotMock):
        self._setup_config_mock(ConfigMock)
        self._setup_robot_mock(RobotMock, Point(65, 200), 120)
        self.assertTrue(self._robot_controller.get_cube(self._cube))
