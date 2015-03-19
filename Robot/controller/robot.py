from Robot.locators.localization import Localization
from Robot.path_finding.point import Point


class Robot():

    def __init__(self, serial_port):
        self._localization = Localization(Point(0, 0), 0)
        self._serial_port = serial_port
        self._instructions = []

    def append_instruction(self, instruction):
        self._instructions.append(instruction)

    def execute_instructions(self):
        command = self._instructions.pop(0)
        command(self._serial_port)

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
