from unittest.mock import patch, MagicMock, Mock
import unittest

from Robot.cycle.objects.color import Color
from Robot.cycle.objects.cube import Cube
from Robot.path_finding.point import Point
from Robot.path_finding.point_adjustor import PointAdjustor


class TestPointAdjuster(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._cube = Cube(Color.RED, 0)

    def setUp(self):
        self._robot_position = Point(50, 50)
        self._point_test = Point(0, 0)

    def _setup_config_mock(self, mock):
        a_mock = MagicMock()
        a_mock.get_height = Mock(return_value=231)
        a_mock.get_width = Mock(return_value=111)
        a_mock.get_cube_radius = Mock(return_value=4)
        a_mock.get_robot_radius = Mock(return_value=11)
        a_mock.get_distance_between_objects = Mock(return_value=4)
        a_mock.get_check_points_distance = Mock(return_value=25)
        a_mock.get_distance_uncertainty = Mock(return_value=5)
        a_mock.get_atlas_zone_position = Mock(return_value=Point(95, 20))
        a_mock.get_table_width = Mock(return_value=111)

        mock.return_value = a_mock

    @patch('Robot.path_finding.point_adjustor.config.Config')
    def _find_target_point_and_robot_orientation(self, ConfigMock):
        self._setup_config_mock(ConfigMock)
        point = \
            PointAdjustor().find_target_position(self._cube.get_localization().
                                                 position,
                                                 self._robot_position)
        orientation = \
            PointAdjustor().find_robot_orientation(0, self._robot_position,
                                                   self._cube.
                                                   get_localization().
                                                   position)
        self.assertEqual(self._point_test, point)
        self.assertEqual(self._orientation_test, orientation)

    def test_when_cube_is_near_west_wall(self):
        self._point_test = Point(24, 50)
        self._orientation_test = -90
        self._cube.set_localization_position(Point(5, 50))
        self._find_target_point_and_robot_orientation()

    def test_when_cube_is_near_east_wall(self):
        self._point_test = Point(87, 30)
        self._orientation_test = 110
        self._cube.set_localization_position(Point(106, 30))
        self._find_target_point_and_robot_orientation()

    def test_when_cube_is_near_north_wall(self):
        self._point_test = Point(50, 208)
        self._orientation_test = 0
        self._cube.set_localization_position(Point(50, 227))
        self._find_target_point_and_robot_orientation()

    def test_when_cube_is_top_right_of_robot(self):
        self._point_test = Point(70, 51)
        self._orientation_test = 45
        self._cube.set_localization_position(Point(70, 70))
        self._find_target_point_and_robot_orientation()

    def test_when_cube_is_top_left_of_robot(self):
        self._point_test = Point(33, 51)
        self._orientation_test = -40
        self._cube.set_localization_position(Point(33, 70))
        self._find_target_point_and_robot_orientation()

    def test_when_cube_is_bottom_left_of_robot(self):
        self._point_test = Point(21, 34)
        self._orientation_test = -140
        self._cube.set_localization_position(Point(21, 15))
        self._find_target_point_and_robot_orientation()

    def test_when_cube_is_bottom_right_of_robot(self):
        self._point_test = Point(70, 34)
        self._orientation_test = 151
        self._cube.set_localization_position(Point(70, 15))
        self._find_target_point_and_robot_orientation()

    def test_when_cube_is_near_wall_and_robot(self):
        self._point_test = Point(39, 60)
        self._orientation_test = -71
        self._cube.set_localization_position(Point(20, 60))
        self._find_target_point_and_robot_orientation()

    @patch('Robot.path_finding.point_adjustor.config.Config')
    def test_find_next_point_for_short_distance(self, ConfigMock):
        self._setup_config_mock(ConfigMock)
        self._point_test = Point(50, 50)
        point = PointAdjustor().find_next_point(Point(30, 40), Point(50, 50))
        self.assertEqual(self._point_test, point)

    @patch('Robot.path_finding.point_adjustor.config.Config')
    def test_find_next_point_for_long_distance(self, ConfigMock):
        self._setup_config_mock(ConfigMock)
        self._point_test = Point(28, 36)
        point = PointAdjustor().find_next_point(Point(15, 15), Point(50, 50))
        self.assertEqual(self._point_test, point)
