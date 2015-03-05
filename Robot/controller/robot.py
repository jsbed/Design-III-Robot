from Robot.locators.localization import Localization
from Robot.path_finding.point import Point


class Robot():

    def __init__(self):
        self._localization = Localization(Point(0, 0), 0)

    def set_localization_position(self, value):
        self._localization.position = value

    def get_localization(self):
        return self._localization
