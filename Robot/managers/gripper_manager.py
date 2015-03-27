import time

from Robot.configuration import config


CERVO_POSITION_INDEX = 3
ADJUSTEMENT_INDEX = 4


class GripperManager():

    def __init__(self, serial_port):
        self._serial_port = serial_port

    def take_cube(self):
        array_of_ints = config.Config().get_take_cube_gripper_values()

        self._serial_port.send_array_of_ints(array_of_ints[:4])
        self._send_adjustment(array_of_ints[:4], array_of_ints[4])

    def release_cube(self):
        array_of_ints = config.Config().get_release_cube_gripper_values()

        self._serial_port.send_array_of_ints(array_of_ints[:4])
        self._send_adjustment(array_of_ints[:4], array_of_ints[4])

    def lift_gripper(self):
        array_of_ints = config.Config().get_lift_gripper_values()

        self._serial_port.send_array_of_ints(array_of_ints[:4])
        self._send_adjustment(array_of_ints[:4], array_of_ints[4])

    def lower_gripper(self):
        array_of_ints = config.Config().get_lower_gripper_values()

        self._serial_port.send_array_of_ints(array_of_ints[:4])
        self._send_adjustment(array_of_ints[:4], array_of_ints[4])

    def widest_gripper(self):
        array_of_ints = config.Config().get_widest_gripper_values()

        self._serial_port.send_array_of_ints(array_of_ints[:4])
        self._send_adjustment(array_of_ints[:4], array_of_ints[4])

    def _send_adjustment(self, array, value):
        if value != 0:
            time.sleep(1)
            array[CERVO_POSITION_INDEX] += value
            self._serial_port.send_array_of_ints(array)
