from unittest.mock import MagicMock, Mock
import unittest

from Robot.controller.instructions.rotate import Rotate


CLOCKWISE_ANGLE = 120
ANTICLOCKWISE_ANGLE = -50
ROTATE_CLOCKWISE_ANGLE_STRING = "ROL00000120"
ROTATE_ANTICLOCKWISE_ANGLE_STRING = "ROR00000050"


class RotateTest(unittest.TestCase):

    def setUp(self):
        self.serial_mock = RotateTest.create_serial_mock()

    @staticmethod
    def create_serial_mock():
        serial_mock = MagicMock()
        serial_mock.send_string = Mock()
        return serial_mock

    def test_rotate_when_clockwise_execute_should_call_serial_with_clockwise_angle_string(self):
        rotate_command = Rotate(120)
        rotate_command.execute(self.serial_mock)
        self.serial_mock.send_string.assert_called_with(
            ROTATE_CLOCKWISE_ANGLE_STRING)

    def test_rotate_when_anticlockwise_should_call_serial_with_anticlockwise_angle_string(self):
        rotate_command = Rotate(-50)
        rotate_command.execute(self.serial_mock)
        self.serial_mock.send_string.assert_called_with(
            ROTATE_ANTICLOCKWISE_ANGLE_STRING)

    def test_rotate_without_angle_should_not_call_serial(self):
        rotate_command = Rotate(0)
        rotate_command.execute(self.serial_mock)
        assert not self.serial_mock.send_string.called
