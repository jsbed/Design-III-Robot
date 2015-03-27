from unittest.mock import MagicMock, Mock
import unittest

from Robot.controller.instructions.move import Move


FORWARD_DISTANCE = 20
BACKWARD_DISTANCE = -10
MOVE_FORWARD_DISTANCE_STRING = "GO000000200"
MOVE_BACKWARD_DISTANCE_STRING = "BA000000100"


class MoveTest(unittest.TestCase):

    def setUp(self):
        self.serial_mock = MoveTest.create_serial_mock()

    @staticmethod
    def create_serial_mock():
        serial_mock = MagicMock()
        serial_mock.send_string = Mock()
        return serial_mock

    def test_move_when_forward_should_call_serial_with_move_forward_distance_string(self):
        move_command = Move(20)
        move_command.execute(self.serial_mock)
        self.serial_mock.send_string.assert_called_with(
            MOVE_FORWARD_DISTANCE_STRING)

    def test_move_when_backward_should_call_serial_with_move_backward_distance_string(self):
        move_command = Move(-10)
        move_command.execute(self.serial_mock)
        self.serial_mock.send_string.assert_called_with(
            MOVE_BACKWARD_DISTANCE_STRING)

    def test_move_without_distance_should_not_call_serial(self):
        move_command = Move(0)
        move_command.execute(self.serial_mock)
        assert not self.serial_mock.send_string.called
