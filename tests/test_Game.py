import unittest

from game_state import GameState
from game import Game


class GameTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.game = Game()

    def test_next_state_for_get_country(self):
        test_next_state = GameState.GET_COUNTRY
        self.game.next_state()
        self.assertEqual(test_next_state, self.game.get_state())

    def test_construct_flag_for_canada(self):
        pass
