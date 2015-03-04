from Robot.configuration.config import Config
from Robot.game_cycle.objects.color import Color

X_INDEX = 0
Y_INDEX = 1

CUBE_INDEX_ORDER = [6, 7, 8, 3, 4, 5, 0, 1, 2]


class FlagCreator:

    def __init__(self, country):
        self._has_next_cubes = True
        self._cube_order = []
        self._creation_zone_height = 0
        self._creation_zone_width = 0
        self._target_zone_position = Config().get_target_zone_position()
        self._cube_radius = Config().get_cube_radius()
        self._country = country

        for cube_index in CUBE_INDEX_ORDER:
            country.flag
            if color != Color.NONE:
                self._cube_order.append(color)

    def get_has_next_cubes(self):
        return len(self._cube_order) > 0

    def get_cube_order(self):
        return self._cube_order

    def get_creation_zone_height(self):
        return self._creation_zone_height

    def get_creation_zone_width(self):
        return self._creation_zone_width

    def get_country(self):
        return self._country

    def next_cube(self):
        try:
            next_cube = self._cube_order.pop()
            if not self._cube_order:
                self._has_next_cubes = False
            return next_cube
        except IndexError:
            self._has_next_cubes = False
            print("Cube order list is empty!")
