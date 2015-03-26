from Robot.locators.localization import Localization
from Robot.utilities.observable import Observable

FIRST_INSTRUCTION = 0
INSTRUCTION_FINISHED = "finished instruction"


class Robot(Observable):

    def __init__(self, serial_port):
        Observable.__init__(self)
        self._localization = Localization(None, None, unknown=True)
        self._serial_port = serial_port
        self._instructions = []

    def append_instruction(self, instruction):
        self._instructions.append(instruction)

    def execute_instructions(self):
        command = self._instructions.pop(FIRST_INSTRUCTION)
        command.execute(self._serial_port)
        self._serial_port.wait_for_read_line()
        self.notify(INSTRUCTION_FINISHED, None)

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

    def get_instructions(self):
        return self._instructions
