import unittest
from Robot.controller.robot import Robot
from unittest.mock import patch, MagicMock, Mock


A_SERIAL_PORT = "SerialPortPath"


class RobotTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.rotate_mock = RobotTest.create_mock()
        cls.move_mock = RobotTest.create_mock()

    @staticmethod
    def create_mock():
        a_mock = MagicMock()
        a_mock.execute = Mock()
        return a_mock

    def setUp(self):
        self._robot = Robot(A_SERIAL_PORT)

    @patch('Robot.controller.instructions.move.Move')
    @patch('Robot.controller.instructions.rotate.Rotate')
    def test_execute_multiple_instructions(self, RotateMock, MoveMock):
        RotateMock.return_value = self.rotate_mock
        MoveMock.return_value = self.move_mock
        self._robot.append_instruction(self.rotate_mock.execute)
        self._robot.append_instruction(self.move_mock.execute)
        self._robot.execute_instructions()
        self._robot.execute_instructions()
        self.rotate_mock.execute.assert_called_with(A_SERIAL_PORT)
        self.move_mock.execute.assert_called_with(A_SERIAL_PORT)

    @patch('Robot.controller.instructions.rotate.Rotate')
    def test_execute_a_rotation(self, RotateMock):
        RotateMock.return_value = self.rotate_mock
        self._robot.append_instruction(self.rotate_mock.execute)
        self._robot.execute_instructions()
        self.rotate_mock.execute.assert_called_with(A_SERIAL_PORT)

    @patch('Robot.controller.instructions.move.Move')
    def test_execute_a_movement(self, MoveMock):
        MoveMock.return_value = self.move_mock
        self._robot.append_instruction(self.move_mock.execute)
        self._robot.execute_instructions()
        self.move_mock.execute.assert_called_with(A_SERIAL_PORT)
