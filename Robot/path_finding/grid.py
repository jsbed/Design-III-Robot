from Robot.configuration.config import Config


class SquareGrid:
    def __init__(self):
        self._table_width = Config().get_table_width()
        self._table_height = Config().get_table_height()
        self._robot_radius = Config().get_robot_radius()
        self._cube_radius = Config().get_cube_radius()
        self._atlas_zone_position = Config().get_atlas_zone_position()

    def get_width(self):
        return self._table_width

    def get_height(self):
        return self._table_height

    def get_robot_radius(self):
        return self._robot_radius

    def get_cube_radius(self):
        return self._cube_radius

    def get_atlas_zone_position(self):
        return self._atlas_zone_position
