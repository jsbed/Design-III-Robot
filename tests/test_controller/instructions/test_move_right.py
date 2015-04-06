from unittest.mock import MagicMock, Mock
import unittest

from Robot.controller.instructions.move_right import MoveRight


RIGHT_DISTANCE = 20
LEFT_DISTANCE = -10
MOVE_RIGHT_DISTANCE_STRING = "RI000000200"
MOVE_LEFT_DISTANCE_STRING = "LE000000100"


class MoveRightTest(unittest.TestCase):

    def setUp(self):
        self.serial_mock = MoveRightTest.create_serial_mock()

    @staticmethod
    def create_serial_mock():
        serial_mock = MagicMock()
        serial_mock.send_string = Mock()
        return serial_mock

    def test_move_when_forward_should_call_serial_with_move_forward_distance_string(self):
        move_command = MoveRight(20)
        move_command.execute(self.serial_mock)
        self.serial_mock.send_string.assert_called_with(
            MOVE_RIGHT_DISTANCE_STRING)

    def test_move_when_backward_should_call_serial_with_move_backward_distance_string(self):
        move_command = MoveRight(-10)
        move_command.execute(self.serial_mock)
        self.serial_mock.send_string.assert_called_with(
            MOVE_LEFT_DISTANCE_STRING)

    def test_move_without_distance_should_not_call_serial(self):
        move_command = MoveRight(0)
        move_command.execute(self.serial_mock)
        assert not self.serial_mock.send_string.called
