from collections.__main__ import Point
from Robot.game_cycle.objects.color import Color
from Robot.path_finding.grid import SquareGrid
from Robot.controller.robot import Robot
from Robot.path_finding.path_finder import PathFinder
from Robot.path_finding.point_adjustor import PointAdjustor
from Robot.game_cycle.objects.cube import Cube
from Robot.locators.localization import Localization
from Robot.path_finding.angle_adjustor import AngleAdjustor

file = open("path.txt", "w")

CUBE_POSITION = Point(90, 150)
ROBOT_POSITION = Point(50, 50)

grid = SquareGrid()
robot = Robot()
path_finder = PathFinder()
adjustor = PointAdjustor(grid)
angle_adjustor = AngleAdjustor(grid)

cube = Cube(Color.RED, 0, False, Localization(CUBE_POSITION, 0))
robot.set_localization_position(ROBOT_POSITION)


target_point = adjustor.find_target_position(cube.get_localization().position,
                                             robot.get_localization().
                                             position)
'''
target_point = angle_adjustor.calculate_target_point(target_point2,
                                                     cube.get_localization().
                                                     position, 80)
'''

path = path_finder.find_path(robot.get_localization().position, target_point)

for y in reversed(range(0, grid.get_height())):
    for x in range(0, grid.get_width()):
        if (Point(x, y) in path):
            if (Point(x, y) == robot.get_localization().position):
                file.write("4")
            else:
                file.write("1")
        else:
            if (Point(x, y) == cube.get_localization().position):
                file.write("3")
            else:
                file.write("-")
    file.write("\n")

file.close()
