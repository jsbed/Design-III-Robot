from unittest.mock import MagicMock, Mock, patch, call
import unittest

from Robot.controller.robot_controller import RobotController
from Robot.country.country import Country
from Robot.cycle.objects.color import Color
from Robot.cycle.objects.cube import Cube
from Robot.path_finding.point import Point


class RobotControllerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._cube = Cube(Color.RED, Point(80, 30))
        cls._cube.set_localization_position(Point(80, 200))
        cls._a_country = Country("TestCountry", [Color.RED,
                                                 Color.GREEN,
                                                 Color.NONE,
                                                 Color.BLUE,
                                                 Color.BLACK,
                                                 Color.YELLOW,
                                                 Color.WHITE,
                                                 Color.NONE,
                                                 Color.BLUE])

    @patch('Robot.controller.robot_controller.SerialPort')
    @patch('Robot.controller.robot_controller.config.Config')
    @patch('Robot.controller.robot_controller.LedManager')
    @patch('Robot.controller.robot_controller.Robot')
    @patch('Robot.controller.robot_controller.GripperManager')
    def setUp(self, gripper_mock, robot_mock, led_manager_mock,
              config_mock, serial_port_mock):
        new_config_mock = self._setup_config_mock()
        config_mock.return_value = new_config_mock
        led_manager_mock.return_value = MagicMock()

        self._config_mock = config_mock
        self._serial_port_mock = serial_port_mock
        self._led_manager_mock = led_manager_mock.return_value
        self._robot_mock = robot_mock
        self._gripper_mock = gripper_mock

        self._robot_controller = RobotController()

    @staticmethod
    def _setup_config_mock():
        config_mock = MagicMock()
        config_mock.get_stm_serial_port_path = Mock()
        config_mock.get_stm_serial_port_baudrate = Mock()
        config_mock.get_stm_serial_port_timeout = Mock()
        config_mock.get_pololu_serial_port_path = Mock()
        return config_mock

    @patch("time.sleep")
    @patch('Robot.controller.robot_controller.config.Config')
    def test_when_display_country_leds_then_display_country_and_close_leds_are_called(
            self, ConfigMock, TimeMock):
        config_mock = MagicMock()
        config_mock.get_display_country_wait_time = Mock(return_value=5)
        ConfigMock.return_value = config_mock
        self._led_manager_mock.display_country = Mock()
        self._led_manager_mock.close_leds = Mock()

        self._robot_controller.display_country_leds(self._a_country)

        calls = [call.display_country(self._a_country),
                 call.close_leds()]

        self._led_manager_mock.assert_has_calls(calls)

    @patch("time.sleep")
    @patch('Robot.controller.robot_controller.config.Config')
    def test_when_display_country_leds_then_time_sleep_is_called_with_5_secs(
            self, ConfigMock, TimeMock):
        config_mock = MagicMock()
        config_mock.get_display_country_wait_time = Mock(return_value=5)
        ConfigMock.return_value = config_mock
        self._led_manager_mock.display_country = Mock()
        self._led_manager_mock.close_leds = Mock()

        self._robot_controller.display_country_leds(self._a_country)

        TimeMock.assert_called_with(5)


#
#     @patch('Robot.controller.robot_controller.LedManager')
#     def test_when_ask_for_cube_then_display_flag_led_for_next_cube_is_called(
#             self, LedManagerMock, ConfigMock, SerialPortMock):
#         config_mock = self._setup_config_mock()
#         ConfigMock.return_value = config_mock
#         led_manager_mock = MagicMock()
#         LedManagerMock.return_value = led_manager_mock
#
#         RobotController().ask_for_cube(self._cube)
#         assert led_manager_mock.display_flag_led_for_next_cube.called
#
#     @patch("time.sleep")
#     @patch('Robot.controller.robot_controller.Lateral')
#     @patch('Robot.controller.robot_controller.Move')
#     @patch('Robot.controller.robot_controller.Rotate')
#     @patch('Robot.controller.robot_controller.Robot')
#     @patch('Robot.controller.robot_controller.PointAdjustor')
#     def test_move_forward_to_target_zone_when_lateral_distance_is_higher_than_distance_min_then_lateral_is_called(
#             self, PointAdjustorMock, RobotMock,
#             RotateMock, MoveMock, LateralMock, TimeMock, ConfigMock, SerialPortMock):
#         config_mock = self._setup_config_mock()
#         config_mock.get_gripper_size = Mock(return_value=6)
#         config_mock.get_cube_radius = Mock(return_value=4)
#         config_mock.get_robot_radius = Mock(return_value=10.5)
#         config_mock.get_rotation_min = Mock(return_value=3)
#         config_mock.get_distance_min = Mock(return_value=1)
#         config_mock.get_orientation_max = Mock(return_value=90)
#         ConfigMock.return_value = config_mock
#         point_adjustor_mock = MagicMock()
#         point_adjustor_mock.find_robot_rotation = Mock(return_value=0)
#         PointAdjustorMock.return_value = point_adjustor_mock
#         robot_mock = MagicMock()
#         robot_mock.get_localization_position = \
#             Mock(return_value=Point(85, 60))
#         RobotMock.return_value = robot_mock
#
#         RobotController().move_forward_to_target_zone(
#             self._cube.get_target_zone_position())
#         LateralMock.assert_called_with(-5)
#
#     @patch("time.sleep")
#     @patch('Robot.controller.robot_controller.Lateral')
#     @patch('Robot.controller.robot_controller.Move')
#     @patch('Robot.controller.robot_controller.Rotate')
#     @patch('Robot.controller.robot_controller.Robot')
#     @patch('Robot.controller.robot_controller.PointAdjustor')
#     def test_move_forward_to_target_zone_when_lateral_distance_is_lower_than_distance_min_then_lateral_is_not_called(
#             self, PointAdjustorMock, RobotMock,
#             RotateMock, MoveMock, LateralMock, TimeMock, ConfigMock, SerialPortMock):
#         config_mock = self._setup_config_mock()
#         config_mock.get_gripper_size = Mock(return_value=6)
#         config_mock.get_cube_radius = Mock(return_value=4)
#         config_mock.get_robot_radius = Mock(return_value=10.5)
#         config_mock.get_rotation_min = Mock(return_value=3)
#         config_mock.get_distance_min = Mock(return_value=1)
#         config_mock.get_orientation_max = Mock(return_value=90)
#         ConfigMock.return_value = config_mock
#         point_adjustor_mock = MagicMock()
#         point_adjustor_mock.find_robot_rotation = Mock(return_value=0)
#         PointAdjustorMock.return_value = point_adjustor_mock
#         robot_mock = MagicMock()
#         robot_mock.get_localization_position = \
#             Mock(return_value=Point(81, 60))
#         RobotMock.return_value = robot_mock
#
#         RobotController().move_forward_to_target_zone(
#             self._cube.get_target_zone_position())
#         self.assertFalse(LateralMock.called)
#
#     @patch("time.sleep")
#     @patch('Robot.controller.robot_controller.Lateral')
#     @patch('Robot.controller.robot_controller.Move')
#     @patch('Robot.controller.robot_controller.Rotate')
#     @patch('Robot.controller.robot_controller.Robot')
#     @patch('Robot.controller.robot_controller.PointAdjustor')
#     def test_when_move_forward_to_target_zone_then_move_is_called_with_correct_distance(
#             self, PointAdjustorMock, RobotMock,
#             RotateMock, MoveMock, LateralMock, TimeMock, ConfigMock, SerialPortMock):
#         config_mock = self._setup_config_mock()
#         config_mock.get_gripper_size = Mock(return_value=6)
#         config_mock.get_cube_radius = Mock(return_value=4)
#         config_mock.get_robot_radius = Mock(return_value=10.5)
#         config_mock.get_rotation_min = Mock(return_value=3)
#         config_mock.get_distance_min = Mock(return_value=1)
#         config_mock.get_orientation_max = Mock(return_value=90)
#         ConfigMock.return_value = config_mock
#         point_adjustor_mock = MagicMock()
#         point_adjustor_mock.find_robot_rotation = Mock(return_value=0)
#         PointAdjustorMock.return_value = point_adjustor_mock
#         robot_mock = MagicMock()
#         robot_mock.get_localization_position = \
#             Mock(return_value=Point(85, 60))
#         RobotMock.return_value = robot_mock
#
#         RobotController().move_forward_to_target_zone(
#             self._cube.get_target_zone_position())
#         MoveMock.assert_called_with(
#             robot_mock.get_localization_position.return_value.y -
#             self._cube.get_target_zone_position().y -
#             config_mock.get_gripper_size.return_value -
#             config_mock.get_cube_radius.return_value -
#             config_mock.get_robot_radius.return_value)
#
#     @patch('Robot.controller.robot_controller.Move')
#     @patch('Robot.controller.robot_controller.Robot')
#     def test_when_move_backward_then_move_is_called_with_move_backward_distance(
#             self, RobotMock, MoveMock, ConfigMock, SerialPortMock):
#         config_mock = self._setup_config_mock()
#         config_mock.get_move_backward_distance = Mock(return_value=-8)
#         ConfigMock.return_value = config_mock
#
#         RobotController().move_backward()
#         MoveMock.assert_called_with(-8)
#
#     @patch('Robot.controller.robot_controller.Robot')
#     def test_instruction_remaining_when_at_least_one_instruction_is_remaining(
#             self, RobotMock, ConfigMock, SerialPortMock):
#         config_mock = self._setup_config_mock()
#         ConfigMock.return_value = config_mock
#         robot_mock = MagicMock()
#         robot_mock.get_instructions = Mock(return_value=[1])
#         RobotMock.return_value = robot_mock
#
#         self.assertTrue(RobotController().instruction_remaining())
#
#     @patch('Robot.controller.robot_controller.Robot')
#     def test_instruction_remaining_when_no_instruction_are_remaining(
#             self, RobotMock, ConfigMock, SerialPortMock):
#         config_mock = self._setup_config_mock()
#         ConfigMock.return_value = config_mock
#         robot_mock = MagicMock()
#         robot_mock.get_instructions = Mock(return_value=[])
#         RobotMock.return_value = robot_mock
#
#         self.assertFalse(RobotController().instruction_remaining())
#
#     @patch('Robot.controller.robot_controller.Robot')
#     def test_next_instruction_then_execute_instructions_is_called(
#             self, RobotMock, ConfigMock, SerialPortMock):
#         config_mock = self._setup_config_mock()
#         ConfigMock.return_value = config_mock
#         robot_mock = MagicMock()
#         RobotMock.return_value = robot_mock
#
#         RobotController().next_instruction()
#         assert robot_mock.execute_instructions.called
#
#     @patch('Robot.controller.robot_controller.LedManager')
#     def test_end_cycle_then_display_red_led_is_called(
#             self, LedManagerMock, ConfigMock, SerialPortMock):
#         config_mock = self._setup_config_mock()
#         ConfigMock.return_value = config_mock
#         led_manager_mock = MagicMock()
#         LedManagerMock.return_value = led_manager_mock
#
#         RobotController().end_cycle()
#         assert led_manager_mock.display_red_led.called
