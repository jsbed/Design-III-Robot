import math
import time

from Robot.communication.base_station_client import BaseStationClient
from Robot.communication.serial_port import SerialPort
from Robot.configuration import config
from Robot.controller.instructions.lateral import Lateral
from Robot.controller.instructions.move import Move
from Robot.controller.instructions.rotate import Rotate
from Robot.controller.robot import Robot
from Robot.cycle import atlas
from Robot.managers.gripper_manager import GripperManager
from Robot.managers.led_manager import LedManager
from Robot.path_finding.point_adjustor import PointAdjustor


LOCALIZE_CUBE_ANGLE = 0
CUBE_RELEASE_ANGLE = 180


class RobotController():

    def __init__(self):
        self._stm_serial_port = SerialPort(
            config.Config().get_stm_serial_port_path(),
            baudrate=config.Config().get_stm_serial_port_baudrate(),
            timeout=config.Config().get_stm_serial_port_timeout())

        self._pololu_serial_port = SerialPort(
            config.Config().get_pololu_serial_port_path())

        self._robot = Robot(self._stm_serial_port)
        self._led_manager = LedManager(self._stm_serial_port)
        self._gripper_manager = GripperManager(self._pololu_serial_port)
        self._switch = 0

    def get_robot(self):
        return self._robot

    def get_gripper(self):
        return self._gripper_manager

    def get_question_from_atlas(self):
        self._led_manager.display_red_led()
        time.sleep(config.Config().get_red_led_wait_time())
        self._led_manager.close_red_led()

        return atlas.get_question()

    def arrived_at_zone_atlas(self):
        self._update_robot_localization()
        self._distance = PointAdjustor(). \
            calculate_distance_between_points(self._robot_position,
                                              config.Config().
                                              get_atlas_zone_position())

        return self._robot_is_next_to_atlas()

    def move_to_atlas(self):
        self._update_robot_localization()
        atlas_zone_position = config.Config().get_atlas_zone_position()
        self._distance = PointAdjustor(). \
            calculate_distance_between_points(self._robot_position,
                                              atlas_zone_position)

        self._move_robot_towards_target_point(atlas_zone_position)
        self._robot.execute_instructions()

    def display_country_leds(self, country):
        self._led_manager.display_country(country)
        time.sleep(config.Config().get_display_country_wait_time())
        self._led_manager.close_leds()

    def ask_for_cube(self, cube):
        self._led_manager.display_flag_led_for_next_cube(cube)

    def robot_is_next_to_target_with_correct_orientation(self, target):
        self._update_robot_localization()
        target_point = self._find_next_destination_point(target)
        self._distance = PointAdjustor(). \
            calculate_distance_between_points(self._robot_position,
                                              target_point)

        return (self._robot_is_next_to_target_point() and
                self._robot_has_correct_orientation(target))

    def move_robot_to(self, destination):
        self._update_robot_localization()
        destination_point = self._find_next_destination_point(destination)
        self._distance = PointAdjustor(). \
            calculate_distance_between_points(self._robot_position,
                                              destination_point)
        self._move_robot_towards_target_point(destination_point)
        self._robot.execute_instructions()

    def move_robot_to_localize_cube(self):
        self._update_robot_localization()
        localization_position = config.Config().get_localize_cube_position()
        self._distance = PointAdjustor(). \
            calculate_distance_between_points(self._robot_position,
                                              localization_position)
        rotation = LOCALIZE_CUBE_ANGLE - \
            PointAdjustor().find_robot_rotation(LOCALIZE_CUBE_ANGLE,
                                                self._robot_position,
                                                localization_position)
        self._move_robot_towards_target_point(localization_position)
        self._append_rotations(rotation)
        self._robot.execute_instructions()

    def turn_switch_on(self):
        self._switch += 1

    def turn_switch_off(self):
        self._switch -= 1

    def get_switch_status(self):
        return self._switch >= config.Config().get_number_of_switches()

    def push_cube(self, cube_position):
        self._update_robot_localization()
        self._distance = PointAdjustor(). \
            calculate_distance_between_points(self._robot_position,
                                              cube_position)
        self._distance -= (config.Config().get_gripper_size() +
                           config.Config().get_cube_radius() +
                           config.Config().get_robot_radius())
        if (self._robot_is_next_to_cube()):
            self.move_backward()
        else:
            print("pushing")
            rotation = PointAdjustor().find_robot_rotation(
                self._robot_orientation, self._robot_position,
                cube_position)
            self._append_rotations(rotation)
            wall_distance = \
                PointAdjustor().\
                calculate_distance_between_cube_and_closest_wall(cube_position)
            print("Distance from wall :", wall_distance)
            push_distance = config.Config().get_push_cube_distance()
            if (push_distance > self._distance + wall_distance +
                    config.Config().get_cube_radius()):
                push_distance = (self._distance + wall_distance +
                                 config.Config().get_cube_radius())
            self._robot.append_instruction(Move(push_distance))
            self._robot.execute_instructions()

    def move_forward_to_target_zone(self, target_zone_position):
        print("MOVING TORWARD ", target_zone_position)

        self._update_robot_localization()

        rotation = -PointAdjustor().find_robot_rotation(
            CUBE_RELEASE_ANGLE, self._robot_position, target_zone_position)
        print("Rotation ", rotation)
        self._append_rotations(rotation)
        lateral_distance = target_zone_position.x - self._robot_position.x
        if (lateral_distance > config.Config().get_distance_min() or
                lateral_distance < -config.Config().get_distance_min()):
            self._robot.append_instruction(Lateral(lateral_distance))
        self._robot.append_instruction(
            Move(self._robot_position.y - target_zone_position.y -
                 config.Config().get_gripper_size() -
                 config.Config().get_cube_radius() -
                 config.Config().get_robot_radius()))
        self._robot.execute_instructions()

    def move_backward(self):
        self._robot.append_instruction(Move((config.Config().
                                             get_move_backward_distance())))
        self._robot.execute_instructions()

    def instruction_remaining(self):
        return len(self._robot.get_instructions()) > 0

    def next_instruction(self):
        self._robot.execute_instructions()

    def end_cycle(self):
        self._led_manager.display_red_led()

    def _update_robot_localization(self):
        time.sleep(3)
        self._robot.update_localization()
        self._robot_position = self._robot.get_localization_position()
        self._robot_orientation = self._robot.get_localization_orientation()

    def _find_next_destination_point(self, destination):
        target_point = PointAdjustor().find_target_position(
            destination, self._robot_position)
        print("target point", target_point)
        next_point = PointAdjustor().find_next_point(self._robot_position,
                                                     target_point)
        print("next pint", next_point)
        return next_point

    def _robot_has_correct_orientation(self, destination):
        rotation = PointAdjustor().find_robot_rotation(
            self._robot_orientation, self._robot_position, destination)
        print("Adjust rotation", rotation)

        if not(self._robot_is_facing_correct_angle(rotation)):
            self._append_rotations(rotation)
            self._robot.execute_instructions()
        return self._robot_is_facing_correct_angle(rotation)

    def _move_robot_towards_target_point(self, destination):
        print("destination", destination)
        rotation = PointAdjustor().find_robot_rotation(
            self._robot_orientation, self._robot_position, destination)
        self._append_rotations(rotation)
        if (self._distance >= config.Config().get_distance_min()):
            self._robot.append_instruction(Move(self._distance))
        self._send_new_path(destination)

    def _send_new_path(self, target_point):
        path = [target_point.x, target_point.y]
        BaseStationClient().send_path(path)

    def _robot_is_next_to_atlas(self):
        return self._distance <= \
            config.Config().get_atlas_distance_uncertainty()

    def _robot_is_next_to_target_point(self):
        print("Distance between objects :", self._distance)
        return self._distance <= config.Config().get_distance_uncertainty()

    def _robot_is_next_to_cube(self):
        print("Distance between objects :", self._distance)
        return self._distance <= config.Config().\
            get_distance_uncertainty_with_cube()

    def _robot_is_facing_correct_angle(self, rotation):
        angle_uncertainty = config.Config().get_orientation_uncertainty()

        return (rotation <= angle_uncertainty and
                rotation >= -angle_uncertainty)

    def _append_rotations(self, rotation):
        orientation_max = config.Config().get_orientation_max()
        number_sign = math.copysign(1, rotation)
        number_of_rotation = math.floor(abs(rotation /
                                            orientation_max))
        final_rotation = abs(rotation) % orientation_max

        for _ in range(number_of_rotation):
            self._robot.append_instruction(Rotate(number_sign *
                                                  orientation_max))
        if (final_rotation >= config.Config().get_rotation_min()):
            self._robot.append_instruction(Rotate(number_sign *
                                                  final_rotation))
