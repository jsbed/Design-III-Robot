from unittest.mock import MagicMock, Mock, patch, call
import unittest
from Robot.country.country import Country
from Robot.cycle.cycle import Cycle
from Robot.cycle.objects.color import Color
from Robot.cycle.objects.cube import Cube
from Robot.path_finding.point import Point


class CycleTestLocalizeCubeState(unittest.TestCase):

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

    @patch('Robot.cycle.cycle.RobotController')
    def setUp(self, robot_controller_mock):
        robot_controller_mock.return_value = MagicMock()
        self._robot_controller_mock = robot_controller_mock.return_value
        self._robot_controller_mock.get_robot = Mock()

        self._cycle = Cycle()

    @patch("time.sleep")
    @patch('Robot.cycle.cycle.FlagCreator')
    @patch('Robot.cycle.cycle.QuestionAnalyser')
    @patch('Robot.cycle.cycle.CountryRepository')
    @patch('Robot.cycle.cycle.BaseStationClient')
    def test_when_localize_cube_state_then_robot_controller_is_called(
            self, base_station_client_mock, country_mock,
            question_mock, flag_mock, TimeMock):
        base_station_client_mock.return_value = MagicMock()
        base_station_client_mock.return_value.send_question = Mock()
        base_station_client_mock.return_value.send_country = Mock()
        base_station_client_mock.return_value.send_cubes_location = Mock()
        country_mock.return_value = MagicMock()
        country_mock.return_value.get = Mock(return_value=self._a_country)
        question_mock.return_value = MagicMock()
        question_mock.return_value.answer_question = Mock()
        flag_mock.return_value = MagicMock()
        flag_mock.return_value.get_cube_order = Mock()
        flag_mock.return_value.next_cube = Mock(return_value=self._cube)
        flag_mock.return_value.has_next_cubes = Mock(return_value=True)
        self._robot_controller_mock.arrived_at_zone_atlas = Mock(
            return_value=True)
        self._robot_controller_mock.get_question_from_atlas = Mock()
        self._robot_controller_mock.display_country_leds = Mock()
        self._robot_controller_mock.ask_for_cube = Mock()
        self._robot_controller_mock.move_robot_to_localize_cube = Mock()
        self._robot_controller_mock.get_gripper = Mock()
        self._robot_controller_mock.\
            robot_is_next_to_target_with_correct_orientation = Mock(
                return_value=False)
        self._robot_controller_mock.move_robot_to = Mock()
        self._robot_controller_mock.find_cube_position = Mock()
        self._robot_controller_mock.robot_is_facing_cube = Mock(return_value=True)
        self._robot_controller_mock.instruction_remaining = Mock(
            return_value=False)

        self._cycle.start_cycle()
        self._cycle.continue_cycle()

        calls = [call.robot_is_facing_cube(),
                 call.find_cube_position(),
                 call.robot_is_next_to_target_with_correct_orientation(
                 flag_mock.return_value.next_cube().
                 get_localization().position),
                 call.move_robot_to(
                 flag_mock.return_value.next_cube().
                 get_localization().position)]

        self._robot_controller_mock.assert_has_calls(calls)
