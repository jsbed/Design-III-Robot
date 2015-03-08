from unittest.mock import MagicMock, Mock, patch
import unittest

from Robot.controller.robot_controller import RobotController
from Robot.game_cycle.objects.color import Color
from Robot.game_cycle.objects.cube import Cube
from Robot.path_finding.point import Point


@patch('Robot.path_finding.point_adjustor.config.Config')
@patch('Robot.managers.led_manager.LedManager')
class RobotControllerTest(unittest.TestCase):

    def setUp(self):
        self._cube = Cube(Color.RED, Point(50, 10))
        self._cube.set_localization_position(Point(80, 200))

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
        self.assertFalse(self._robot_controller.get_cube(self._cube))
        self._setup_robot_mock(RobotMock, Point(50, 200), 90)
        self.assertFalse(self._robot_controller.move_cube(self._cube))

    @patch('Robot.controller.robot_controller.Robot')
    def test_get_and_move_cube_with_long_distance_and_right_orientation(self, RobotMock, LedManagerMock, ConfigMock):
        self._setup_config_mock(ConfigMock)
        self._setup_robot_mock(RobotMock, Point(80, 30), 0)
        self.assertFalse(self._robot_controller.get_cube(self._cube))
        self._setup_robot_mock(RobotMock, Point(50, 200), 270)
        self.assertFalse(self._robot_controller.move_cube(self._cube))

    @patch('Robot.controller.robot_controller.Robot')
    def test_get_and_move_cube_when_arrived_to_cube_with_wrong_orientation(self, RobotMock, LedManagerMock, ConfigMock):
        self._setup_config_mock(ConfigMock)
        self._setup_robot_mock(RobotMock, Point(65, 200), 120)
        self.assertFalse(self._robot_controller.get_cube(self._cube))
        self._setup_robot_mock(RobotMock, Point(50, 25), 90)
        self.assertFalse(self._robot_controller.move_cube(self._cube))

    @patch('Robot.controller.robot_controller.Robot')
    def test_get_and_move_cube_when_arrived_to_cube_with_right_orientation(self, RobotMock, LedManagerMock, ConfigMock):
        self._setup_config_mock(ConfigMock)
        self._setup_robot_mock(RobotMock, Point(65, 200), 0)
        self.assertTrue(self._robot_controller.get_cube(self._cube))
        self._setup_robot_mock(RobotMock, Point(50, 25), 270)
        self.assertTrue(self._robot_controller.move_cube(self._cube))

    @patch('Robot.controller.robot_controller.Robot')
    def test_move_to_atlas_with_short_and_long_distance(self, RobotMock, LedManagerMock, ConfigMock):
        self._setup_config_mock(ConfigMock)
        self._setup_robot_mock(RobotMock, Point(95, 20), 90)
        self.assertTrue(self._robot_controller.move_to_atlas())
        self._setup_robot_mock(RobotMock, Point(20, 30), 90)
        self.assertFalse(self._robot_controller.move_to_atlas())

    @patch("time.sleep")
    @patch("Robot.game_cycle.atlas.get_question")
    def test_when_get_question_from_atlas_then_atlas_get_question_is_called(self, AtlasMock, TimeMock, LedManagerMock, ConfigMock):
        self._setup_config_mock(ConfigMock)
        RobotController().get_question_from_atlas()
        assert AtlasMock.called

    @patch("time.sleep")
    @patch("Robot.game_cycle.atlas.get_question")
    def test_when_get_question_from_atlas_then_time_sleep_is_called_with_2_sec(self, AtlasMock, TimeMock, LedManagerMock, ConfigMock):
        RobotController().get_question_from_atlas()
        TimeMock.assert_called_with(2)

    @patch("time.sleep")
    @patch("Robot.game_cycle.atlas.get_question")
    def test_when_get_question_from_atlas_then_display_red_led_is_called(self, AtlasMock, TimeMock, LedManagerMock, ConfigMock):
        led_manager_mock = MagicMock()
        led_manager_mock.display_red_led = Mock()
        LedManagerMock.return_value = led_manager_mock

        RobotController().get_question_from_atlas()
        assert led_manager_mock.display_red_led.called

    @patch("Robot.controller.robot_controller.RobotController")
    def test_display_country_leds(self, RobotControllerMock, LedManagerMock, ConfigMock):
        RobotControllerMock.display_country_leds()
        RobotControllerMock.display_country_leds.assert_called_with()

    @patch("Robot.controller.robot_controller.RobotController")
    def test_ask_for_cube(self, RobotControllerMock, LedManagerMock, ConfigMock):
        RobotControllerMock.ask_for_cube()
        RobotControllerMock.ask_for_cube.assert_called_with()
