import time

from Robot.communication.base_station_client import BaseStationClient
from Robot.communication.serial_port import SerialPort
from Robot.configuration import config
from Robot.controller.instructions.move import Move
from Robot.controller.instructions.rotate import Rotate
from Robot.controller.robot import Robot
from Robot.cycle import atlas
from Robot.managers.led_manager import LedManager
from Robot.path_finding.point_adjustor import PointAdjustor


FULL_ROTATION = 360
ANGLE_DIFFERENCE_NULL = 0
FACE_NORTH = 0


class RobotController():

    def __init__(self):
        self._serial_port = SerialPort(
            config.Config().get_stm_serial_port_path(),
            baudrate=config.Config().get_stm_serial_port_baudrate(),
            timeout=config.Config().get_stm_serial_port_timeout())

        self._robot = Robot(self._serial_port)
        self._point_adjustor = PointAdjustor()
        self._led_manager = LedManager(self._serial_port)
        
    def get_robot(self):
        return self._robot

    def get_question_from_atlas(self):
        self._led_manager.display_red_led()
        time.sleep(config.Config().get_red_led_wait_time())
        self._led_manager.close_red_led()

        return atlas.get_question()

    def arrived_at_zone_atlas(self):
        self._update_robot_localization()
        target_point = config.Config().get_atlas_zone_position()
        self._distance = \
            self._point_adjustor. \
            _calculate_distance_between_points(self._robot_position,
                                               target_point)

        return self._robot_is_next_to_target_point()

    def move_to_atlas(self):
        self._update_robot_localization()
        target_point = config.Config().get_atlas_zone_position()
        self._distance = \
            self._point_adjustor. \
            _calculate_distance_between_points(self._robot_position,
                                               target_point)

        self._move_robot_towards_target_point(target_point)
        self._send_new_path(config.Config().get_atlas_zone_position())

    def display_country_leds(self, country):
        self._led_manager.display_country(country)
        time.sleep(config.Config().get_display_country_wait_time())
        self._led_manager.close_leds()

    def ask_for_cube(self, cube):
        self._led_manager.next_flag_led(cube)

    def robot_is_next_to_target_with_correct_orientation(self, target):
        self._update_robot_localization()
        next_point = self._find_next_destination_point(target)
        self._distance = self._point_adjustor. \
            _calculate_distance_between_points(self._robot_position,
                                               next_point)

        return (self._robot_is_next_to_target_point() and
                self._robot_has_correct_orientation(target))

    def move_robot_to(self, destination):
        self._update_robot_localization()
        next_point = self._find_next_destination_point(destination)
        self._distance = \
            self._point_adjustor. \
            _calculate_distance_between_points(self._robot_position,
                                               next_point)
        print(next_point)
        self._move_robot_towards_target_point(next_point)
        self._send_new_path(next_point)

    def move_robot_to_localize_cube(self):
        self._update_robot_localization()
        self._distance = \
            self._point_adjustor. \
            _calculate_distance_between_points(self._robot_position,
                                               config.Config().
                                               get_localize_cube_position())
        target_orientation = self._point_adjustor.find_robot_orientation(
            self._robot_orientation,
            self._robot_position,
            config.Config().get_localize_cube_position())

        if (abs(target_orientation) > config.Config().get_orientation_max()):
            self._robot.append_instruction(
                Rotate(config.Config().get_orientation_max()))
            self._robot.append_instruction(
                Rotate(target_orientation -
                       config.Config().get_orientation_max()))
        else:
            self._robot.append_instruction(Rotate(target_orientation))
        self._robot.append_instruction(Move(self._distance))
        rotation = FACE_NORTH - target_orientation - self._robot_orientation
        if (abs(rotation) > config.Config().get_orientation_max()):
            self._robot.append_instruction(
                Rotate(config.Config().get_orientation_max()))
            self._robot.append_instruction(
                Rotate(rotation -
                       config.Config().get_orientation_max()))
        else:
            self._robot.append_instruction(Rotate(rotation))
        self._robot.execute_instructions()
        self._send_new_path(config.Config().get_localize_cube_position())

    def push_cube(self):
        self._robot.append_instruction(Move(config.Config().
                                            get_push_cube_distance()))
        self._robot.execute_instructions()

    def move_forward_to_target_zone(self):
        self._robot.append_instruction(Move(config.Config().
                                            get_distance_between_objects()))
        self._robot.execute_instructions()

    def move_backward_from_target_zone(self):
        self._robot.append_instruction(Move(-(config.Config().
                                              get_distance_between_objects())))
        self._robot.execute_instructions()

    def instruction_remaining(self):
        return len(self._robot.get_instructions()) > 0

    def next_instruction(self):
        self._robot.execute_instructions()

    def _update_robot_localization(self):
        self._robot.update_localization()
        self._robot_position = self._robot.get_localization_position()
        self._robot_orientation = \
            self._robot.get_localization_orientation()

    def _find_next_destination_point(self, destination):
        target_point = \
            self._point_adjustor.find_target_position(destination,
                                                      self._robot_position)
        next_point = self._point_adjustor.find_next_point(self._robot_position,
                                                          target_point)
        return next_point

    def _robot_has_correct_orientation(self, destination):
        target_orientation = self._point_adjustor.find_robot_orientation(
            self._robot_orientation, self._robot_position, destination)

        if (self._robot_is_facing_correct_angle(target_orientation)):
            return True
        else:
            if (abs(target_orientation) >
                    config.Config().get_orientation_max()):
                self._robot.append_instruction(
                    Rotate(config.Config().get_orientation_max()))
                self._robot.append_instruction(
                    Rotate(target_orientation -
                           config.Config().get_orientation_max()))
            else:
                self._robot.append_instruction(Rotate(target_orientation))
            self._robot.execute_instructions()
            return False

    def _move_robot_towards_target_point(self, destination):
        target_orientation = self._point_adjustor.find_robot_orientation(
            self._robot_orientation,
            self._robot_position,
            destination)

        if (abs(target_orientation) > config.Config().get_orientation_max()):
            self._robot.append_instruction(
                Rotate(config.Config().get_orientation_max()))
            self._robot.append_instruction(
                Rotate(target_orientation -
                       config.Config().get_orientation_max()))
        else:
            self._robot.append_instruction(Rotate(target_orientation))
        self._robot.append_instruction(Move(self._distance))
        self._robot.execute_instructions()
        

    def _send_new_path(self, target_point):
        path = [target_point.x, target_point.y]
        BaseStationClient().send_path(path)

    def _robot_is_next_to_target_point(self):
        return self._distance <= config.Config().get_distance_uncertainty()

    def _robot_is_facing_correct_angle(self, angle_difference):
        angle_uncertainty = (FULL_ROTATION -
                             config.Config().get_orientation_uncertainty())

        if ((angle_difference >= angle_uncertainty)
                or (angle_difference <= -angle_uncertainty)):
            angle_difference = ANGLE_DIFFERENCE_NULL

        angle_uncertainty = config.Config().get_orientation_uncertainty()

        return (angle_difference <= angle_uncertainty and
                angle_difference >= -angle_uncertainty)
