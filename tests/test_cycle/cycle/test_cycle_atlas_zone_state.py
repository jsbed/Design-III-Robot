from unittest.mock import MagicMock, Mock, patch
import unittest
from Robot.cycle.cycle import Cycle


class CycleTestAtlasZoneState(unittest.TestCase):

    @patch('Robot.cycle.cycle.RobotController')
    def setUp(self, robot_controller_mock):
        robot_controller_mock.return_value = MagicMock()
        self._robot_controller_mock = robot_controller_mock.return_value
        self._robot_controller_mock.get_robot = Mock()

        self._cycle = Cycle()

    def test_atlas_zone_state_when_robot_is_not_at_zone_atlas_then_move_to_atlas_is_called(self):
        self._robot_controller_mock.arrived_at_zone_atlas = Mock(
            return_value=False)
        self._robot_controller_mock.move_to_atlas = Mock()

        self._cycle.start_cycle()

        assert self._robot_controller_mock.move_to_atlas.called

    @patch('Robot.cycle.cycle.FlagCreator')
    @patch('Robot.cycle.cycle.QuestionAnalyser')
    @patch('Robot.cycle.cycle.CountryRepository')
    @patch('Robot.cycle.cycle.BaseStationClient')
    def test_atlas_zone_state_when_robot_is_at_zone_atlas_then_get_question_from_atlas_is_called(
            self, base_station_client_mock, country_mock, question_mock,
            flag_mock):
        base_station_client_mock.return_value = MagicMock()
        base_station_client_mock.return_value.send_question = Mock()
        base_station_client_mock.return_value.send_country = Mock()
        country_mock.return_value.return_value = MagicMock()
        country_mock.return_value.get = Mock()
        question_mock.return_value.return_value = MagicMock()
        question_mock.return_value.answer_question = Mock()
        self._robot_controller_mock.arrived_at_zone_atlas = Mock(
            return_value=True)
        self._robot_controller_mock.get_question_from_atlas = Mock()

        self._cycle.start_cycle()

        assert self._robot_controller_mock.get_question_from_atlas.called
