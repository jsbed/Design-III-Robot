from unittest.mock import patch, MagicMock, Mock
import unittest

from Robot.cycle.cycle import Cycle
from Robot.cycle.cycle_state import CycleState
from Robot.path_finding.point import Point


@patch('Robot.cycle.cycle.RobotController')
class CycleTest(unittest.TestCase):

    @staticmethod
    def _setup_country_repository_mock(mock):
        country_repo_mock = MagicMock()
        country_repo_mock.get = Mock()
        mock.return_value = country_repo_mock

    @staticmethod
    def _setup_question_mock(mock):
        question_mock = MagicMock()
        question_mock.answer_question = Mock(return_value="Canada")
        mock.return_value = question_mock

    @staticmethod
    def _setup_flag_mock(has_next_cube):
        flag_mock = MagicMock()
        flag_mock.has_next_cubes = Mock(return_value=has_next_cube)
        flag_mock.next_cube = Mock()
        return flag_mock

    @staticmethod
    def _setup_cube_mock(mock, position, target_zone_position):
        cube_mock = MagicMock()
        cube_mock.get_localization.position = Mock(return_value=position)
        cube_mock.get_target_zone_position = Mock(
            return_value=target_zone_position)
        mock.return_value = cube_mock

    @staticmethod
    def _setup_base_station_client_mock():
        client_mock = MagicMock()
        client_mock.send_question_and_country = Mock()
        return client_mock

    def test_when_start_cycle_then_move_to_atlas_is_called(self, RobotControllerMock):
        robot_controller_mock = MagicMock()
        robot_controller_mock.arrived_at_zone_atlas = Mock(return_value=False)
        robot_controller_mock.move_to_atlas = Mock()
        RobotControllerMock.return_value = robot_controller_mock
        self._new_cycle = Cycle()
        self._new_cycle.start_cycle()

        assert robot_controller_mock.move_to_atlas.called

    def test_continue_cycle_with_instruction_remaining_then_next_instruction_is_called(self, RobotControllerMock):
        robot_controller_mock = MagicMock()
        robot_controller_mock.instruction_remaining = Mock(return_value=True)
        robot_controller_mock.next_instruction = Mock()
        RobotControllerMock.return_value = robot_controller_mock
        self._new_cycle = Cycle()
        self._new_cycle.continue_cycle()

        assert robot_controller_mock.next_instruction.called

    def test_continue_cycle_with_no_instruction_remaining_when_robot_is_not_in_atlas_zone_then_move_to_atlas_is_called(self, RobotControllerMock):
        robot_controller_mock = MagicMock()
        robot_controller_mock.instruction_remaining = Mock(return_value=False)
        robot_controller_mock.arrived_at_zone_atlas = Mock(return_value=False)
        robot_controller_mock.move_to_atlas = Mock()
        RobotControllerMock.return_value = robot_controller_mock
        self._new_cycle = Cycle()
        self._new_cycle.continue_cycle()

        assert robot_controller_mock.move_to_atlas.called

#     @patch('Robot.cycle.cycle.FlagCreator')
#     @patch('Robot.cycle.cycle.CountryRepository')
#     @patch('Robot.cycle.cycle.QuestionAnalyser')
#     def test_continue_cycle_when_robot_arrived_at_atlas_zone_then_multiple_functions_are_called(self, QuestionMock, CountryRepoMock,
#                                                                                                 FlagMock, RobotControllerMock, CubeMock,
#                                                                                                 CountryMock, ConfigMock, TCPClientMock):
#         self._setup_config_mock(ConfigMock)
#         self._setup_country_repository_mock(CountryRepoMock)
#         self._setup_question_mock(QuestionMock)
#         flag_mock = self._setup_flag_mock(True)
#         FlagMock.return_value = flag_mock
#         self._setup_cube_mock(CubeMock, Point(50, 50), None)
#         tcp_client_mock = self._setup_tcp_client_mock()
#         TCPClientMock.return_value = tcp_client_mock
#         robot_controller_mock = MagicMock()
#         robot_controller_mock.instruction_remaining = Mock(return_value=False)
#         robot_controller_mock.arrived_at_zone_atlas = Mock(return_value=True)
#         robot_controller_mock.robot_is_next_to_target_with_correct_orientation = Mock(
#             return_value=False)
#         robot_controller_mock.get_question_from_atlas = Mock()
#         robot_controller_mock.display_country_leds = Mock()
#         robot_controller_mock.ask_for_cube = Mock()
#         robot_controller_mock.move_robot_to = Mock()
#         RobotControllerMock.return_value = robot_controller_mock
#         self._new_cycle = Cycle()
#         self._new_cycle.continue_cycle()
#
#         assert robot_controller_mock.get_question_from_atlas.called
#         assert QuestionMock.called
#         assert CountryRepoMock.called
#         assert flag_mock.has_next_cubes.called
#         assert flag_mock.next_cube.called
#         assert tcp_client_mock.connect_socket.called
#         assert tcp_client_mock.send_data.called
#         assert tcp_client_mock.disconnect_socket.called
#         assert robot_controller_mock.display_country_leds.called
#         assert robot_controller_mock.ask_for_cube.called
#         assert robot_controller_mock.move_robot_to.called
#
#     def test_continue_cycle_when_robot_arrived_at_cube_then_push_cube_is_called(self, RobotControllerMock, CubeMock, CountryMock):
#         self._setup_cube_mock(CubeMock, None, None)
#         robot_controller_mock = MagicMock()
#         robot_controller_mock.instruction_remaining = Mock(return_value=False)
#         robot_controller_mock.robot_is_next_to_target_with_correct_orientation = Mock(
#             return_value=True)
#         robot_controller_mock.push_cube = Mock()
#         RobotControllerMock.return_value = robot_controller_mock
#         self._new_cycle = Cycle()
#         self._new_cycle.set_state(CycleState.MOVE_TO_CUBE)
#         self._new_cycle.continue_cycle()
#
#         assert robot_controller_mock.push_cube.called
#
#     @patch("time.sleep")
#     @patch('Robot.cycle.cycle.GripperManager')
#     def test_continue_cycle_when_cube_is_ready_for_pick_up_then_multiple_functions_are_called(self, GripperMock, TimeMock, RobotControllerMock,
#                                                                                               CubeMock, CountryMock, ConfigMock, TCPClientMock):
#         self._setup_config_mock(ConfigMock)
#         self._setup_cube_mock(CubeMock, None, Point(50, 10))
#         gripper_mock = MagicMock()
#         gripper_mock.take_cube = Mock()
#         gripper_mock.lift_gripper = Mock()
#         GripperMock.return_value = gripper_mock
#         robot_controller_mock = MagicMock()
#         robot_controller_mock.instruction_remaining = Mock(return_value=False)
#         robot_controller_mock.robot_is_next_to_target_with_correct_orientation = Mock(
#             return_value=False)
#         robot_controller_mock.move_robot_to = Mock()
#         RobotControllerMock.return_value = robot_controller_mock
#         self._new_cycle = Cycle()
#         self._new_cycle.set_state(CycleState.PICK_UP_CUBE)
#         self._new_cycle.continue_cycle()
#
#         assert gripper_mock.take_cube.called
#         assert gripper_mock.lift_gripper.called
#         TimeMock.assert_called_with(2)
#         assert robot_controller_mock.move_robot_to.called
#
#     def test_continue_cycle_when_robot_is_at_target_zone_then_move_forward_to_target_zone_is_called(self, RobotControllerMock, CubeMock,
#                                                                                                     CountryMock, ConfigMock, TCPClientMock):
#         self._setup_config_mock(ConfigMock)
#         self._setup_cube_mock(CubeMock, None, Point(50, 10))
#         robot_controller_mock = MagicMock()
#         robot_controller_mock.instruction_remaining = Mock(return_value=False)
#         robot_controller_mock.robot_is_next_to_target_with_correct_orientation = Mock(
#             return_value=True)
#         robot_controller_mock.move_forward_to_target_zone = Mock()
#         RobotControllerMock.return_value = robot_controller_mock
#         self._new_cycle = Cycle()
#
#         self._new_cycle.set_state(CycleState.MOVE_TO_TARGET_ZONE)
#         self._new_cycle.continue_cycle()
#
#         assert robot_controller_mock.move_forward_to_target_zone.called
#
#     @patch("time.sleep")
#     @patch('Robot.cycle.cycle.GripperManager')
#     @patch('Robot.cycle.cycle.FlagCreator')
#     @patch('Robot.cycle.cycle.CountryRepository')
#     @patch('Robot.cycle.cycle.QuestionAnalyser')
#     def test_continue_cycle_when_robot_is_right_in_front_of_target_zone_and_cycle_is_finished_then_multiple_functions_are_called(self, QuestionMock, CountryRepoMock, FlagMock,
#                                                                                                                                  GripperMock, TimeMock, RobotControllerMock,
#                                                                                                                                  CubeMock, CountryMock, ConfigMock, TCPClientMock):
#         self._setup_config_mock(ConfigMock)
#         self._setup_country_repository_mock(CountryRepoMock)
#         self._setup_question_mock(QuestionMock)
#         self._setup_cube_mock(CubeMock, None, Point(50, 10))
#         flag_mock = self._setup_flag_mock(False)
#         FlagMock.return_value = flag_mock
#         gripper_mock = MagicMock()
#         gripper_mock.lower_gripper = Mock()
#         gripper_mock.release_cube = Mock()
#         GripperMock.return_value = gripper_mock
#         robot_controller_mock = MagicMock()
#         robot_controller_mock.instruction_remaining = Mock(return_value=False)
#         robot_controller_mock.robot_is_next_to_target_with_correct_orientation = Mock(
#             return_value=True)
#         RobotControllerMock.return_value = robot_controller_mock
#         self._new_cycle = Cycle()
#
# Create test FlagCreator object
#         self._new_cycle.set_state(CycleState.DISPLAY_COUNTRY)
#         self._new_cycle.continue_cycle()
#
#         self._new_cycle.set_state(CycleState.PUT_DOWN_CUBE)
#         self._new_cycle.continue_cycle()
#
#         assert gripper_mock.lower_gripper.called
#         assert gripper_mock.release_cube.called
#         assert robot_controller_mock.move_backward_from_target_zone.called
#         TimeMock.assert_called_with(2)
#         self.assertEqual(flag_mock.has_next_cubes.call_count, 2)
#         assert not robot_controller_mock.ask_for_cube.called
#
#     @patch("time.sleep")
#     @patch('Robot.cycle.cycle.GripperManager')
#     @patch('Robot.cycle.cycle.FlagCreator')
#     @patch('Robot.cycle.cycle.CountryRepository')
#     @patch('Robot.cycle.cycle.QuestionAnalyser')
#     def test_continue_cycle_when_robot_is_right_in_front_of_target_zone_and_cycle_is_not_finished_then_ask_for_cube_is_called(self, QuestionMock, CountryRepoMock, FlagMock,
#                                                                                                                               GripperMock, TimeMock, RobotControllerMock,
#                                                                                                                               CubeMock, CountryMock, ConfigMock, TCPClientMock):
#         self._setup_config_mock(ConfigMock)
#         self._setup_country_repository_mock(CountryRepoMock)
#         self._setup_question_mock(QuestionMock)
#         self._setup_cube_mock(CubeMock, Point(50, 50), Point(50, 10))
#         flag_mock = self._setup_flag_mock(True)
#         FlagMock.return_value = flag_mock
#         gripper_mock = MagicMock()
#         gripper_mock.lower_gripper = Mock()
#         gripper_mock.release_cube = Mock()
#         GripperMock.return_value = gripper_mock
#         robot_controller_mock = MagicMock()
#         robot_controller_mock.instruction_remaining = Mock(return_value=False)
#         robot_controller_mock.robot_is_next_to_target_with_correct_orientation = Mock(
#             return_value=True)
#         robot_controller_mock.ask_for_cube = Mock()
#         robot_controller_mock.push_cube = Mock()
#         RobotControllerMock.return_value = robot_controller_mock
#         self._new_cycle = Cycle()
#
# Create test FlagCreator object
#         self._new_cycle.set_state(CycleState.DISPLAY_COUNTRY)
#         self._new_cycle.continue_cycle()
#
#         self._new_cycle.set_state(CycleState.PUT_DOWN_CUBE)
#         self._new_cycle.continue_cycle()
#
#         self.assertEqual(robot_controller_mock.ask_for_cube.call_count, 2)
