from unittest.mock import MagicMock, Mock, patch
import unittest

from Robot.controller.robot_controller import RobotController
from Robot.cycle.objects.color import Color
from Robot.cycle.objects.cube import Cube
from Robot.path_finding.point import Point


@patch('Robot.controller.robot_controller.SerialPort')
class RobotControllerTestForRobotMoveTo(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._cube = Cube(Color.RED, Point(50, 10))
        cls._cube.set_localization_position(Point(80, 150))

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
    @patch('Robot.controller.robot_controller.Robot')
    @patch('Robot.controller.robot_controller.PointAdjustor')
    @patch('Robot.controller.robot_controller.config.Config')
    def test_robot_is_next_to_target_when_robot_is_far_from_target(
            self, ConfigMock, PointAdjustorMock, RobotMock,
            TimeMock, SerialPortMock):
        config_mock = self._setup_config_mock()
        config_mock.get_distance_uncertainty = Mock(return_value=10)
        ConfigMock.return_value = config_mock
        point_adjustor_mock = MagicMock()
        point_adjustor_mock.find_target_position = \
            Mock(return_value=Point(50, 50))
        point_adjustor_mock.find_next_point = Mock(return_value=Point(50, 50))
        point_adjustor_mock.calculate_distance_between_points = \
            Mock(return_value=50)
        PointAdjustorMock.return_value = point_adjustor_mock

        self.assertFalse(
            RobotController().robot_is_next_to_target_with_correct_orientation(
                self._cube.get_localization().position))

    @patch("time.sleep")
    @patch('Robot.controller.robot_controller.Robot')
    @patch('Robot.controller.robot_controller.PointAdjustor')
    @patch('Robot.controller.robot_controller.config.Config')
    def test_robot_is_next_to_target_with_correct_orientation_when_orientation_is_wrong(
            self, ConfigMock, PointAdjustorMock, RobotMock,
            TimeMock, SerialPortMock):
        config_mock = self._setup_config_mock()
        config_mock.get_distance_uncertainty = Mock(return_value=10)
        config_mock.get_orientation_uncertainty = Mock(return_value=5)
        config_mock.get_rotation_min = Mock(return_value=3)
        config_mock.get_orientation_max = Mock(return_value=90)
        ConfigMock.return_value = config_mock
        point_adjustor_mock = MagicMock()
        point_adjustor_mock.find_target_position = \
            Mock(return_value=Point(50, 50))
        point_adjustor_mock.find_next_point = Mock(return_value=Point(50, 50))
        point_adjustor_mock.find_robot_rotation = Mock(return_value=15)
        point_adjustor_mock.calculate_distance_between_points = \
            Mock(return_value=5)
        PointAdjustorMock.return_value = point_adjustor_mock

        self.assertFalse(
            RobotController().robot_is_next_to_target_with_correct_orientation(
                self._cube.get_localization().position))

    @patch("time.sleep")
    @patch('Robot.controller.robot_controller.Robot')
    @patch('Robot.controller.robot_controller.PointAdjustor')
    @patch('Robot.controller.robot_controller.config.Config')
    def test_when_robot_is_next_to_target_with_correct_orientation(
            self, ConfigMock, PointAdjustorMock, RobotMock,
            TimeMock, SerialPortMock):
        config_mock = self._setup_config_mock()
        config_mock.get_distance_uncertainty = Mock(return_value=10)
        config_mock.get_orientation_uncertainty = Mock(return_value=5)
        config_mock.get_rotation_min = Mock(return_value=3)
        config_mock.get_orientation_max = Mock(return_value=90)
        ConfigMock.return_value = config_mock
        point_adjustor_mock = MagicMock()
        point_adjustor_mock.find_target_position = \
            Mock(return_value=Point(50, 50))
        point_adjustor_mock.find_next_point = Mock(return_value=Point(50, 50))
        point_adjustor_mock.find_robot_rotation = Mock(return_value=0)
        point_adjustor_mock.calculate_distance_between_points = \
            Mock(return_value=5)
        PointAdjustorMock.return_value = point_adjustor_mock

        self.assertTrue(
            RobotController().robot_is_next_to_target_with_correct_orientation(
                self._cube.get_localization().position))

    @patch("time.sleep")
    @patch('Robot.controller.robot_controller.MoveForward')
    @patch('Robot.controller.robot_controller.Rotate')
    @patch('Robot.controller.robot_controller.Robot')
    @patch('Robot.controller.robot_controller.PointAdjustor')
    @patch('Robot.controller.robot_controller.config.Config')
    @patch('Robot.controller.robot_controller.BaseStationClient')
    def test_when_move_robot_to_then_execute_instructions_is_called(
            self, BaseStationClientMock, ConfigMock, PointAdjustorMock,
            RobotMock, RotateMock, MoveMock, TimeMock, SerialPortMock):
        config_mock = self._setup_config_mock()
        config_mock.get_distance_uncertainty = Mock(return_value=10)
        config_mock.get_orientation_uncertainty = Mock(return_value=5)
        config_mock.get_rotation_min = Mock(return_value=3)
        config_mock.get_distance_min = Mock(return_value=1)
        config_mock.get_orientation_max = Mock(return_value=90)
        ConfigMock.return_value = config_mock
        point_adjustor_mock = MagicMock()
        point_adjustor_mock.find_target_position = \
            Mock(return_value=Point(50, 50))
        point_adjustor_mock.find_next_point = Mock(return_value=Point(50, 50))
        point_adjustor_mock.find_robot_rotation = Mock(return_value=0)
        point_adjustor_mock.calculate_distance_between_points = \
            Mock(return_value=5)
        PointAdjustorMock.return_value = point_adjustor_mock
        robot_mock = MagicMock()
        RobotMock.return_value = robot_mock

        RobotController().move_robot_to(self._cube.get_localization().position)
        assert robot_mock.execute_instructions.called

    @patch("time.sleep")
    @patch('Robot.controller.robot_controller.MoveForward')
    @patch('Robot.controller.robot_controller.Rotate')
    @patch('Robot.controller.robot_controller.Robot')
    @patch('Robot.controller.robot_controller.PointAdjustor')
    @patch('Robot.controller.robot_controller.config.Config')
    @patch('Robot.controller.robot_controller.BaseStationClient')
    def test_when_move_robot_to_localize_cube_then_execute_instructions_is_called(
            self, BaseStationClientMock, ConfigMock, PointAdjustorMock,
            RobotMock, RotateMock, MoveMock, TimeMock, SerialPortMock):
        config_mock = self._setup_config_mock()
        config_mock.get_distance_uncertainty = Mock(return_value=10)
        config_mock.get_orientation_uncertainty = Mock(return_value=5)
        config_mock.get_rotation_min = Mock(return_value=3)
        config_mock.get_distance_min = Mock(return_value=1)
        config_mock.get_orientation_max = Mock(return_value=90)
        config_mock.get_localize_cube_position = \
            Mock(return_value=Point(55, 85))
        ConfigMock.return_value = config_mock
        point_adjustor_mock = MagicMock()
        point_adjustor_mock.find_robot_rotation = Mock(return_value=0)
        point_adjustor_mock.calculate_distance_between_points = \
            Mock(return_value=50)
        PointAdjustorMock.return_value = point_adjustor_mock
        robot_mock = MagicMock()
        RobotMock.return_value = robot_mock

        RobotController().move_robot_to_localize_cube()
        assert robot_mock.execute_instructions.called

    @patch("time.sleep")
    @patch('Robot.controller.robot_controller.MoveForward')
    @patch('Robot.controller.robot_controller.Rotate')
    @patch('Robot.controller.robot_controller.Robot')
    @patch('Robot.controller.robot_controller.PointAdjustor')
    @patch('Robot.controller.robot_controller.config.Config')
    @patch('Robot.controller.robot_controller.BaseStationClient')
    def test_when_move_robot_to_localize_cube_with_rotation_required_higher_than_90_then_rotate_is_called_4_times(
            self, BaseStationClientMock, ConfigMock, PointAdjustorMock,
            RobotMock, RotateMock, MoveMock, TimeMock, SerialPortMock):
        config_mock = self._setup_config_mock()
        config_mock.get_distance_uncertainty = Mock(return_value=10)
        config_mock.get_orientation_uncertainty = Mock(return_value=5)
        config_mock.get_rotation_min = Mock(return_value=3)
        config_mock.get_distance_min = Mock(return_value=1)
        config_mock.get_orientation_max = Mock(return_value=90)
        config_mock.get_localize_cube_position = \
            Mock(return_value=Point(55, 85))
        ConfigMock.return_value = config_mock
        point_adjustor_mock = MagicMock()
        point_adjustor_mock.find_robot_rotation = Mock(return_value=110)
        point_adjustor_mock.calculate_distance_between_points = \
            Mock(return_value=50)
        PointAdjustorMock.return_value = point_adjustor_mock

        RobotController().move_robot_to_localize_cube()
        self.assertEqual(RotateMock.call_count, 4)

    @patch("time.sleep")
    @patch('Robot.controller.robot_controller.MoveForward')
    @patch('Robot.controller.robot_controller.Robot')
    @patch('Robot.controller.robot_controller.PointAdjustor')
    @patch('Robot.controller.robot_controller.config.Config')
    def test_push_cube_when_robot_is_next_to_cube_then_move_is_called_with_move_backward_distance(
            self, ConfigMock, PointAdjustorMock,
            RobotMock, MoveMock, TimeMock, SerialPortMock):
        config_mock = self._setup_config_mock()
        config_mock.get_gripper_size = Mock(return_value=6)
        config_mock.get_cube_radius = Mock(return_value=4)
        config_mock.get_robot_radius = Mock(return_value=10.5)
        config_mock.get_distance_uncertainty_with_cube = Mock(return_value=4)
        config_mock.get_move_backward_distance = Mock(return_value=-8)
        ConfigMock.return_value = config_mock
        point_adjustor_mock = MagicMock()
        point_adjustor_mock.calculate_distance_between_points = \
            Mock(return_value=20)
        PointAdjustorMock.return_value = point_adjustor_mock

        RobotController().push_cube(self._cube.get_localization().position)
        MoveMock.assert_called_with(-8)

    @patch("time.sleep")
    @patch('Robot.controller.robot_controller.MoveForward')
    @patch('Robot.controller.robot_controller.Rotate')
    @patch('Robot.controller.robot_controller.Robot')
    @patch('Robot.controller.robot_controller.PointAdjustor')
    @patch('Robot.controller.robot_controller.config.Config')
    def test_push_cube_when_robot_is_far_from_cube_and_cube_is_far_from_wall_then_move_is_called_with_push_cube_distance(
            self, ConfigMock, PointAdjustorMock,
            RobotMock, RotateMock, MoveMock, TimeMock, SerialPortMock):
        config_mock = self._setup_config_mock()
        config_mock.get_gripper_size = Mock(return_value=6)
        config_mock.get_cube_radius = Mock(return_value=4)
        config_mock.get_robot_radius = Mock(return_value=10.5)
        config_mock.get_distance_uncertainty_with_cube = Mock(return_value=4)
        config_mock.get_move_backward_distance = Mock(return_value=-8)
        config_mock.get_push_cube_distance = Mock(return_value=25)
        config_mock.get_rotation_min = Mock(return_value=3)
        config_mock.get_orientation_max = Mock(return_value=90)
        ConfigMock.return_value = config_mock
        point_adjustor_mock = MagicMock()
        point_adjustor_mock.calculate_distance_between_points = \
            Mock(return_value=30)
        point_adjustor_mock.find_robot_rotation = Mock(return_value=0)
        point_adjustor_mock.calculate_distance_between_cube_and_closest_wall = \
            Mock(return_value=60)
        PointAdjustorMock.return_value = point_adjustor_mock

        RobotController().push_cube(self._cube.get_localization().position)
        MoveMock.assert_called_with(34.5)
