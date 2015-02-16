import unittest

from Robot.grid import SquareGrid
from Robot.robot import Robot
from Robot.path_finder import PathFinder
from cube import Cube
from localization import Localization
from color import Color
from collections.__main__ import Point


class GameTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._cube = Cube(Color.RED, 0, False, Localization((15, 18), 0))
        cls._grid = SquareGrid(20, 20)

    def setUp(self):
        self._robot = Robot()
        self._path_finder = PathFinder()
        self._robot.set_localization_position(Point(1, 2))

    def test_get_cube_path(self):
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
