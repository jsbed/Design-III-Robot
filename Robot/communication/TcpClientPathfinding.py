from Robot.configuration.config import Config
from Robot.communication.tcp_client import TCPClient
from Robot.path_finding.point import Point
from Robot.path_finding.path_finder import PathFinder
import json
from random import randint


# Example for pathfinding
Config("Robot/config.ini").load_config()
client = TCPClient()
client.connect_socket()

robot_position = Point(randint(15, 95), randint(15, 50))
cube_position = Point(randint(15, 95), randint(150, 240))

# target_point = PointAdjustor().find_target_position(cube_position, robot_position)
pathing = PathFinder().find_path(robot_position, cube_position)

path = []
path.append(robot_position)
path.append(PathFinder().get_point_where_path_change_direction(pathing))
path.append(cube_position)

# Transform list of points into list of ints before sending
pathlist = []
pathlist.append(path[0].x)
pathlist.append(path[0].y)
pathlist.append(path[1].x)
pathlist.append(path[1].y)
pathlist.append(path[2].x)
pathlist.append(path[2].y)
cube_list = []
cube_list.append(cube_position.x)
cube_list.append(cube_position.y)

print("Sending to Base Station...")
print("path :", path)
print("cube position :", cube_list)

dictio = {'path': pathlist, 'cubePosition': cube_list}
data = bytes(json.dumps(dictio), "utf-8")
client.send_data(data)

client.diconnect_socket()
