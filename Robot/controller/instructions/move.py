from Robot.controller.robot_instruction import RobotInstruction


class Move(RobotInstruction):
    def move(self, target, angle):
        self._target = target
        self._angle = angle

    def execute(self):
        pass
