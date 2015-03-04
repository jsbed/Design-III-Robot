from unittest.mock import patch, MagicMock, Mock
import unittest

from Robot.country.country import Country
from Robot.country.flag_creator import FlagCreator
from Robot.game_cycle.objects.color import Color
from Robot.game_cycle.objects.cube import Cube
from Robot.path_finding.point import Point


FIRST_CUBE = Cube(Color.WHITE, Point(75, 36))
SECOND_CUBE = Cube(Color.BLUE, Point(51, 36))
THIRD_CUBE = Cube(Color.BLUE, Point(75, 48))
FOURTH_CUBE = Cube(Color.BLACK, Point(63, 48))
FIFTH_CUBE = Cube(Color.YELLOW, Point(51, 48))
SIXTH_CUBE = Cube(Color.RED, Point(75, 60))
LAST_CUBE = Cube(Color.GREEN, Point(63, 60))


class FlagCreatorTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._a_country = Country("TestCountry", [Color.RED,
                                                 Color.GREEN,
                                                 Color.NONE,
                                                 Color.BLUE,
                                                 Color.BLACK,
                                                 Color.YELLOW,
                                                 Color.WHITE,
                                                 Color.NONE,
                                                 Color.BLUE])

    @patch("Robot.configuration.config.Config")
    def setUp(self, config_mock):
        self._setup_config_mock(config_mock)
        self.flag_creator = FlagCreator(self._a_country)

    def _setup_config_mock(self, mock):
        a_mock = MagicMock()
        a_mock.get_flag_creation_zone_position = Mock(
            return_value=Point(6, 53))
        a_mock.get_target_zone_position = Mock(return_value=Point(85, 85))
        a_mock.get_cube_radius = Mock(return_value=4)
        a_mock.get_cube_center_distance = Mock(return_value=12)

        mock.return_value = a_mock

    def test_has_next_cube_when_has_remaining_cube(self):
        self.assertTrue(self.flag_creator.has_next_cubes())

    def test_has_next_cube_when_has_no_remaining_cube(self):
        for _ in range(7):
            self.flag_creator.next_cube()

        self.assertFalse(self.flag_creator.has_next_cubes())

    def test_sequence_of_next_cube(self):
        self.assert_equal_cube(self.flag_creator.next_cube(), FIRST_CUBE)
        self.assert_equal_cube(self.flag_creator.next_cube(), SECOND_CUBE)
        self.assert_equal_cube(self.flag_creator.next_cube(), THIRD_CUBE)
        self.assert_equal_cube(self.flag_creator.next_cube(), FOURTH_CUBE)
        self.assert_equal_cube(self.flag_creator.next_cube(), FIFTH_CUBE)
        self.assert_equal_cube(self.flag_creator.next_cube(), SIXTH_CUBE)
        self.assert_equal_cube(self.flag_creator.next_cube(), LAST_CUBE)
        self.assertRaises(IndexError, self.flag_creator.next_cube())

    def assert_equal_cube(self, actual_cube, expected_cube):
        self.assertEqual(actual_cube.get_color(), expected_cube.get_color())
        self.assertEqual(actual_cube.get_target_zone_position(),
                         expected_cube.get_target_zone_position())
