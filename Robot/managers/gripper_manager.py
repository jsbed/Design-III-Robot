from Robot.configuration import config


class GripperManager():

    def __init__(self, serial_port):
        self._serial_port = serial_port

    def take_cube(self):
        self._serial_port.send_array_of_ints(
            config.Config().get_take_cube_gripper_values())

    def release_cube(self):
        self._serial_port.send_array_of_ints(
            config.Config().get_release_cube_gripper_values())

    def lift_gripper(self):
        self._serial_port.send_array_of_ints(
            config.Config().get_lift_gripper_values())

    def lower_gripper(self):
        self._serial_port.send_array_of_ints(
            config.Config().get_lower_gripper_values())

    def widest_gripper(self):
        self._serial_port.send_array_of_ints(
            config.Config().get_widest_gripper_values())
