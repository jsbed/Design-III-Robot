from Robot.locators.localization import Localization
from Robot.path_finding.point import Point


class Cube:

    def __init__(self, color, target_zone_position, index=0):
        self._color = color
        self._target_zone_position = target_zone_position
        self._localization = Localization(Point(-1, -1), 0)
        self._index = index

    def set_localization_position(self, value):
        self._localization.position = value

    def get_target_zone_position(self):
        return self._target_zone_position

    def get_color(self):
        return self._color

    def get_localization(self):
        return self._localization

    def get_index(self):
        return self._index
