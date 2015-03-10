from Robot.locators.localization import Localization
from Robot.path_finding.point import Point


class Robot():

    def __init__(self):
        self._localization = Localization(Point(0, 0), 0)
        self._insturctions = []

    def append_instruction(self, instruction):
        self._insturctions.append(instruction)

    def execute_instructions(self):
        for i in self._insturctions:
            self._insturctions[i].execute()
            self._insturctions.remove(i)

    def update_localization(self):
        pass

    def set_localization_position(self, value):
        self._localization.position = value

    def get_localization_position(self):
        return self._localization.position

    def get_localization_orientation(self):
        return self._localization.orientation

    def get_localization(self):
        return self._localization
