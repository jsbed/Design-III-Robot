from unittest.mock import MagicMock, Mock
import unittest

from Robot.cycle.objects.color import Color
from Robot.cycle.objects.cube import Cube
from Robot.managers.led_manager import LedManager


RED_CUBE_STRING = "F1000000000"
GREEN_CUBE_STRING = "F2000000000"
BLUE_CUBE_STRING = "F3000000000"
YELLOW_CUBE_STRING = "F4000000000"
WHITE_CUBE_STRING = "F5000000000"
BLACK_CUBE_STRING = "F6000000000"

RED_CUBE = Cube(Color.RED, None)
GREEN_CUBE = Cube(Color.GREEN, None)
BLUE_CUBE = Cube(Color.BLUE, None)
YELLOW_CUBE = Cube(Color.YELLOW, None)
WHITE_CUBE = Cube(Color.WHITE, None)
BLACK_CUBE = Cube(Color.BLACK, None)


class LedManagerColorTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.serial_mock = LedManagerColorTest.create_serial_mock()

    @staticmethod
    def create_serial_mock():
        serial_mock = MagicMock()
        serial_mock.send_string = Mock()
        return serial_mock

    def setUp(self):
        self._led_manager = LedManager(self.serial_mock)

    def test_led_manager_when_display_flag_led_for_next_cube_with_red_cube_should_call_serial_with_red_cube_string(self):
        self._led_manager.display_flag_led_for_next_cube(RED_CUBE)
        self.serial_mock.send_string.assert_called_with(RED_CUBE_STRING)

    def test_led_manager_when_display_flag_led_for_next_cube_with_green_cube_should_call_serial_with_green_cube_string(self):
        self._led_manager.display_flag_led_for_next_cube(GREEN_CUBE)
        self.serial_mock.send_string.assert_called_with(GREEN_CUBE_STRING)

    def test_led_manager_when_display_flag_led_for_next_cube_with_blue_cube_should_call_serial_with_blue_cube_string(self):
        self._led_manager.display_flag_led_for_next_cube(BLUE_CUBE)
        self.serial_mock.send_string.assert_called_with(BLUE_CUBE_STRING)

    def test_led_manager_when_display_flag_led_for_next_cube_with_yellow_cube_should_call_serial_with_yellow_cube_string(self):
        self._led_manager.display_flag_led_for_next_cube(YELLOW_CUBE)
        self.serial_mock.send_string.assert_called_with(YELLOW_CUBE_STRING)

    def test_led_manager_when_display_flag_led_for_next_cube_with_white_cube_should_call_serial_with_white_cube_string(self):
        self._led_manager.display_flag_led_for_next_cube(WHITE_CUBE)
        self.serial_mock.send_string.assert_called_with(WHITE_CUBE_STRING)

    def test_led_manager_when_display_flag_led_for_next_cube_with_black_cube_should_call_serial_with_black_cube_string(self):
        self._led_manager.display_flag_led_for_next_cube(BLACK_CUBE)
        self.serial_mock.send_string.assert_called_with(BLACK_CUBE_STRING)
