from math import floor

from Robot.configuration import config
from Robot.game_cycle.objects.color import Color
from Robot.game_cycle.objects.cube import Cube
from Robot.path_finding.point import Point


CUBE_INDEX_ORDER = [6, 7, 8, 3, 4, 5, 0, 1, 2]


class FlagCreator:

    def __init__(self, country):
        self._cube_order = []
        self._country = country
        self._fill_cube_order()

    # Finds the cubes' location in the target zone using the optimal cube
    # selection order to form a flag
    def _fill_cube_order(self):
        cube_radius = config.Config().get_cube_radius()
        cube_distance = config.Config().get_cube_center_distance()
        creation_zone = config.Config().get_flag_creation_zone_position()
        target_zone_position = config.Config().get_target_zone_position()

        for cube_index in reversed(CUBE_INDEX_ORDER):
            flag_color = self._country.flag[cube_index]

            if flag_color != Color.NONE:
                x = target_zone_position.x - creation_zone.x - \
                    cube_radius - (cube_index % 3) * cube_distance
                y = target_zone_position.y - creation_zone.y + \
                    cube_radius + (2 - floor(cube_index / 3)) * cube_distance
                self._cube_order.append(Cube(flag_color, Point(x, y)))

    def has_next_cubes(self):
        return len(self._cube_order) > 0

    def next_cube(self):
        if (self.has_next_cubes()):
            return self._cube_order.pop()
        else:
            Exception("The cube queue is empty.")
