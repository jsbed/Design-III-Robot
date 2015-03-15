from time import sleep

from Robot.configuration import config
from Robot.controller.instructions.move import Move
from Robot.controller.robot import Robot
from Robot.game_cycle import atlas
from Robot.managers.led_manager import LedManager
from Robot.path_finding.point_adjustor import PointAdjustor


class RobotController():

    def __init__(self):
        self._robot = Robot()
        self._adjustor = PointAdjustor()
        self._led_manager = LedManager(None)

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
                                                  robot_position,
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
        self._led_manager.display_red_led()
        sleep(2)
        self._led_manager.close_red_led()
        return atlas.get_question()

    def move_to_atlas(self):
        self._robot.update_localization()
        robot_position = self._robot.get_localization_position()
        robot_orientation = self._robot.get_localization_orientation()
        target_point = self._adjustor.find_next_point(robot_position,
                                                      config.Config().
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
        self._led_manager.display_country(country)
        sleep(5)

    def ask_for_cube(self, cube):
        self._led_manager.next_flag_led(cube)

    def verify_distance(self, start, end):
        distance = \
            self._adjustor.calculate_distance_between_points(start,
                                                             end)
        if (distance <= config.Config().get_distance_uncertainty()):
            return True
        else:
            return False
