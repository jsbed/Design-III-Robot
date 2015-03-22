from unittest.mock import MagicMock, Mock, patch
import unittest

from Robot.controller.robot_controller import RobotController
from Robot.country.country import Country
from Robot.cycle.objects.color import Color
from Robot.cycle.objects.cube import Cube
from Robot.path_finding.point import Point


@patch('Robot.path_finding.point_adjustor.config.Config')
@patch('Robot.managers.led_manager.LedManager')
class RobotControllerTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._cube = Cube(Color.RED, Point(50, 10))
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

    @staticmethod
    def _setup_config_mock(mock):
        a_mock = MagicMock()
        a_mock.get_height = Mock(return_value=251)
        a_mock.get_width = Mock(return_value=111)
        a_mock.get_cube_radius = Mock(return_value=4)
        a_mock.get_robot_radius = Mock(return_value=11)
        a_mock.get_atlas_zone_position = Mock(return_value=Point(95, 20))
        a_mock.get_distance_between_objects = Mock(return_value=4)
        a_mock.get_check_points_distance = Mock(return_value=25)
        a_mock.get_distance_uncertainty = Mock(return_value=5)
        a_mock.get_orientation_uncertainty = Mock(return_value=5)
        a_mock.get_red_led_wait_time = Mock(return_value=2)
        a_mock.get_display_country_wait_time = Mock(return_value=5)

        mock.return_value = a_mock

    def _setup_robot_mock(self, mock, position, orientation):
        a_mock = MagicMock()
        a_mock.get_localization_position.return_value = position
        a_mock.get_localization_orientation.return_value = orientation

        mock.return_value = a_mock
        self._robot_controller = RobotController()

    @patch('Robot.controller.robot_controller.Robot')
    def test_get_and_move_cube_with_long_distance_and_wrong_orientation(self, RobotMock, LedManagerMock, ConfigMock):
        self._setup_config_mock(ConfigMock)
        self._setup_robot_mock(RobotMock, Point(80, 30), 120)
        self.assertFalse(self._robot_controller.
                         robot_is_next_to_target_with_correct_orientation(self._cube.get_localization().position))
        self._setup_robot_mock(RobotMock, Point(50, 200), 90)
        self.assertFalse(self._robot_controller.
                         robot_is_next_to_target_with_correct_orientation(self._cube.get_target_zone_position()))

    @patch('Robot.controller.robot_controller.Robot')
    def test_get_and_move_cube_with_long_distance_and_right_orientation(self, RobotMock, LedManagerMock, ConfigMock):
        self._setup_config_mock(ConfigMock)
        self._setup_robot_mock(RobotMock, Point(80, 30), 0)
        self.assertFalse(self._robot_controller.
                         robot_is_next_to_target_with_correct_orientation(self._cube.get_localization().position))
        self._setup_robot_mock(RobotMock, Point(50, 200), 270)
        self.assertFalse(self._robot_controller.
                         robot_is_next_to_target_with_correct_orientation(self._cube.get_target_zone_position()))

    @patch('Robot.controller.robot_controller.Robot')
    def test_get_and_move_cube_when_arrived_to_cube_with_wrong_orientation(self, RobotMock, LedManagerMock, ConfigMock):
        self._setup_config_mock(ConfigMock)
        self._setup_robot_mock(RobotMock, Point(65, 200), 120)
        self.assertFalse(self._robot_controller.
                         robot_is_next_to_target_with_correct_orientation(self._cube.get_localization().position))
        self._setup_robot_mock(RobotMock, Point(50, 25), 90)
        self.assertFalse(self._robot_controller.
                         robot_is_next_to_target_with_correct_orientation(self._cube.get_target_zone_position()))

    @patch('Robot.controller.robot_controller.Robot')
    def test_get_and_move_cube_when_arrived_to_cube_with_right_orientation(self, RobotMock, LedManagerMock, ConfigMock):
        self._setup_config_mock(ConfigMock)
        self._setup_robot_mock(RobotMock, Point(65, 200), 0)
        self.assertTrue(self._robot_controller.
                        robot_is_next_to_target_with_correct_orientation(self._cube.get_localization().position))
        self._setup_robot_mock(RobotMock, Point(50, 25), 270)
        self.assertTrue(self._robot_controller.
                        robot_is_next_to_target_with_correct_orientation(self._cube.get_target_zone_position()))

    @patch('Robot.controller.robot_controller.Robot')
    def test_move_to_atlas_with_short_and_long_distance(self, RobotMock, LedManagerMock, ConfigMock):
        self._setup_config_mock(ConfigMock)
        self._setup_robot_mock(RobotMock, Point(95, 20), 90)
        self.assertTrue(self._robot_controller.arrived_at_zone_atlas())
        self._setup_robot_mock(RobotMock, Point(20, 30), 90)
        self.assertFalse(self._robot_controller.arrived_at_zone_atlas())

    @patch('Robot.controller.robot_controller.Rotate')
    @patch('Robot.controller.robot_controller.Robot')
    def test_when_robot_move_to_point_then_rotate_is_called(self, RobotMock, RotateMock, LedManagerMock, ConfigMock):
        self._setup_config_mock(ConfigMock)
        self._setup_robot_mock(RobotMock, Point(50, 50), 0)
        rotate_mock = MagicMock()
        RotateMock.return_value = rotate_mock

        RobotController().move_robot_to(Point(95, 20))
        RobotController().move_to_atlas()
        self.assertEqual(rotate_mock.rotate.call_count, 2)

    @patch('Robot.controller.robot_controller.Move')
    @patch('Robot.controller.robot_controller.Robot')
    def test_when_robot_move_to_point_then_move_is_called(self, RobotMock, MoveMock, LedManagerMock, ConfigMock):
        self._setup_config_mock(ConfigMock)
        self._setup_robot_mock(RobotMock, Point(50, 50), 0)
        move_mock = MagicMock()
        MoveMock.return_value = move_mock

        RobotController().move_robot_to(Point(95, 20))
        RobotController().move_to_atlas()
        self.assertEqual(move_mock.move.call_count, 2)

    @patch('Robot.controller.robot_controller.Robot')
    def test_when_robot_move_to_point_then_append_instruction_is_called_twice(self, RobotMock, LedManagerMock, ConfigMock):
        self._setup_config_mock(ConfigMock)
        robot_mock = MagicMock()
        robot_mock.get_localization_position.return_value = Point(50, 50)
        robot_mock.get_localization_orientation.return_value = 0
        RobotMock.return_value = robot_mock

        RobotController().move_robot_to(Point(95, 20))
        RobotController().move_to_atlas()
        self.assertEqual(robot_mock.append_instruction.call_count, 4)

    @patch('Robot.controller.robot_controller.Robot')
    def test_when_robot_move_to_point_then_execute_instructions_is_called(self, RobotMock, LedManagerMock, ConfigMock):
        self._setup_config_mock(ConfigMock)
        robot_mock = MagicMock()
        robot_mock.get_localization_position.return_value = Point(50, 50)
        robot_mock.get_localization_orientation.return_value = 0
        RobotMock.return_value = robot_mock

        RobotController().move_robot_to(Point(95, 20))
        RobotController().move_to_atlas()
        self.assertEqual(robot_mock.execute_instructions.call_count, 2)

    @patch("time.sleep")
    @patch("Robot.cycle.atlas.get_question")
    def test_when_get_question_from_atlas_then_atlas_get_question_is_called(self, AtlasMock, TimeMock, LedManagerMock, ConfigMock):
        self._setup_config_mock(ConfigMock)
        RobotController().get_question_from_atlas()
        assert AtlasMock.called

    @patch("time.sleep")
    @patch("Robot.cycle.atlas.get_question")
    def test_when_get_question_from_atlas_then_time_sleep_is_called_with_2_sec(self, AtlasMock, TimeMock, LedManagerMock, ConfigMock):
        self._setup_config_mock(ConfigMock)
        RobotController().get_question_from_atlas()
        TimeMock.assert_called_with(2)

    @patch("time.sleep")
    @patch("Robot.cycle.atlas.get_question")
    def test_when_get_question_from_atlas_then_display_red_led_is_called(self, AtlasMock, TimeMock, LedManagerMock, ConfigMock):
        led_manager_mock = MagicMock()
        led_manager_mock.display_red_led = Mock()
        LedManagerMock.return_value = led_manager_mock

        RobotController().get_question_from_atlas()
        assert led_manager_mock.display_red_led.called

    @patch("time.sleep")
    def test_when_display_country_leds_then_display_country_is_called(self, TimeMock, LedManagerMock, ConfigMock):
        led_manager_mock = MagicMock()
        led_manager_mock.display_country = Mock()
        LedManagerMock.return_value = led_manager_mock

        RobotController().display_country_leds(self._a_country)
        assert led_manager_mock.display_country.called

    @patch("time.sleep")
    def test_when_display_country_leds_then_time_sleep_is_called_with_5_sec(self, TimeMock, LedManagerMock, ConfigMock):
        self._setup_config_mock(ConfigMock)
        RobotController().display_country_leds(self._a_country)
        TimeMock.assert_called_with(5)

    def test_when_ask_for_cube_then_next_flag_led_is_called(self, LedManagerMock, ConfigMock):
        led_manager_mock = MagicMock()
        led_manager_mock.next_flag_led = Mock()
        LedManagerMock.return_value = led_manager_mock

        RobotController().ask_for_cube(self._cube)
        assert led_manager_mock.next_flag_led.called
