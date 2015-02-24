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
        self._walls = []

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

    def in_bounds(self, grid_id):
        (x, y) = grid_id
        return 0 <= x < self._width and 0 <= y < self._height

    def passable(self, grid_id):
        return id not in self._walls

    def neighbors(self, grid_id):
        (x, y) = grid_id
        results = [(x+1, y), (x, y-1), (x-1, y), (x, y+1)]
        if (x + y) % 2 == 0:
            results.reverse()
        results = filter(self.in_bounds, results)
        results = filter(self.passable, results)
        return results
