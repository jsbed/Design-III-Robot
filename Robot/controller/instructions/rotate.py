from Robot.controller.robot_instruction import RobotInstruction
import serial

NUMBER_OF_BYTES = 8
EMPTY_BYTE = "0"
CLOCKWISE_ROTATION = "ROR"
ANTICLOCKWISE_ROTATION = "ROL"


class Rotate(RobotInstruction):
    def rotate(self, angle):
        self._angle = angle

    def execute(self, serial_port):
        self._serial_port = serial.Serial(serial_port)
        command = self._format_angle_to_string()
        self._serial_port.write(command.encode())

    def _format_angle_to_string(self):
        if (self._angle < 0):
            formated_string = CLOCKWISE_ROTATION
            self._angle = abs(self._angle)

        else:
            formated_string = ANTICLOCKWISE_ROTATION

        angle_string = str(self._angle)

        while(len(angle_string) < NUMBER_OF_BYTES):
            angle_string = EMPTY_BYTE + angle_string

        formated_string += angle_string

        return formated_string
