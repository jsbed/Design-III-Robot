from unittest.mock import patch, MagicMock, Mock
import unittest

from Robot.controller.robot import Robot
from Robot.game_cycle.objects.color import Color
from Robot.game_cycle.objects.cube import Cube
from Robot.path_finding.point import Point
from Robot.path_finding.point_adjustor import PointAdjustor


class TestPointAdjuster(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._cube = Cube(Color.RED, 0)
        cls._robot = Robot()

    def setUp(self):
        self._robot.set_localization_position(Point(50, 50))
        self._point_test = Point(0, 0)

    def _setup_config_mock(self, mock):
        a_mock = MagicMock()
        a_mock.get_height = Mock(return_value=251)
        a_mock.get_width = Mock(return_value=111)
        a_mock.get_cube_radius = Mock(return_value=4)
        a_mock.get_robot_radius = Mock(return_value=11)
        a_mock.get_atlas_zone_position = Mock(return_value=Point(95, 20))

        mock.return_value = a_mock

    @patch('Robot.path_finding.point_adjustor.config.Config')
    def _adjustor(self, ConfigMock):
        self._setup_config_mock(ConfigMock)
        point = PointAdjustor().find_target_position(self._cube.get_localization().position,
                                                     self._robot.get_localization().position)
        self.assertEqual(self._point_test, point)

    def test_when_cube_is_near_west_wall(self):
        self._point_test = Point(18, 50)
        self._cube.set_localization_position(Point(3, 50))
        self._adjustor()

    def test_when_cube_is_near_east_wall(self):
        self._point_test = Point(95, 30)
        self._cube.set_localization_position(Point(110, 30))
        self._adjustor()

    def test_when_cube_is_near_north_wall(self):
        self._point_test = Point(50, 236)
        self._cube.set_localization_position(Point(50, 251))
        self._adjustor()

    def test_when_cube_is_near_south_wall(self):
        self._point_test = Point(80, 23)
        self._cube.set_localization_position(Point(80, 8))
        self._adjustor()

    def test_when_cube_is_top_right_of_robot(self):
        self._point_test = Point(55, 70)
        self._cube.set_localization_position(Point(70, 70))
        self._adjustor()

    def test_when_cube_is_top_left_of_robot(self):
        self._point_test = Point(33, 55)
        self._cube.set_localization_position(Point(33, 70))
        self._adjustor()

    def test_when_cube_is_bottum_left_of_robot(self):
        self._point_test = Point(21, 30)
        self._cube.set_localization_position(Point(21, 15))
        self._adjustor()

    def test_when_cube_is_bottum_right_of_robot(self):
        self._point_test = Point(55, 15)
        self._cube.set_localization_position(Point(70, 15))
        self._adjustor()

    def test_when_cube_is_near_wall_and_robot(self):
        self._point_test = Point(35, 60)
        self._cube.set_localization_position(Point(20, 60))
        self._adjustor()
