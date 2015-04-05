from unittest.mock import MagicMock, Mock
import unittest

from Robot.controller.robot import Robot


class RobotTest(unittest.TestCase):

    FINISHED_INSTRUCTION_SIGNAL = "ok"

    def setUp(self):
        self._robot = Robot(self._create_serial_port_mock())

    def _create_instruction_mock(self):
        a_mock = MagicMock()
        a_mock.execute = Mock()
        return a_mock

    def _create_serial_port_mock(self):
        a_mock = MagicMock()
        a_mock.wait_for_read_line = Mock(
            return_value=self.FINISHED_INSTRUCTION_SIGNAL)

        return a_mock

    def test_given_an_instruction_when_execute_instruction_should_execute_given_instruction(self):
        an_instruction = self._create_instruction_mock()
        self._robot.append_instruction(an_instruction)

        self._robot.execute_instructions()

        assert an_instruction.execute.called

    def test_given_two_instructions_when_execute_instruction_twice_should_execute_both_instruction(self):
        first_instruction = self._create_instruction_mock()
        second_instruction = self._create_instruction_mock()
        self._robot.append_instruction(first_instruction)
        self._robot.append_instruction(second_instruction)

        self._robot.execute_instructions()
        assert first_instruction.execute.called
        assert not second_instruction.execute.called

        self._robot.execute_instructions()
        assert second_instruction.execute.called
