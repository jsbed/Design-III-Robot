from Robot.controller.robot_instruction import RobotInstruction


class Rotate(RobotInstruction):
    def rotate(self, angle):
        self._angle = angle

    def execute(self):
        print("Execute rotation " + self._angle + "°")
