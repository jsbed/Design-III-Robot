from unittest.mock import MagicMock, Mock
import unittest

from Robot.cycle.objects.color import Color
from Robot.cycle.objects.cube import Cube
from Robot.managers.led_manager import LedManager


FIRST_CUBE_STRING = "F1000000000"
SECOND_CUBE_STRING = "F0100000000"
THIRD_CUBE_STRING = "F0010000000"
FOURTH_CUBE_STRING = "F0001000000"
FIFTH_CUBE_STRING = "F0000100000"
SIXTH_CUBE_STRING = "F0000010000"
SEVENTH_CUBE_STRING = "F0000001000"
EIGHTH_CUBE_STRING = "F0000000100"
NINTH_CUBE_STRING = "F0000000010"

FIRST_CUBE = Cube(Color.RED, None, index=0)
SECOND_CUBE = Cube(Color.RED, None, index=1)
THIRD_CUBE = Cube(Color.RED, None, index=2)
FOURTH_CUBE = Cube(Color.RED, None, index=3)
FIFTH_CUBE = Cube(Color.RED, None, index=4)
SIXTH_CUBE = Cube(Color.RED, None, index=5)
SEVENTH_CUBE = Cube(Color.RED, None, index=6)
EIGHTH_CUBE = Cube(Color.RED, None, index=7)
NINTH_CUBE = Cube(Color.RED, None, index=8)


class LedManagerLedOrderTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.serial_mock = LedManagerLedOrderTest.create_serial_mock()

    @staticmethod
    def create_serial_mock():
        serial_mock = MagicMock()
        serial_mock.write = Mock()
        return serial_mock

    def setUp(self):
        self._led_manager = LedManager(self.serial_mock)

    def test_led_manager_when_display_flag_led_for_next_cube_with_first_cube_should_call_serial_with_first_cube_string(self):
        self._led_manager.display_flag_led_for_next_cube(FIRST_CUBE)
        self.serial_mock.send_string.assert_called_with(FIRST_CUBE_STRING)

    def test_led_manager_when_display_flag_led_for_next_cube_with_second_cube_should_call_serial_with_second_cube_string(self):
        self._led_manager.display_flag_led_for_next_cube(SECOND_CUBE)
        self.serial_mock.send_string.assert_called_with(SECOND_CUBE_STRING)

    def test_led_manager_when_display_flag_led_for_next_cube_with_third_cube_should_call_serial_with_third_cube_string(self):
        self._led_manager.display_flag_led_for_next_cube(THIRD_CUBE)
        self.serial_mock.send_string.assert_called_with(THIRD_CUBE_STRING)

    def test_led_manager_when_display_flag_led_for_next_cube_with_fourth_cube_should_call_serial_with_fourth_cube_string(self):
        self._led_manager.display_flag_led_for_next_cube(FOURTH_CUBE)
        self.serial_mock.send_string.assert_called_with(FOURTH_CUBE_STRING)

    def test_led_manager_when_display_flag_led_for_next_cube_with_fifth_cube_should_call_serial_with_fifth_cube_string(self):
        self._led_manager.display_flag_led_for_next_cube(FIFTH_CUBE)
        self.serial_mock.send_string.assert_called_with(FIFTH_CUBE_STRING)

    def test_led_manager_when_display_flag_led_for_next_cube_with_sixth_cube_should_call_serial_with_sixth_cube_string(self):
        self._led_manager.display_flag_led_for_next_cube(SIXTH_CUBE)
        self.serial_mock.send_string.assert_called_with(SIXTH_CUBE_STRING)

    def test_led_manager_when_display_flag_led_for_next_cube_with_seventh_cube_should_call_serial_with_seventh_cube_string(self):
        self._led_manager.display_flag_led_for_next_cube(SEVENTH_CUBE)
        self.serial_mock.send_string.assert_called_with(SEVENTH_CUBE_STRING)

    def test_led_manager_when_display_flag_led_for_next_cube_with_eighth_cube_should_call_serial_with_eighth_cube_string(self):
        self._led_manager.display_flag_led_for_next_cube(EIGHTH_CUBE)
        self.serial_mock.send_string.assert_called_with(EIGHTH_CUBE_STRING)

    def test_led_manager_when_display_flag_led_for_next_cube_with_ninth_cube_should_call_serial_with_ninth_cube_string(self):
        self._led_manager.display_flag_led_for_next_cube(NINTH_CUBE)
        self.serial_mock.send_string.assert_called_with(NINTH_CUBE_STRING)
