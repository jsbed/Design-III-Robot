from Robot.path_finder import PathFinder
from Robot.robot import Robot
from collections.__main__ import Point
from time import sleep

ATLAS_ZONE_POSITION = Point(0, 0)


class RobotService():

    def __init__(self):
        self._robot = Robot()
        self._path_finder = PathFinder()
        self._path = []

    def get_cube(self, cube):
        self._path = self._path_finder.find_shortest_path(
            self._robot.get_localization().position,
            cube.get_localization().position)
        # TODO: Move the robot via the path

    def move_cube(self, cube):
        self._path = self._path_finder.find_shortest_path(
            self._robot.get_localization().position,
            cube.get_target_zone_position())
        # TODO: Move the robot via the path

    def get_question_from_atlas(self):
        self.move_to_atlas()
        # TODO: Show question led
        sleep(2)

    def move_to_atlas(self):
        self._path = self._path_finder.find_shortest_path
        (self._robot.get_localization().position, ATLAS_ZONE_POSITION)
        # TODO: Move the robot via the path

    def display_country_leds(self, country):
        # TODO: display country with led
        sleep(5)

    def ask_for_cube(self, cube):
        # TODO: Led Manager
        pass
