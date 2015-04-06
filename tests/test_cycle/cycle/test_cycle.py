from unittest.mock import MagicMock, Mock, patch
import unittest
from Robot.cycle.cycle import Cycle


class CycleTest(unittest.TestCase):

    @patch('Robot.cycle.cycle.RobotController')
    def setUp(self, robot_controller_mock):
        robot_controller_mock.return_value = MagicMock()
        self._robot_controller_mock = robot_controller_mock.return_value
        self._robot_controller_mock.get_robot = Mock()

        self._cycle = Cycle()

    def test_continue_cycle_when_an_instruction_is_remaining_then_next_instruction_is_called(self):
        self._robot_controller_mock.next_instruction = Mock()
        self._robot_controller_mock.instruction_remaining = Mock(
            return_value=True)

        self._cycle.continue_cycle()

        assert self._robot_controller_mock.next_instruction.called

    def test_observer_update_when_event_is_instruction_finished_then_instruction_remaining_is_called(self):
        self._robot_controller_mock.next_instruction = Mock()
        self._robot_controller_mock.instruction_remaining = Mock(
            return_value=True)

        self._cycle.observer_update("finished instruction", None)

        assert self._robot_controller_mock.instruction_remaining.called

    def test_observer_update_when_event_is_switch_activated_then_turn_switch_on_is_called(self):
        self._robot_controller_mock.turn_switch_on = Mock()

        self._cycle.observer_update("switch activated", None)

        assert self._robot_controller_mock.turn_switch_on.called

    def test_observer_update_when_event_is_switch_deactivated_then_turn_switch_off_is_called(self):
        self._robot_controller_mock.turn_switch_off = Mock()

        self._cycle.observer_update("switch deactivated", None)

        assert self._robot_controller_mock.turn_switch_off.called
