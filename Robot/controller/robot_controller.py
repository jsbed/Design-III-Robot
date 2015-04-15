import math
import time

from Robot.communication.base_station_client import BaseStationClient
from Robot.communication.serial_port import SerialPort
from Robot.configuration import config
from Robot.controller.instructions.move_forward import MoveForward
from Robot.controller.instructions.move_right import MoveRight
from Robot.controller.instructions.rotate import Rotate
from Robot.controller.robot import Robot
from Robot.cycle import atlas
from Robot.locators import cube_locator
from Robot.managers.gripper_manager import GripperManager
from Robot.managers.led_manager import LedManager
from Robot.path_finding.point import Point
from Robot.path_finding.point_adjustor import PointAdjustor


LOCALIZE_CUBE_ANGLE = 0
CUBE_RELEASE_ANGLE = 180
ROTATION_MIN_POSSIBLE = 3
DISTANCE_MIN_POSSIBLE = 3


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
        atlas_zone_position = config.Config().get_atlas_zone_position()
        self._distance = PointAdjustor(). \
            calculate_distance_between_points(self._robot_position,
                                              atlas_zone_position)
        rotation = -PointAdjustor().find_robot_rotation(LOCALIZE_CUBE_ANGLE,
                                                        self._robot_position,
                                                        atlas_zone_position)

        self._move_robot_towards_target_point(atlas_zone_position)
        self._append_rotations(rotation)
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

        if self._robot_orientation < 180:
            rotation = -self._robot_orientation
        else:
            rotation = 360 - self._robot_orientation

        if (abs(rotation) > 5 or self._distance > 40):
            self._move_robot_towards_target_point(localization_position)
            self._append_rotations(
                -PointAdjustor().find_robot_rotation(LOCALIZE_CUBE_ANGLE,
                                                     self._robot_position,
                                                     localization_position))
        else:
            self._robot.append_instruction(
                MoveForward(localization_position.y - self._robot_position.y))
            self._robot.append_instruction(
                MoveRight(self._robot_position.x - localization_position.x))
            BaseStationClient().send_path(
                [Point(self._robot_position.x, localization_position.y),
                 Point(localization_position.x, localization_position.y)])

        self._robot.execute_instructions()

    def robot_is_facing_cube(self, cube):
        try:
            self._angle = cube_locator.find_cube_center_angle_from_camera(
                cube.get_color())
        except Exception as e:
            self._angle = None
            print("robot_is_facing_cube : cube not found - ", str(e))
            return False
        else:
            print("robot_is_facing_cube : ", abs(self._angle) <=
                  config.Config().get_orientation_uncertainty())

            return (abs(self._angle) <=
                    config.Config().get_orientation_uncertainty())

    def rotate_robot_torwards_cube(self, cube):
        if self._angle:
            self._append_rotations(self._angle)
            self._robot.execute_instructions()
        else:
            self._fix_robot_orientation_for_localization()

    def find_cube_position(self, cube):
        self._update_robot_localization()

        distance = cube_locator.find_cube_distance_from_camera(
            cube.get_color())

        print("cube distance from cam :", distance)
        print("robot pos :", self._robot_position)

        x, y = PointAdjustor().calculate_cube_position(
            distance, self._robot_orientation + self._angle)

        return Point(self._robot_position.x + x, self._robot_position.y + y)

    def turn_switch_on(self):
        self._switch += 1

    def turn_switch_off(self):
        self._switch -= 1

    def get_switch_status(self):
        return self._switch >= config.Config().get_number_of_switches()

    def push_cube(self, cube):
        self._update_robot_localization()

        distance = cube_locator.find_cube_distance_from_camera(
            cube.get_color())

        distance_between_cube_and_wall = PointAdjustor().\
            calculate_distance_between_cube_and_closest_wall(
                cube.get_localization().position)

        push_distance = distance + config.Config().get_push_cube_distance()
        wall_push_distance = (distance + distance_between_cube_and_wall -
                              config.Config().get_cube_radius() * 2 -
                              config.Config().get_gripper_size())

        print("cube distance with cam : ", distance)
        max_push_distance = 50

        if (push_distance > max_push_distance):
            push_distance = max_push_distance
        elif (push_distance > wall_push_distance):
            push_distance = wall_push_distance

        x, y = PointAdjustor().calculate_distance_point_with_robot(
            push_distance, self._robot_orientation)

        print("destination point for path : ", x, y)
        BaseStationClient().send_path(
            [Point(self._robot_position.x + x, self._robot_position.y + y)])

        self._robot.append_instruction(MoveForward(push_distance))

        self._robot.execute_instructions()

    def robot_is_close_to_target_zone(self, target):
        self._update_robot_localization()
        self._robot_orientation = (self._robot_orientation + 180) % 360
        self._distance = PointAdjustor(). \
            calculate_distance_between_points(self._robot_position,
                                              target)

        return self._robot_is_next_to_target_point()

    def move_robot_to_target_zone(self, destination):
        self._update_robot_localization()
        self._robot_orientation = (self._robot_orientation + 180) % 360
        destination_point = PointAdjustor().find_next_point(
            self._robot_position, destination)
        print("move to target zone dest point", destination_point)

        self._distance = PointAdjustor(). \
            calculate_distance_between_points(self._robot_position,
                                              destination_point)
        self._move_robot_towards_target_zone_backward(destination_point)
        self._robot.execute_instructions()

    def robot_is_next_to_target_zone_with_correct_orientation(
            self, target_zone_position):
        self._update_robot_localization()

        lateral_distance = target_zone_position.x - self._robot_position.x

        if self._robot_orientation < 180:
            rotation = self._robot_orientation
        else:
            rotation = 360 - self._robot_orientation

        return (abs(lateral_distance) <= config.Config().
                get_target_zone_uncertainty_with_distance() and
                abs(rotation) <= config.Config().
                get_target_zone_uncertainty_with_orientation())

    def move_robot_into_target_zone(self, target_zone_position):
        self._update_robot_localization()

        self._rotate_to_target_zone(target_zone_position)
        self._lateral_move_to_target_zone(target_zone_position)

        print("verif if instructions remain")
        if (self.instruction_remaining()):
            print("yes -> execute instructions")
            self._robot.execute_instructions()
        else:
            print("no -> restart checkup")
            False

    def move_forward_to_target_zone(self, target_zone_position):
        print("MOVING TORWARD ", target_zone_position)
        # self._update_robot_localization()

        print("target zone y position: ", target_zone_position.y)
        print("target zone x position: ", target_zone_position.x)

        distance_x = target_zone_position.x - self._robot_position.x
        distance_y = self._robot_position.y - target_zone_position.y - \
            config.Config().get_gripper_size() - \
            config.Config().get_robot_radius()

        print("droping distance", distance_y)

        cube_radius = config.Config().get_cube_radius() - 1

        self._append_rotations(-180)
        self._robot.append_instruction(MoveForward(distance_y - cube_radius))
        self._robot.append_instruction(MoveRight(distance_x))
        self._robot.append_instruction(MoveForward(cube_radius))

        path = [Point(
            self._robot_position.x, self._robot_position.y - distance_y +
            cube_radius),
            Point(self._robot_position.x + distance_x,
                  self._robot_position.y - distance_y + cube_radius),
            Point(self._robot_position.x + distance_x, self._robot_position.y -
                  distance_y)]
        BaseStationClient().send_path(path)
        self._robot.execute_instructions()

    def move_backward(self, target_zone_position):
        BaseStationClient().send_path(
            [Point(target_zone_position.x, target_zone_position.y +
                   config.Config().get_move_backward_distance() +
                   config.Config().get_robot_radius() +
                   config.Config().get_cube_radius() +
                   config.Config().get_gripper_size())])
        self._robot.append_instruction(
            MoveForward((config.Config().get_move_backward_distance())))
        self._append_rotations(180)
        self._robot.execute_instructions()

    def instruction_remaining(self):
        return len(self._robot.get_instructions()) > 0

    def next_instruction(self):
        self._robot.execute_instructions()

    def end_cycle(self):
        self._led_manager.display_red_led()

    def _rotate_to_target_zone(self, target_zone_position):
        orientation_uncertainty = config.Config(
        ).get_target_zone_uncertainty_with_orientation()

        if self._robot_orientation < 180:
            rotation = -self._robot_orientation
        else:
            rotation = 360 - self._robot_orientation

        print("calculated rotation", rotation)

        if (abs(rotation) > orientation_uncertainty):
            print("Rotation ", rotation)

            self._robot.append_instruction(Rotate(rotation))

    def _lateral_move_to_target_zone(self, target_zone_position):
        distance_uncertainty = config.Config(
        ).get_target_zone_uncertainty_with_distance()

        lateral_distance = target_zone_position.x - self._robot_position.x

        print("calculated lateral distance", lateral_distance)

        if (abs(lateral_distance) > distance_uncertainty):
            print("Lateral distance ", lateral_distance)

            self._robot.append_instruction(MoveRight(-lateral_distance))

    def _fix_robot_orientation_for_localization(self):
        self._update_robot_localization()
        angle_fix = config.Config().get_adjusted_localization_rotation()

        if self._robot_orientation <= 180:
            self._append_rotations(- angle_fix - self._robot_orientation)
        else:
            self._append_rotations(abs(
                self._robot_orientation - 360 - angle_fix))

        self._robot.execute_instructions()

    def _update_robot_localization(self):
        time.sleep(2)
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
            self._robot.append_instruction(MoveForward(self._distance))
        BaseStationClient().send_path([destination])

    def _move_robot_towards_target_zone_backward(self, destination):
        print("destination", destination)
        rotation = PointAdjustor().find_robot_rotation(
            self._robot_orientation, self._robot_position, destination)
        self._append_rotations(rotation)
        if (self._distance >= config.Config().get_distance_min()):
            self._robot.append_instruction(MoveForward(-self._distance))
        BaseStationClient().send_path([destination])

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

        return (abs(rotation) <= angle_uncertainty)

    def _append_rotations(self, rotation):
        print("appending rotation :", rotation)
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
