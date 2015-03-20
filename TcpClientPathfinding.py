from random import randint
import json

from Robot.communication.tcp_client import TCPClient
from Robot.configuration.config import Config
from Robot.path_finding.path_finder import PathFinder
from Robot.path_finding.point import Point


# Example for pathfinding
Config().load_config()
client = TCPClient(Config().get_base_station_communication_ip(),
                   Config().get_base_station_communication_port())
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
client.send_data(json.dumps(dictio))

client.disconnect_socket()
