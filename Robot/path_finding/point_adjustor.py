from Robot.configuration import config
from Robot.path_finding.point import Point
import math
from math import degrees, atan2


class PointAdjustor():

    def __init__(self):
        self._target_point = Point(0, 0)
        self._cube_center = Point(0, 0)
        self._robot_position = Point(0, 0)
        self._distance_between_points = (config.Config().get_cube_radius() +
                                         config.Config().
                                         get_distance_between_objects() +
                                         config.Config().get_robot_radius())

    def find_target_position(self, cube_position, robot_position):
        self._target_point = cube_position
        self._cube_center = cube_position
        self._robot_position = robot_position

        self._check_if_cube_too_close_to_wall()

        return self._target_point

    def find_next_point(self, start, end):
        distance = self._calculate_distance_between_points(start, end)
        current_distance = config.Config().get_check_points_distance()

        if (distance <= current_distance +
                config.Config().get_distance_uncertainty()):
            return Point(end.x, end.y)

        else:
            angle = self._calculate_angle_between_points(start, end)
            x = current_distance * math.cos(angle)
            y = current_distance * math.sin(angle)
            return Point(start.x + int(x), start.y + int(y))

    def find_robot_orientation(self, robot_orientation, robot_position, point):
        start_x = config.Config().get_table_width() - robot_position.x
        end_x = config.Config().get_table_width() - point.x
        start = Point(start_x, robot_position.y)
        end = Point(end_x, point.y)
        angle = self._calculate_angle_between_points(start, end)
        rotation_angle = int(angle - robot_orientation - 90)
        if (rotation_angle > 180):
            rotation_angle = 360 - rotation_angle
        if (rotation_angle < -180):
            rotation_angle = 360 + rotation_angle
        return rotation_angle

    '''
    Description: Verify if the cube is too close or next to a wall
                 and adjust the target position accordingly. Otherwise,
                 call adjut_target_point to find the target position
                 closest to the robot.
    '''
    def _check_if_cube_too_close_to_wall(self):
        if (self._cube_center.x < config.Config().get_robot_radius()):
            self._target_point = Point(self._target_point.x +
                                       self._distance_between_points,
                                       self._target_point.y)

        elif (self._cube_center.x > (config.Config().get_width() -
                                     config.Config().get_robot_radius())):
            self._target_point = Point(self._target_point.x -
                                       self._distance_between_points,
                                       self._target_point.y)

        elif (self._cube_center.y > (config.Config().get_height() -
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
        if (self._cube_center.x <= self._robot_position.x):
            if (self._cube_center.y <= (self._robot_position.y -
                                        self._distance_between_points)):
                self._target_point = Point(self._target_point.x,
                                           self._target_point.y +
                                           self._distance_between_points)

            elif (self._cube_center.y >= (self._robot_position.y +
                                          self._distance_between_points)):
                self._target_point = Point(self._target_point.x,
                                           self._target_point.y -
                                           self._distance_between_points)

            else:
                self._target_point = (self._target_point.x +
                                      self._distance_between_points,
                                      self._target_point.y)

        else:
            if (self._cube_center.y <= (self._robot_position.y -
                                        self._distance_between_points)):
                self._target_point = Point(self._target_point.x,
                                           self._target_point.y +
                                           self._distance_between_points)

            elif (self._cube_center.y >= (self._robot_position.y +
                                          self._distance_between_points)):
                self._target_point = Point(self._target_point.x,
                                           self._target_point.y -
                                           self._distance_between_points)

            else:
                self._target_point = Point(self._target_point.x -
                                           self._distance_between_points,
                                           self._target_point.y)

    @staticmethod
    def _calculate_angle_between_points(start, end):
        xDiff = end.x - start.x
        yDiff = end.y - start.y

        return degrees(atan2(yDiff, xDiff))

    @staticmethod
    def _calculate_distance_between_points(start, end):
        return math.sqrt(math.pow(end.x - start.x, 2) +
                         math.pow(end.y - start.y, 2))
