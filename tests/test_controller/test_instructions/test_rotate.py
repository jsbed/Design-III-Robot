import unittest
from unittest.mock import MagicMock, Mock, patch
from Robot.controller.instructions.rotate import Rotate


A_SERIAL_PORT = "SerialPortPath"
ROTATE_120_DEGREES_CLOCKWISE_ENCODED_STRING = "RO000000120".encode()
ROTATE_50_DEGREES_ANTICLOCKWISE_ENCODED_STRING = "RO000000050".encode()  # ****Need command for negative angle****


class RotateTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.serial_mock = RotateTest.create_serial_mock()

    @staticmethod
    def create_serial_mock():
        serial_mock = MagicMock()
        serial_mock.write = Mock()
        return serial_mock

    @patch("Robot.controller.instructions.rotate.serial.Serial")
    def test_rotate_should_call_serial_with_clockwise_angle_encoded_string(self, serial_mock):
        serial_mock.return_value = self.serial_mock
        self._rotate = Rotate()
        self._rotate.rotate(120)
        self._rotate.execute(A_SERIAL_PORT)
        self.serial_mock.write.assert_called_with(ROTATE_120_DEGREES_CLOCKWISE_ENCODED_STRING)

    @patch("Robot.controller.instructions.rotate.serial.Serial")
    def test_rotate_should_call_serial_with_anticlockwise_angle_encoded_string(self, serial_mock):
        serial_mock.return_value = self.serial_mock
        self._rotate = Rotate()
        self._rotate.rotate(-50)
        self._rotate.execute(A_SERIAL_PORT)
        self.serial_mock.write.assert_called_with(ROTATE_50_DEGREES_ANTICLOCKWISE_ENCODED_STRING)
