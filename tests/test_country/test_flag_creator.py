from unittest.mock import patch, MagicMock, Mock
import unittest

from Robot.country.country import Country
from Robot.country.flag_creator import FlagCreator
from Robot.cycle.objects.color import Color
from Robot.cycle.objects.cube import Cube
from Robot.path_finding.point import Point


EXPECTED_FIRST_CUBE = Cube(Color.WHITE, Point(76.5, 34.5), index=6)
EXPECTED_SECOND_CUBE = Cube(Color.BLUE, Point(52.5, 34.5), index=8)
EXPECTED_THIRD_CUBE = Cube(Color.BLUE, Point(76.5, 46.5), index=3)
EXPECTED_FOURTH_CUBE = Cube(Color.BLACK, Point(64.5, 46.5), index=4)
EXPECTED_FIFTH_CUBE = Cube(Color.YELLOW, Point(52.5, 46.5), index=5)
EXPECTED_SIXTH_CUBE = Cube(Color.RED, Point(76.5, 58.5), index=0)
EXPECTED_LAST_CUBE = Cube(Color.GREEN, Point(64.5, 58.5), index=1)

EXPECTED_CUBE_ORDER = [EXPECTED_FIRST_CUBE, EXPECTED_SECOND_CUBE,
                       EXPECTED_THIRD_CUBE, EXPECTED_FOURTH_CUBE,
                       EXPECTED_FIFTH_CUBE, EXPECTED_SIXTH_CUBE,
                       EXPECTED_LAST_CUBE]


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
            return_value=Point(5, 55))
        a_mock.get_target_zone_position = Mock(return_value=Point(85.5, 85.5))
        a_mock.get_cube_radius = Mock(return_value=4)
        a_mock.get_cube_center_distance = Mock(return_value=12)

        mock.return_value = a_mock

    def test_has_next_cube_when_has_remaining_cube(self):
        self.assertTrue(self.flag_creator.has_next_cubes())

    def test_has_next_cube_when_has_no_remaining_cube(self):
        for _ in range(7):
            self.flag_creator.next_cube()

        self.assertFalse(self.flag_creator.has_next_cubes())

    def test_get_cube_order(self):
        actual_cube_order = self.flag_creator.get_cube_order()

        self.assert_cube_sequence(actual_cube_order, EXPECTED_CUBE_ORDER)

    def test_sequence_of_next_cube(self):
        self.assert_equal_cube(self.flag_creator.next_cube(),
                               EXPECTED_FIRST_CUBE)
        self.assert_equal_cube(self.flag_creator.next_cube(),
                               EXPECTED_SECOND_CUBE)
        self.assert_equal_cube(self.flag_creator.next_cube(),
                               EXPECTED_THIRD_CUBE)
        self.assert_equal_cube(self.flag_creator.next_cube(),
                               EXPECTED_FOURTH_CUBE)
        self.assert_equal_cube(self.flag_creator.next_cube(),
                               EXPECTED_FIFTH_CUBE)
        self.assert_equal_cube(self.flag_creator.next_cube(),
                               EXPECTED_SIXTH_CUBE)
        self.assert_equal_cube(self.flag_creator.next_cube(),
                               EXPECTED_LAST_CUBE)
        self.assertRaises(Exception, self.flag_creator.next_cube())

    def assert_equal_cube(self, actual_cube, expected_cube):
        self.assertEqual(actual_cube.get_color(), expected_cube.get_color())
        self.assertEqual(actual_cube.get_target_zone_position(),
                         expected_cube.get_target_zone_position())
        self.assertEqual(actual_cube.get_index(), expected_cube.get_index())

    def assert_cube_sequence(self, actual_sequence, expected_sequence):
        self.assertEqual(len(actual_sequence), len(expected_sequence))

        for actual_cube, expected_cube in zip(actual_sequence,
                                              expected_sequence):
            self.assert_equal_cube(actual_cube, expected_cube)
