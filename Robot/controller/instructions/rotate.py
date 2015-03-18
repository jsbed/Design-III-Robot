from Robot.controller.robot_instruction import RobotInstruction
import serial


class Rotate(RobotInstruction):
    def rotate(self, angle):
        self._angle = angle

    def execute(self, serial_port):
        self._serial_port = serial.Serial(serial_port)
        command = self._format_angle_to_string()
        self._serial_port.write(command.encode())

    def _format_angle_to_string(self):
        if (self._angle < 0):
            formated_string = "RO"  # ****Need command for negative angle****
            self._angle = abs(self._angle)
        else:
            formated_string = "RO"

        angle_string = str(self._angle)

        while(len(angle_string) < 9):
            angle_string = "0" + angle_string

        formated_string += angle_string
        return formated_string
