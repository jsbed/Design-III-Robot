from unittest.mock import MagicMock, Mock
import unittest

from Robot.country.country import Country
from Robot.cycle.objects.color import Color
from Robot.managers.led_manager import LedManager

FULL_COUNTRY_LED_STRING = "F1203645030"
FULL_COUNTRY_WITH_RED_LED_STRING = "F1203645031"
DISPLAY_RED_LED_STRING = "F1203645031"
CLOSE_RED_LED_STRING = "F1203645030"
CLOSE_ALL_LEDS_STRING = "F0000000000"


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

        cls.serial_mock = LedManagerTest.create_serial_mock()

    @staticmethod
    def create_serial_mock():
        serial_mock = MagicMock()
        serial_mock.send_string = Mock()
        return serial_mock

    def setUp(self):
        self._new_led_manager = LedManager(self.serial_mock)
        self._led_manager_with_open_leds = LedManager(self.serial_mock)
        self._led_manager_with_open_leds.display_country(self._a_country)

    def test_new_led_manager_when_display_country_with_a_country_should_call_serial_with_full_country_led_string(self):
        self._new_led_manager.display_country(self._a_country)
        self.serial_mock.send_string.assert_called_with(
            FULL_COUNTRY_LED_STRING)

    def test_led_manager_with_red_led_when_display_country_with_a_country_should_call_serial_with_full_country_with_red_led_string(self):
        led_manager_with_red_led = LedManager(self.serial_mock)
        led_manager_with_red_led.display_red_led()

        led_manager_with_red_led.display_country(self._a_country)

        self.serial_mock.send_string.assert_called_with(
            FULL_COUNTRY_WITH_RED_LED_STRING)

    def test_led_manager_with_open_leds_when_display_red_led_should_call_serial_with_display_red_led_string(self):
        self._led_manager_with_open_leds.display_red_led()
        self.serial_mock.send_string.assert_called_with(
            DISPLAY_RED_LED_STRING)

    def test_led_manager_with_open_leds_when_close_red_led_should_call_serial_with_close_red_led_string(self):
        self._led_manager_with_open_leds.display_red_led()

        self._led_manager_with_open_leds.close_red_led()

        self.serial_mock.send_string.assert_called_with(
            CLOSE_RED_LED_STRING)

    def test_led_manager_with_open_leds_when_close_leds_should_call_serial_with_close_all_leds_string(self):
        self._led_manager_with_open_leds.close_leds()
        self.serial_mock.send_string.assert_called_with(
            CLOSE_ALL_LEDS_STRING)
