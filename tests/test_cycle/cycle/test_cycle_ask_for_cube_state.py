from unittest.mock import MagicMock, Mock, patch, call
import unittest
from Robot.country.country import Country
from Robot.cycle.cycle import Cycle
from Robot.cycle.objects.color import Color
from Robot.cycle.objects.cube import Cube
from Robot.path_finding.point import Point


class CycleTestAskForCubeState(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._cube = Cube(Color.RED, Point(80, 30))
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

    @patch('Robot.cycle.cycle.FlagCreator')
    @patch('Robot.cycle.cycle.QuestionAnalyser')
    @patch('Robot.cycle.cycle.CountryRepository')
    @patch('Robot.cycle.cycle.BaseStationClient')
    def test_ask_for_cube_state_when_has_next_cube_then_flag_creator_is_called(
            self, base_station_client_mock, country_mock,
            question_mock, flag_mock):
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
        flag_mock.return_value.next_cube = Mock()
        flag_mock.return_value.has_next_cubes = Mock(return_value=True)
        self._robot_controller_mock.arrived_at_zone_atlas = Mock(
            return_value=True)
        self._robot_controller_mock.get_question_from_atlas = Mock()
        self._robot_controller_mock.display_country_leds = Mock()
        self._robot_controller_mock.ask_for_cube = Mock()
        self._robot_controller_mock.move_robot_to_localize_cube = Mock()

        self._cycle.start_cycle()

        calls = [call().has_next_cubes(), call().next_cube()]

        flag_mock.assert_has_calls(calls)

    @patch('Robot.cycle.cycle.FlagCreator')
    @patch('Robot.cycle.cycle.QuestionAnalyser')
    @patch('Robot.cycle.cycle.CountryRepository')
    @patch('Robot.cycle.cycle.BaseStationClient')
    def test_ask_for_cube_state_when_has_next_cube_then_robot_controller_is_called(
            self, base_station_client_mock, country_mock,
            question_mock, flag_mock):
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
        flag_mock.return_value.next_cube = Mock()
        flag_mock.return_value.has_next_cubes = Mock(return_value=True)
        self._robot_controller_mock.arrived_at_zone_atlas = Mock(
            return_value=True)
        self._robot_controller_mock.get_question_from_atlas = Mock()
        self._robot_controller_mock.display_country_leds = Mock()
        self._robot_controller_mock.ask_for_cube = Mock()
        self._robot_controller_mock.move_robot_to_localize_cube = Mock()

        self._cycle.start_cycle()

        calls = [call.ask_for_cube(flag_mock.return_value.next_cube()),
                 call.get_gripper(),
                 call.get_gripper().widest_gripper(),
                 call.move_robot_to_localize_cube()]

        self._robot_controller_mock.assert_has_calls(calls)
