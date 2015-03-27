from Robot.configuration import config
import time

CERVO_POSITION_INDEX = 3


class GripperManager():

    def __init__(self, serial_port):
        self._serial_port = serial_port

    def take_cube(self):
        array_of_ints = config.Config().get_take_cube_gripper_values()

        self._serial_port.send_array_of_ints(array_of_ints)
        self._send_adjustment(array_of_ints, 0)

    def release_cube(self):
        array_of_ints = config.Config().get_release_cube_gripper_values()

        self._serial_port.send_array_of_ints(array_of_ints)
        self._send_adjustment(array_of_ints, -12)

    def lift_gripper(self):
        array_of_ints = config.Config().get_lift_gripper_values()

        self._serial_port.send_array_of_ints(array_of_ints)
        self._send_adjustment(array_of_ints, 2)

    def lower_gripper(self):
        array_of_ints = config.Config().get_lower_gripper_values()

        self._serial_port.send_array_of_ints(array_of_ints)
        self._send_adjustment(array_of_ints, -2)

    def widest_gripper(self):
        array_of_ints = config.Config().get_widest_gripper_values()

        self._serial_port.send_array_of_ints(array_of_ints)
        self._send_adjustment(array_of_ints, -12)

    def _send_adjustment(self, array, value):
        if value:
            time.sleep(1)
            array[CERVO_POSITION_INDEX] += value
            self._serial_port.send_array_of_ints(array)
