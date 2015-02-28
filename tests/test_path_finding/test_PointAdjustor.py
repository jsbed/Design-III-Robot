from collections.__main__ import Point
import unittest

from Robot.controller.robot import Robot
from Robot.game_cycle.objects.color import Color
from Robot.game_cycle.objects.cube import Cube
from Robot.locators.localization import Localization
from Robot.path_finding.grid import SquareGrid
from Robot.path_finding.point_adjustor import PointAdjustor


class GameTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._cube = Cube(Color.RED, 0, False, Localization(Point(0, 0), 0))
        cls._robot = Robot()
        cls._grid = SquareGrid()

    def setUp(self):
        self._robot.set_localization_position(Point(50, 50))
        self._point_test = Point(0, 0)

    def adjustor(self):
        self._adjustor = PointAdjustor(self._grid)
        point = self._adjustor.find_target_position(self.
                                                    _cube.get_localization().
                                                    position,
                                                    self._robot.
                                                    get_localization().
                                                    position)
        self.assertEqual(self._point_test, point)

    def test_west_wall(self):
        self._point_test = Point(18, 50)
        self._cube.set_localization_position(Point(3, 50))
        self.adjustor()

    def test_east_wall(self):
        self._point_test = Point(95, 30)
        self._cube.set_localization_position(Point(110, 30))
        self.adjustor()

    def test_north_wall(self):
        self._point_test = Point(50, 236)
        self._cube.set_localization_position(Point(50, 251))
        self.adjustor()

    def test_south_wall(self):
        self._point_test = Point(80, 23)
        self._cube.set_localization_position(Point(80, 8))
        self.adjustor()

    def test_first_quadrant(self):
        self._point_test = Point(55, 70)
        self._cube.set_localization_position(Point(70, 70))
        self.adjustor()

    def test_second_quadrant(self):
        self._point_test = Point(33, 55)
        self._cube.set_localization_position(Point(33, 70))
        self.adjustor()

    def test_third_quadrant(self):
        self._point_test = Point(21, 30)
        self._cube.set_localization_position(Point(21, 15))
        self.adjustor()

    def test_fourth_quadrant(self):
        self._point_test = Point(55, 15)
        self._cube.set_localization_position(Point(70, 15))
        self.adjustor()

    def test_tight_spot(self):
        self._point_test = Point(35, 60)
        self._cube.set_localization_position(Point(20, 60))
        self.adjustor()
