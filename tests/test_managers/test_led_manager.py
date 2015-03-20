from unittest.mock import patch, MagicMock, Mock
import unittest

from Robot.country.country import Country
from Robot.cycle.objects.color import Color
from Robot.managers.led_manager import LedManager

A_SERIAL_PORT = "SerialPortPath"
FULL_COUNTRY_LED_ENCODED_STRING = "F1203645030".encode()
DISPLAY_RED_LED_ENCODED_STRING = "F1203645031".encode()
CLOSE_RED_LED_ENCODED_STRING = "F1203645030".encode()
CLOSE_ALL_LEDS_ENCODED_STRING = "F0000000000".encode()


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
        serial_mock.write = Mock()
        return serial_mock

    @patch("Robot.managers.led_manager.serial.Serial")
    def setUp(self, serial_mock):
        serial_mock.return_value = self.serial_mock
        self._new_led_manager = LedManager(A_SERIAL_PORT)
        self._led_manager_with_open_leds = LedManager(A_SERIAL_PORT)
        self._led_manager_with_open_leds.display_country(self._a_country)

    def test_new_led_manager_when_display_country_with_a_country_should_call_serial_with_full_country_led_encoded_string(self):
        self._new_led_manager.display_country(self._a_country)
        self.serial_mock.write.assert_called_with(
            FULL_COUNTRY_LED_ENCODED_STRING)

    def test_led_manager_with_open_leds_when_display_red_led_should_call_serial_with_display_red_led_encoded_string(self):
        self._led_manager_with_open_leds.display_red_led()
        self.serial_mock.write.assert_called_with(
            DISPLAY_RED_LED_ENCODED_STRING)

    def test_led_manager_with_open_leds_when_close_red_led_should_call_serial_with_close_red_led_encoded_string(self):
        self._led_manager_with_open_leds.display_red_led()

        self._led_manager_with_open_leds.close_red_led()

        self.serial_mock.write.assert_called_with(
            CLOSE_RED_LED_ENCODED_STRING)

    def test_led_manager_with_open_leds_when_close_leds_should_call_serial_with_close_all_leds_encoded_string(self):
        self._led_manager_with_open_leds.close_leds()
        self.serial_mock.write.assert_called_with(
            CLOSE_ALL_LEDS_ENCODED_STRING)
