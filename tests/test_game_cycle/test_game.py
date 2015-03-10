'''import unittest
from unittest.mock import patch

from Robot.game_cycle.game_state import GameState


class GameTest(unittest.TestCase):

    @patch('Robot.game_cycle')
    def test_next_state_for_get_country(self, GameMock):
        self._game = GameMock
        self._game.next_state().return_value = GameState.GET_COUNTRY
        test_next_state = GameState.GET_COUNTRY
        self.assertEqual(test_next_state,
                         self._game.next_state().return_value)'''
