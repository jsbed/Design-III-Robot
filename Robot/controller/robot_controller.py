from time import sleep

from Robot.controller.robot import Robot
from Robot.path_finding.point_adjustor import PointAdjustor
from Robot.configuration.config import Config
from Robot.controller.instructions.move import Move


class RobotController():

    def __init__(self):
        self._robot = Robot()
        self._adjustor = PointAdjustor()
        self._config = Config()

    def get_cube(self, cube):
        self._robot.update_localization()
        robot_position = self._robot.get_localization_position()
        robot_orientation = self._robot.get_localization_orientation()
        target_point = \
            self._adjustor.find_target_position(cube.get_localization().
                                                position, robot_position)
        next_point = self._adjustor.find_next_point(robot_position,
                                                    target_point)
        if (self.verify_distance(robot_position, next_point)):
            return True

        target_orientation = \
            self._adjustor.find_robot_orientation(robot_orientation,
                                                  next_point)
        self._robot.append_instruction(Move().move(next_point,
                                                   target_orientation))
        self._robot.execute_instructions()
        return False

    def move_cube(self, cube):
        self._robot.update_localization()
        robot_position = self._robot.get_localization_position()
        robot_orientation = self._robot.get_localization_orientation()
        target_point = \
            self._adjustor.find_target_position(cube.get_target_zone_position(),
                                                robot_position)
        next_point = self._adjustor.find_next_point(robot_position,
                                                    target_point)
        if (self.verify_distance(robot_position, next_point)):
            return True

        target_orientation = \
            self._adjustor.find_robot_orientation(robot_orientation,
                                                  next_point)
        self._robot.append_instruction(Move().move(next_point,
                                                   target_orientation))
        self._robot.execute_instructions()
        return False

    def get_question_from_atlas(self):
        # TODO: Show question led
        sleep(2)
        # Ask for question.
        question = ""
        return question

    def move_to_atlas(self):
        self._robot.update_localization()
        robot_position = self._robot.get_localization_position()
        robot_orientation = self._robot.get_localization_orientation()
        target_point = self._adjustor.find_next_point(robot_position,
                                                      self._config.
                                                      get_atlas_zone_position())
        if (self.verify_distance(robot_position, target_point)):
            return True

        target_orientation = \
            self._adjustor.find_robot_orientation(robot_orientation,
                                                  target_point)
        self._robot.append_instruction(Move().move(target_point,
                                                   target_orientation))
        self._robot.execute_instructions()
        return False

    def display_country_leds(self, country):
        # TODO: display country leds
        sleep(5)

    def ask_for_cube(self, cube):
        # TODO: display cube color led
        pass

    def verify_distance(self, start, end):
        distance = \
            self._adjustor.calculate_distance_between_points(start,
                                                             end)
        if (distance <= self._config.get_distance_uncertainty()):
            return True
        else:
            return False
