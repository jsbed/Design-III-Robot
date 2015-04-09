from math import degrees, atan2, radians
import math

from Robot.configuration import config
from Robot.path_finding.point import Point

ANGLE_ADJUSTMENT = 90
ROTATION_MAX = 180


class PointAdjustor():

    def find_target_position(self, cube_position, robot_position):
        self._target_point = cube_position
        self._cube_center = cube_position
        self._robot_position = robot_position
        self._distance_between_points = (config.Config().get_cube_radius() +
                                         config.Config().
                                         get_distance_between_objects() +
                                         config.Config().get_robot_radius() +
                                         config.Config().get_gripper_size())

        self._check_if_cube_is_too_close_to_wall()

        return self._target_point

    def find_next_point(self, start, end):
        distance = self.calculate_distance_between_points(start, end)
        current_distance = config.Config().get_check_points_distance()

        if (distance <= current_distance +
                config.Config().get_distance_uncertainty()):
            return end
        else:
            angle = self.calculate_angle_between_points(start, end)
            x = start.x + int(current_distance * math.cos(radians(angle)))
            y = start.y + int(current_distance * math.sin(radians(angle)))
            return Point(x, y)

    def find_robot_rotation(self, robot_orientation, robot_position, target):
        robot_position = Point(config.Config().get_table_width() -
                               robot_position.x, robot_position.y)
        target = Point(config.Config().get_table_width() - target.x, target.y)
        angle = self.calculate_angle_between_points(robot_position, target)
        rotation_angle = int(angle - robot_orientation - ANGLE_ADJUSTMENT)
        if (rotation_angle > ROTATION_MAX):
            rotation_angle = rotation_angle - 360
        if (rotation_angle < -ROTATION_MAX):
            rotation_angle = 360 + rotation_angle
        return rotation_angle

    def calculate_distance_between_cube_and_closest_wall(self, cube_position):
        return min(min(config.Config().get_table_width() - cube_position.x,
                       cube_position.x - 0),
                   min(config.Config().get_table_height() - cube_position.y,
                       cube_position.y - 0))

    def calculate_cube_position(self, distance, robot_orientation):
        x = int(distance * math.sin(radians(robot_orientation)))
        y = int(distance * math.cos(radians(robot_orientation)) +
                config.Config().get_cube_radius() +
                config.Config().get_robot_radius() +
                config.Config().get_gripper_size())

        return (x, y)

    '''
    Description: Verify if the cube is too close or next to a wall
                 and adjust the target position accordingly. Otherwise,
                 call adjut_target_point to find the target position
                 closest to the robot.
    '''

    def _check_if_cube_is_too_close_to_wall(self):
        if (self._cube_center.x < config.Config().get_robot_radius()):
            self._target_point = Point(self._target_point.x +
                                       self._distance_between_points,
                                       self._target_point.y)

        elif (self._cube_center.x > (config.Config().get_table_width() -
                                     config.Config().get_robot_radius())):
            self._target_point = Point(self._target_point.x -
                                       self._distance_between_points,
                                       self._target_point.y)

        elif (self._cube_center.y > (config.Config().get_table_height() -
                                     config.Config().get_robot_radius())):
            self._target_point = Point(self._target_point.x,
                                       self._target_point.y -
                                       self._distance_between_points)

        elif (self._cube_center.y < config.Config().get_robot_radius()):
            self._target_point = Point(self._target_point.x,
                                       self._target_point.y +
                                       self._distance_between_points)

        else:
            self._adjust_target_point()

    def _adjust_target_point(self):
        if (self._cube_center.y < self._robot_position.y):
            self._target_point = Point(self._target_point.x,
                                       self._target_point.y +
                                       self._distance_between_points)

        else:
            self._target_point = Point(self._target_point.x,
                                       self._target_point.y -
                                       self._distance_between_points)

    @staticmethod
    def calculate_angle_between_points(start, end):
        xDiff = end.x - start.x
        yDiff = end.y - start.y

        return degrees(atan2(yDiff, xDiff))

    @staticmethod
    def calculate_distance_between_points(start, end):
        return math.sqrt(math.pow(end.x - start.x, 2) +
                         math.pow(end.y - start.y, 2))
