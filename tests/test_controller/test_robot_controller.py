import unittest

from Robot.controller.robot import Robot
from Robot.path_finding.path_finder import PathFinder
from Robot.path_finding.point import Point


class GameTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls._robot = Robot()
        cls._path_finder = PathFinder()

    def setUp(self):
        self._robot.set_localization_position(Point(1, 2))
