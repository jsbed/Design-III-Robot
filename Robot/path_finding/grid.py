from collections.__main__ import Point

ROBOT_RADIUS = 11
CUBE_RADIUS = 4
TABLE_WIDTH = 111
TABLE_HEIGHT = 251
ATLAS_ZONE_POSITION = Point(0, 0)


class SquareGrid:
    def __init__(self):
        self._width = TABLE_WIDTH
        self._height = TABLE_HEIGHT
        self._robot_radius = ROBOT_RADIUS
        self._cube_radius = CUBE_RADIUS
        self._atlas_zone_position = ATLAS_ZONE_POSITION

    def get_width(self):
        return self._width

    def get_height(self):
        return self._height

    def get_robot_radius(self):
        return self._robot_radius

    def get_cube_radius(self):
        return self._cube_radius

    def get_atlas_zone_position(self):
        return self._atlas_zone_position
