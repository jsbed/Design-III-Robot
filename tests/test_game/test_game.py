import unittest

from Robot.game_cycle.game import Game
from Robot.game_cycle.game_state import GameState


class GameTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._game = Game()

    def setUp(self):
        pass

    def test_next_state_for_get_country(self):
        test_next_state = GameState.GET_COUNTRY
        self._game.next_state()
        self.assertEqual(test_next_state, self._game.get_state())

    def test_construct_flag_for_canada(self):
        pass
