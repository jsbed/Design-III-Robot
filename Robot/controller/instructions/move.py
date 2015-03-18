from Robot.controller.robot_instruction import RobotInstruction
import serial


class Move(RobotInstruction):
    def move(self, distance_cm):
        self._distance_mm = (distance_cm * 10)

    def execute(self, serial_port):
        self._serial_port = serial.Serial(serial_port)
        command = self._format_distance_to_string()
        self._serial_port.write(command.encode())

    def _format_distance_to_string(self):
        if (self._distance_mm < 0):
            formated_string = "BA"
            self._distance_mm = abs(self._distance_mm)
        else:
            formated_string = "GO"

        distance_string = str(self._distance_mm)

        while(len(distance_string) < 9):
            distance_string = "0" + distance_string

        formated_string += distance_string
        return formated_string
