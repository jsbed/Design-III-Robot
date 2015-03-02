import unittest
from unittest.mock import patch, Mock, MagicMock

from Robot.game_cycle.atlas import get_question


AN_IP_ARGUMENT = "127.0.0.1"


class TestAtlas(unittest.TestCase):

    def _setup_config_mock(self, mock):
        a_mock = MagicMock()
        a_mock.get_atlas_url = Mock(return_value=AN_IP_ARGUMENT)
        mock.return_value = a_mock

    @patch("requests.get")
    @patch("Robot.game_cycle.atlas.config.Config")
    def test_question_request_arguments(self, ConfigMock, RequestMock):
        self._setup_config_mock(ConfigMock)
        get_question()

        RequestMock.assert_called_with(AN_IP_ARGUMENT, verify=False)
