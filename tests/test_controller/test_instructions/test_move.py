import unittest
from unittest.mock import MagicMock, Mock, patch
from Robot.controller.instructions.move import Move


A_SERIAL_PORT = "SerialPortPath"
MOVE_20_CM_FORWARD_ENCODED_STRING = "GO000000200".encode()
MOVE_10_CM_BACKWARD_ENCODED_STRING = "BA000000100".encode()


class MoveTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.serial_mock = MoveTest.create_serial_mock()

    @staticmethod
    def create_serial_mock():
        serial_mock = MagicMock()
        serial_mock.write = Mock()
        return serial_mock

    @patch("Robot.controller.instructions.move.serial.Serial")
    def test_move_should_call_serial_with_move_forward_distance_encoded_string(self, serial_mock):
        serial_mock.return_value = self.serial_mock
        self._move = Move()
        self._move.move(20)
        self._move.execute(A_SERIAL_PORT)
        self.serial_mock.write.assert_called_with(MOVE_20_CM_FORWARD_ENCODED_STRING)

    @patch("Robot.controller.instructions.move.serial.Serial")
    def test_move_should_call_serial_with_move_backward_distance_encoded_string(self, serial_mock):
        serial_mock.return_value = self.serial_mock
        self._move = Move()
        self._move.move(-10)
        self._move.execute(A_SERIAL_PORT)
        self.serial_mock.write.assert_called_with(MOVE_10_CM_BACKWARD_ENCODED_STRING)
