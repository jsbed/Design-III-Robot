import unittest
from Robot.country.country import Country
from Robot.game_cycle.objects.color import Color
from unittest.mock import patch, MagicMock, Mock
from Robot.country.flag_creator import FlagCreator
from Robot.path_finding.point import Point
from Robot.managers.led_manager import LedManager


class LedManagerTest(unittest.TestCase):

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
        self.led_manager = LedManager(None)

    def _setup_config_mock(self, mock):
        a_mock = MagicMock()
        a_mock.get_flag_creation_zone_position = Mock(
            return_value=Point(6, 53))
        a_mock.get_target_zone_position = Mock(return_value=Point(85, 85))
        a_mock.get_cube_radius = Mock(return_value=4)
        a_mock.get_cube_center_distance = Mock(return_value=12)

        mock.return_value = a_mock

    def test_display_and_close_next_flag_leds(self):
        cube = self.flag_creator.next_cube()
        self.led_manager.display_next_flag_led(cube)
        self.assertEqual("F0000005000", self.led_manager._led_status)
        cube = self.flag_creator.next_cube()
        self.led_manager.display_next_flag_led(cube)
        self.assertEqual("F0000005030", self.led_manager._led_status)
        cube = self.flag_creator.next_cube()
        self.led_manager.display_next_flag_led(cube)
        self.assertEqual("F0003005030", self.led_manager._led_status)
        cube = self.flag_creator.next_cube()
        self.led_manager.display_next_flag_led(cube)
        self.assertEqual("F0003605030", self.led_manager._led_status)
        cube = self.flag_creator.next_cube()
        self.led_manager.display_next_flag_led(cube)
        self.assertEqual("F0003645030", self.led_manager._led_status)
        cube = self.flag_creator.next_cube()
        self.led_manager.display_next_flag_led(cube)
        self.assertEqual("F1003645030", self.led_manager._led_status)
        cube = self.flag_creator.next_cube()
        self.led_manager.display_next_flag_led(cube)
        self.assertEqual("F1203645030", self.led_manager._led_status)
        self.led_manager.close_leds()
        self.assertEqual("F0000000000", self.led_manager._led_status)

    def test_display_and_close_country_leds(self):
        self.led_manager.display_country(self._a_country)
        self.assertEqual("F1203645030", self.led_manager._led_status)
        self.led_manager.close_leds()
        self.assertEqual("F0000000000", self.led_manager._led_status)

    def test_display_and_close_red_led(self):
        self.led_manager.display_red_led()
        self.assertEqual("F0000000001", self.led_manager._led_status)
        self.led_manager.close_red_led()
        self.assertEqual("F0000000000", self.led_manager._led_status)
