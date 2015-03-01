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
        cls._cube = Cube(Color.RED, 0, False, Localization(Point(0, 0), 0))
        cls._grid = SquareGrid()
        cls._robot = Robot()
        cls._path_finder = PathFinder()

    def setUp(self):
        self._robot.set_localization_position(Point(50, 50))

    def path_finder(self, path_test):
        path = self._path_finder.find_path(
            self._robot.get_localization().position,
            self._cube.get_localization().position)
        self.assertEqual(path_test, path)

    def test_top_right(self):
        path_test = [Point(x=55, y=60), Point(x=55, y=59), Point(x=55, y=58),
                     Point(x=55, y=57), Point(x=55, y=56), Point(x=55, y=55),
                     Point(x=54, y=54), Point(x=53, y=53), Point(x=52, y=52),
                     Point(x=51, y=51), Point(x=50, y=50)]
        self._cube.set_localization_position(Point(55, 60))
        self.path_finder(path_test)

    def test_top_left(self):
        path_test = [Point(x=45, y=60), Point(x=45, y=59), Point(x=45, y=58),
                     Point(x=45, y=57), Point(x=45, y=56), Point(x=45, y=55),
                     Point(x=46, y=54), Point(x=47, y=53), Point(x=48, y=52),
                     Point(x=49, y=51), Point(x=50, y=50)]
        self._cube.set_localization_position(Point(45, 60))
        self.path_finder(path_test)

    def test_bottum_right(self):
        path_test = [Point(x=60, y=45), Point(x=59, y=45), Point(x=58, y=45),
                     Point(x=57, y=45), Point(x=56, y=45), Point(x=55, y=45),
                     Point(x=54, y=46), Point(x=53, y=47), Point(x=52, y=48),
                     Point(x=51, y=49), Point(x=50, y=50)]
        self._cube.set_localization_position(Point(60, 45))
        self.path_finder(path_test)

    def test_bottum_left(self):
        path_test = [Point(x=40, y=45), Point(x=41, y=45), Point(x=42, y=45),
                     Point(x=43, y=45), Point(x=44, y=45), Point(x=45, y=45),
                     Point(x=46, y=46), Point(x=47, y=47), Point(x=48, y=48),
                     Point(x=49, y=49), Point(x=50, y=50)]
        self._cube.set_localization_position(Point(40, 45))
        self.path_finder(path_test)

    def test_left(self):
        path_test = [Point(x=40, y=50), Point(x=41, y=50), Point(x=42, y=50),
                     Point(x=43, y=50), Point(x=44, y=50), Point(x=45, y=50),
                     Point(x=46, y=50), Point(x=47, y=50), Point(x=48, y=50),
                     Point(x=49, y=50), Point(x=50, y=50)]
        self._cube.set_localization_position(Point(40, 50))
        self.path_finder(path_test)

    def test_right(self):
        path_test = [Point(x=60, y=50), Point(x=59, y=50), Point(x=58, y=50),
                     Point(x=57, y=50), Point(x=56, y=50), Point(x=55, y=50),
                     Point(x=54, y=50), Point(x=53, y=50), Point(x=52, y=50),
                     Point(x=51, y=50), Point(x=50, y=50)]
        self._cube.set_localization_position(Point(60, 50))
        self.path_finder(path_test)

    def test_up(self):
        path_test = [Point(x=50, y=55), Point(x=50, y=54), Point(x=50, y=53),
                     Point(x=50, y=52), Point(x=50, y=51), Point(x=50, y=50)]
        self._cube.set_localization_position(Point(50, 55))
        self.path_finder(path_test)

    def test_down(self):
        path_test = [Point(x=50, y=45), Point(x=50, y=46), Point(x=50, y=47),
                     Point(x=50, y=48), Point(x=50, y=49), Point(x=50, y=50)]
        self._cube.set_localization_position(Point(50, 45))
        self.path_finder(path_test)
