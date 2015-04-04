from unittest.mock import patch, MagicMock, Mock
import unittest

from Robot.cycle.objects.color import Color
from Robot.cycle.objects.cube import Cube
from Robot.path_finding.point import Point
from Robot.path_finding.point_adjustor import PointAdjustor


class TestPointAdjusterTargetPosition(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._cube = Cube(Color.RED, 0)

    def _setup_config_mock(self, mock):
        config_mock = MagicMock()
        config_mock.get_table_height = Mock(return_value=231)
        config_mock.get_table_width = Mock(return_value=111)
        config_mock.get_cube_radius = Mock(return_value=4)
        config_mock.get_robot_radius = Mock(return_value=11)
        config_mock.get_distance_between_objects = Mock(return_value=4)
        config_mock.get_gripper_size = Mock(return_value=6)

        mock.return_value = config_mock

    @patch('Robot.path_finding.point_adjustor.config.Config')
    def _find_target_point_and_robot_orientation(self, ConfigMock):
        self._setup_config_mock(ConfigMock)
        robot_position = Point(50, 50)
        point = PointAdjustor().find_target_position(
            self._cube.get_localization().position, robot_position)
        orientation = PointAdjustor().find_robot_rotation(
            0, robot_position, self._cube.get_localization().position)

        self.assertEqual(self._point_test, point)
        self.assertEqual(self._orientation_test, orientation)

    def test_when_cube_is_near_east_wall(self):
        self._point_test = Point(30, 50)
        self._orientation_test = -90
        self._cube.set_localization_position(Point(5, 50))
        self._find_target_point_and_robot_orientation()

    def test_when_cube_is_near_west_wall(self):
        self._point_test = Point(81, 30)
        self._orientation_test = 110
        self._cube.set_localization_position(Point(106, 30))
        self._find_target_point_and_robot_orientation()

    def test_when_cube_is_near_north_wall(self):
        self._point_test = Point(50, 202)
        self._orientation_test = 0
        self._cube.set_localization_position(Point(50, 227))
        self._find_target_point_and_robot_orientation()

    def test_when_cube_is_top_left_of_robot(self):
        self._point_test = Point(70, 45)
        self._orientation_test = 45
        self._cube.set_localization_position(Point(70, 70))
        self._find_target_point_and_robot_orientation()

    def test_when_cube_is_top_right_of_robot(self):
        self._point_test = Point(33, 45)
        self._orientation_test = -40
        self._cube.set_localization_position(Point(33, 70))
        self._find_target_point_and_robot_orientation()

    def test_when_cube_is_bottom_right_of_robot(self):
        self._point_test = Point(21, 40)
        self._orientation_test = -140
        self._cube.set_localization_position(Point(21, 15))
        self._find_target_point_and_robot_orientation()

    def test_when_cube_is_bottom_left_of_robot(self):
        self._point_test = Point(70, 40)
        self._orientation_test = 151
        self._cube.set_localization_position(Point(70, 15))
        self._find_target_point_and_robot_orientation()
