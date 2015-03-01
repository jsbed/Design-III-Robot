from collections.__main__ import Point
import unittest

from Robot.controller.robot import Robot
from Robot.game_cycle.objects.color import Color
from Robot.game_cycle.objects.cube import Cube
from Robot.locators.localization import Localization
from Robot.path_finding.grid import SquareGrid
from Robot.path_finding.path_finder import PathFinder


class GameTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._cube = Cube(Color.RED, 0, False, Localization(Point(15, 18), 0))
        cls._grid = SquareGrid()
        cls._robot = Robot()
        cls._path_finder = PathFinder()

    def setUp(self):
        self._robot.set_localization_position(Point(1, 2))

    def test_get_cube(self):
        pass

    def test_move_cube(self):
        pass

    def test_get_question_from_atlas(self):
        pass

    def test_move_to_atlas(self):
        pass

    def test_display_country_leds(self):
        pass

    def test_ask_for_cube(self):
        pass
