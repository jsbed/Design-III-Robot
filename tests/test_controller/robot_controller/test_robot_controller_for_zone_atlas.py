from unittest.mock import MagicMock, Mock, patch
import unittest

from Robot.controller.robot_controller import RobotController
from Robot.path_finding.point import Point


@patch('Robot.controller.robot_controller.SerialPort')
class RobotControllerTestForZoneAtlas(unittest.TestCase):

    @staticmethod
    def _setup_config_mock():
        config_mock = MagicMock()
        config_mock.get_stm_serial_port_path = \
            Mock(return_value="/dev/ttyUSB0")
        config_mock.get_stm_serial_port_baudrate = Mock(return_value=19200)
        config_mock.get_stm_serial_port_timeout = Mock(return_value=0.5)
        config_mock.get_pololu_serial_port_path = \
            Mock(return_value="/dev/ttyACM0")
        return config_mock

    @patch("time.sleep")
    @patch("Robot.cycle.atlas.get_question")
    @patch('Robot.controller.robot_controller.LedManager')
    @patch('Robot.controller.robot_controller.config.Config')
    def test_when_get_question_from_atlas_then_display_red_led_is_called(
            self, ConfigMock, LedManagerMock, GetQuestionMock, TimeMock,
            SerialPortMock):
        config_mock = self._setup_config_mock()
        config_mock.get_red_led_wait_time = Mock(return_value=2)
        ConfigMock.return_value = config_mock
        led_manager_mock = MagicMock()
        LedManagerMock.return_value = led_manager_mock

        RobotController().get_question_from_atlas()
        assert led_manager_mock.display_red_led.called

    @patch("time.sleep")
    @patch("Robot.cycle.atlas.get_question")
    @patch('Robot.controller.robot_controller.LedManager')
    @patch('Robot.controller.robot_controller.config.Config')
    def test_when_get_question_from_atlas_then_time_sleep_is_called_with_2_sec(
            self, ConfigMock, LedManagerMock, GetQuestionMock, TimeMock,
            SerialPortMock):
        config_mock = self._setup_config_mock()
        config_mock.get_red_led_wait_time = Mock(return_value=2)
        ConfigMock.return_value = config_mock

        RobotController().get_question_from_atlas()
        TimeMock.assert_called_with(2)

    @patch("time.sleep")
    @patch("Robot.cycle.atlas.get_question")
    @patch('Robot.controller.robot_controller.LedManager')
    @patch('Robot.controller.robot_controller.config.Config')
    def test_when_get_question_from_atlas_then_close_red_led_is_called(
            self, ConfigMock, LedManagerMock, GetQuestionMock, TimeMock,
            SerialPortMock):
        config_mock = self._setup_config_mock()
        config_mock.get_red_led_wait_time = Mock(return_value=2)
        ConfigMock.return_value = config_mock
        led_manager_mock = MagicMock()
        LedManagerMock.return_value = led_manager_mock

        RobotController().get_question_from_atlas()
        assert led_manager_mock.close_red_led.called

    @patch("time.sleep")
    @patch("Robot.cycle.atlas.get_question")
    @patch('Robot.controller.robot_controller.LedManager')
    @patch('Robot.controller.robot_controller.config.Config')
    def test_when_get_question_from_atlas_then_atlas_get_question_is_called(
            self, ConfigMock, LedManagerMock, GetQuestionMock, TimeMock,
            SerialPortMock):
        config_mock = self._setup_config_mock()
        config_mock.get_red_led_wait_time = Mock(return_value=2)
        ConfigMock.return_value = config_mock
        get_question_mock = MagicMock()
        GetQuestionMock.return_value = get_question_mock

        RobotController().get_question_from_atlas()
        assert GetQuestionMock.called

    @patch("time.sleep")
    @patch('Robot.controller.robot_controller.Robot')
    @patch('Robot.controller.robot_controller.PointAdjustor')
    @patch('Robot.controller.robot_controller.config.Config')
    def test_arrived_at_zone_atlas_when_robot_is_not_at_zone_atlas(
            self, ConfigMock, PointAdjustorMock, RobotMock, TimeMock,
            SerialPortMock):
        config_mock = self._setup_config_mock()
        config_mock.get_atlas_distance_uncertainty = Mock(return_value=15)
        ConfigMock.return_value = config_mock
        point_adjustor_mock = MagicMock()
        point_adjustor_mock.calculate_distance_between_points = \
            Mock(return_value=50)
        PointAdjustorMock.return_value = point_adjustor_mock

        self.assertFalse(RobotController().arrived_at_zone_atlas())

    @patch("time.sleep")
    @patch('Robot.controller.robot_controller.Robot')
    @patch('Robot.controller.robot_controller.PointAdjustor')
    @patch('Robot.controller.robot_controller.config.Config')
    def test_arrived_at_zone_atlas_when_robot_is_at_zone_atlas(
            self, ConfigMock, PointAdjustorMock, RobotMock, TimeMock,
            SerialPortMock):
        config_mock = self._setup_config_mock()
        config_mock.get_atlas_distance_uncertainty = Mock(return_value=15)
        ConfigMock.return_value = config_mock
        point_adjustor_mock = MagicMock()
        point_adjustor_mock.calculate_distance_between_points = \
            Mock(return_value=12)
        PointAdjustorMock.return_value = point_adjustor_mock

        self.assertTrue(RobotController().arrived_at_zone_atlas())

    @patch("time.sleep")
    @patch('Robot.controller.robot_controller.Move')
    @patch('Robot.controller.robot_controller.Rotate')
    @patch('Robot.controller.robot_controller.Robot')
    @patch('Robot.controller.robot_controller.PointAdjustor')
    @patch('Robot.controller.robot_controller.config.Config')
    @patch('Robot.controller.robot_controller.BaseStationClient')
    def test_move_to_atlas_when_robot_rotation_required_is_higher_than_rotation_max_then_rotate_is_called_twice(
            self, BaseStationClientMock, ConfigMock, PointAdjustorMock,
            RobotMock, RotateMock, MoveMock, TimeMock, SerialPortMock):
        config_mock = self._setup_config_mock()
        config_mock.get_atlas_zone_position = Mock(return_value=Point(25, 25))
        config_mock.get_rotation_min = Mock(return_value=3)
        config_mock.get_distance_min = Mock(return_value=1)
        config_mock.get_orientation_max = Mock(return_value=90)
        ConfigMock.return_value = config_mock
        point_adjustor_mock = MagicMock()
        point_adjustor_mock.calculate_distance_between_points = \
            Mock(return_value=55)
        point_adjustor_mock.find_robot_rotation = Mock(return_value=110)
        PointAdjustorMock.return_value = point_adjustor_mock

        RobotController().move_to_atlas()
        self.assertEqual(RotateMock.call_count, 2)

    @patch("time.sleep")
    @patch('Robot.controller.robot_controller.Move')
    @patch('Robot.controller.robot_controller.Rotate')
    @patch('Robot.controller.robot_controller.Robot')
    @patch('Robot.controller.robot_controller.PointAdjustor')
    @patch('Robot.controller.robot_controller.config.Config')
    @patch('Robot.controller.robot_controller.BaseStationClient')
    def test_move_to_atlas_when_robot_rotation_required_is_lower_than_rotation_max_then_rotate_is_called_once(
            self, BaseStationClientMock, ConfigMock, PointAdjustorMock,
            RobotMock, RotateMock, MoveMock, TimeMock, SerialPortMock):
        config_mock = self._setup_config_mock()
        config_mock.get_atlas_zone_position = Mock(return_value=Point(25, 25))
        config_mock.get_rotation_min = Mock(return_value=3)
        config_mock.get_distance_min = Mock(return_value=1)
        config_mock.get_orientation_max = Mock(return_value=90)
        ConfigMock.return_value = config_mock
        point_adjustor_mock = MagicMock()
        point_adjustor_mock.calculate_distance_between_points = \
            Mock(return_value=55)
        point_adjustor_mock.find_robot_rotation = Mock(return_value=80)
        PointAdjustorMock.return_value = point_adjustor_mock

        RobotController().move_to_atlas()
        self.assertEqual(RotateMock.call_count, 1)

    @patch("time.sleep")
    @patch('Robot.controller.robot_controller.Move')
    @patch('Robot.controller.robot_controller.Rotate')
    @patch('Robot.controller.robot_controller.Robot')
    @patch('Robot.controller.robot_controller.PointAdjustor')
    @patch('Robot.controller.robot_controller.config.Config')
    @patch('Robot.controller.robot_controller.BaseStationClient')
    def test_move_to_atlas_when_distance_is_shorter_than_min_distance_then_move_is_not_called(
            self, BaseStationClientMock, ConfigMock, PointAdjustorMock,
            RobotMock, RotateMock, MoveMock, TimeMock, SerialPortMock):
        config_mock = self._setup_config_mock()
        config_mock.get_atlas_zone_position = Mock(return_value=Point(25, 25))
        config_mock.get_rotation_min = Mock(return_value=3)
        config_mock.get_distance_min = Mock(return_value=1)
        config_mock.get_orientation_max = Mock(return_value=90)
        ConfigMock.return_value = config_mock
        point_adjustor_mock = MagicMock()
        point_adjustor_mock.calculate_distance_between_points = \
            Mock(return_value=0.8)
        point_adjustor_mock.find_robot_rotation = Mock(return_value=80)
        PointAdjustorMock.return_value = point_adjustor_mock

        RobotController().move_to_atlas()
        self.assertEqual(MoveMock.call_count, 0)

    @patch("time.sleep")
    @patch('Robot.controller.robot_controller.Move')
    @patch('Robot.controller.robot_controller.Rotate')
    @patch('Robot.controller.robot_controller.Robot')
    @patch('Robot.controller.robot_controller.PointAdjustor')
    @patch('Robot.controller.robot_controller.config.Config')
    @patch('Robot.controller.robot_controller.BaseStationClient')
    def test_move_to_atlas_when_rotation_is_shorter_than_min_rotation_then_rotate_is_not_called(
            self, BaseStationClientMock, ConfigMock, PointAdjustorMock,
            RobotMock, RotateMock, MoveMock, TimeMock, SerialPortMock):
        config_mock = self._setup_config_mock()
        config_mock.get_atlas_zone_position = Mock(return_value=Point(25, 25))
        config_mock.get_rotation_min = Mock(return_value=3)
        config_mock.get_distance_min = Mock(return_value=1)
        config_mock.get_orientation_max = Mock(return_value=90)
        ConfigMock.return_value = config_mock
        point_adjustor_mock = MagicMock()
        point_adjustor_mock.calculate_distance_between_points = \
            Mock(return_value=50)
        point_adjustor_mock.find_robot_rotation = Mock(return_value=2)
        PointAdjustorMock.return_value = point_adjustor_mock

        RobotController().move_to_atlas()
        self.assertEqual(RotateMock.call_count, 0)

    @patch("time.sleep")
    @patch('Robot.controller.robot_controller.Move')
    @patch('Robot.controller.robot_controller.Rotate')
    @patch('Robot.controller.robot_controller.Robot')
    @patch('Robot.controller.robot_controller.PointAdjustor')
    @patch('Robot.controller.robot_controller.config.Config')
    @patch('Robot.controller.robot_controller.BaseStationClient')
    def test_move_to_atlas_then_execute_instructions_is_called(
            self, BaseStationClientMock, ConfigMock, PointAdjustorMock,
            RobotMock, RotateMock, MoveMock, TimeMock, SerialPortMock):
        config_mock = self._setup_config_mock()
        config_mock.get_atlas_zone_position = Mock(return_value=Point(25, 25))
        config_mock.get_rotation_min = Mock(return_value=3)
        config_mock.get_distance_min = Mock(return_value=1)
        config_mock.get_orientation_max = Mock(return_value=90)
        ConfigMock.return_value = config_mock
        point_adjustor_mock = MagicMock()
        point_adjustor_mock.calculate_distance_between_points = \
            Mock(return_value=50)
        point_adjustor_mock.find_robot_rotation = Mock(return_value=2)
        PointAdjustorMock.return_value = point_adjustor_mock
        robot_mock = MagicMock()
        RobotMock.return_value = robot_mock

        RobotController().move_to_atlas()
        assert robot_mock.execute_instructions.called
