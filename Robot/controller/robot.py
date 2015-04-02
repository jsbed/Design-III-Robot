from Robot.communication.base_station_client import BaseStationClient
from Robot.locators.localization import Localization
from Robot.utilities.observable import Observable


FIRST_INSTRUCTION = 0
INSTRUCTION_FINISHED = "finished instruction"
SWITCH_ACTIVATED = "switch activated"
SWITCH_DEACTIVATED = "switch deactivated"


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
        print("execute:", command)
        command.execute(self._serial_port)
        self._serial_port.wait_for_read_line()
        #signal_message = self._serial_port.readline()
        print("instruction finished")
        # print(signal_message)
        # if (signal_message == "switch on"):
        #    self.notify(SWITCH_ACTIVATED, None)
        # elif (signal_message == "switch off"):
        #    self.notify(SWITCH_DEACTIVATED, None)
        self.notify(INSTRUCTION_FINISHED, None)

    def update_localization(self):
        print("requesting position")
        self._localization = BaseStationClient().request_robot_localization()
        print(self._localization.position, self._localization.orientation)

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
