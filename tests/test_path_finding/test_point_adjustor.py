from unittest.mock import patch, MagicMock, Mock
import unittest

from Robot.path_finding.point import Point
from Robot.path_finding.point_adjustor import PointAdjustor


@patch('Robot.path_finding.point_adjustor.config.Config')
class TestPointAdjuster(unittest.TestCase):

    def setUp(self):
        self._robot_position = Point(50, 50)
        self._robot_orientation = 0

    def test_find_next_point_for_short_distance(self, ConfigMock):
        config_mock = MagicMock()
        config_mock.get_check_points_distance = Mock(return_value=50)
        config_mock.get_distance_uncertainty = Mock(return_value=10)
        ConfigMock.return_value = config_mock
        point_test = Point(80, 80)
        target_position = Point(80, 80)
        point = PointAdjustor().find_next_point(self._robot_position,
                                                target_position)
        self.assertEqual(point_test, point)

    def test_find_next_point_for_long_distance(self, ConfigMock):
        config_mock = MagicMock()
        config_mock.get_check_points_distance = Mock(return_value=50)
        config_mock.get_distance_uncertainty = Mock(return_value=10)
        ConfigMock.return_value = config_mock
        point_test = Point(61, 98)
        target_position = Point(80, 180)
        point = PointAdjustor().find_next_point(self._robot_position,
                                                target_position)
        self.assertEqual(point_test, point)

    def test_find_robot_rotation_for_positive_angle(self, ConfigMock):
        config_mock = MagicMock()
        config_mock.get_table_width = Mock(return_value=111)
        ConfigMock.return_value = config_mock
        rotation_test = 33
        target_position = Point(90, 110)
        rotation = PointAdjustor().find_robot_rotation(
            self._robot_orientation, self._robot_position, target_position)
        self.assertEqual(rotation_test, rotation)

    def test_find_robot_rotation_for_negative_angle(self, ConfigMock):
        config_mock = MagicMock()
        config_mock.get_table_width = Mock(return_value=111)
        ConfigMock.return_value = config_mock
        rotation_test = -56
        target_position = Point(20, 70)
        rotation = PointAdjustor().find_robot_rotation(
            self._robot_orientation, self._robot_position, target_position)
        self.assertEqual(rotation_test, rotation)

    def test_calculate_distance_between_cube_and_east_wall(self, ConfigMock):
        config_mock = MagicMock()
        config_mock.get_table_width = Mock(return_value=111)
        config_mock.get_table_height = Mock(return_value=231)
        ConfigMock.return_value = config_mock
        distance_test = 12
        cube_position = Point(12, 70)
        distance = PointAdjustor().\
            calculate_distance_between_cube_and_closest_wall(cube_position)
        self.assertEqual(distance_test, distance)

    def test_calculate_distance_between_cube_and_west_wall(self, ConfigMock):
        config_mock = MagicMock()
        config_mock.get_table_width = Mock(return_value=111)
        config_mock.get_table_height = Mock(return_value=231)
        ConfigMock.return_value = config_mock
        distance_test = 31
        cube_position = Point(80, 70)
        distance = PointAdjustor().\
            calculate_distance_between_cube_and_closest_wall(cube_position)
        self.assertEqual(distance_test, distance)

    def test_calculate_distance_between_cube_and_north_wall(self, ConfigMock):
        config_mock = MagicMock()
        config_mock.get_table_width = Mock(return_value=111)
        config_mock.get_table_height = Mock(return_value=231)
        ConfigMock.return_value = config_mock
        distance_test = 21
        cube_position = Point(60, 210)
        distance = PointAdjustor().\
            calculate_distance_between_cube_and_closest_wall(cube_position)
        self.assertEqual(distance_test, distance)
