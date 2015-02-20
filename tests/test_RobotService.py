import unittest

from Robot.robot.grid import SquareGrid
from Robot.robot.robot import Robot
from Robot.robot.path_finder import PathFinder
from Robot.cube import Cube
from Robot.localization import Localization
from Robot.color import Color
from collections.__main__ import Point


class GameTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._cube = Cube(Color.RED, 0, False, Localization(Point(15, 18), 0))
        cls._grid = SquareGrid()
        cls._robot = Robot()
        cls._path_finder = PathFinder()

    def setUp(self):
        self._robot.set_localization_position(Point(1, 2))

    def test_path_finder(self):
        path_test = [(15, 18), (14, 18), (13, 18), (12, 18), (11, 18),
                     (10, 18), (9, 18), (8, 18), (7, 18), (6, 18), (5, 18),
                     (4, 18), (3, 18), (2, 18), (1, 18), (1, 17), (1, 16),
                     (1, 15), (1, 14), (1, 13), (1, 12), (1, 11), (1, 10),
                     (1, 9), (1, 8), (1, 7), (1, 6), (1, 5), (1, 4), (1, 3),
                     (1, 2)]
        path = self._path_finder.a_star_search(
            self._grid,
            self._robot.get_localization().position,
            self._cube.get_localization().position)
        self.assertEqual(path_test, path)

    def test_construct_flag_for_canada(self):
        pass
