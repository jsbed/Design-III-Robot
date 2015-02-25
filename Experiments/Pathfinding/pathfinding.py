from collections.__main__ import Point
from Robot.color import Color
from Robot.cube import Cube
from Robot.localization import Localization
from Robot.robot.grid import SquareGrid
from Robot.robot.robot import Robot
from Robot.robot.path_finder import PathFinder
from Robot.robot.point_adjustor import PointAdjustor

file = open("path.txt", "w")

CUBE_POSITION = Point(110, 230)
ROBOT_POSITION = Point(75, 32)

grid = SquareGrid()
robot = Robot()
path_finder = PathFinder()
adjustor = PointAdjustor(grid)

cube = Cube(Color.RED, 0, False, Localization(CUBE_POSITION, 0))
robot.set_localization_position(ROBOT_POSITION)


target_point = adjustor.find_target_position(cube.get_localization().position,
                                             robot.get_localization().position)

path = path_finder.a_star_search(grid, robot.get_localization().position,
                                 target_point)

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
