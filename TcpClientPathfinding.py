from random import randint
import json

from Robot.communication.tcp_client import TCPClient
from Robot.configuration.config import Config
from Robot.path_finding.point import Point
from Robot.cycle.objects.color import Color
from Robot.country.country import Country
from Robot.country.flag_creator import FlagCreator
from Robot.communication.base_station_client import BaseStationClient
from Robot.country.country_repository import CountryRepository


Config().load_config()
client = TCPClient(Config().get_base_station_ip(),
                   Config().get_base_station_port())
client.connect_socket()

country = Country("TestCountry", [Color.NONE,
                                                 Color.NONE,
                                                 Color.NONE,
                                                 Color.RED,
                                                 Color.WHITE,
                                                 Color.RED,
                                                 Color.NONE,
                                                 Color.NONE,
                                                 Color.NONE])
flag_creator = FlagCreator(country)


robot_position = Point(randint(15, 95), randint(15, 50))
cube_position = Point(randint(15, 95), randint(150, 240))
path = [70, 90]

print("Sending to Base Station...")
print("path :", path)

#
#    print(cube)

dictio = {'path': path}
for cube in flag_creator.get_cube_order():
    client.send_data(json.dumps({'cube position': [int(cube.get_target_zone_position().x),
                                                   int(cube.get_target_zone_position().y)]}))
    client.send_data(json.dumps({'cube color': cube.get_color().value}))
client.send_data(json.dumps(dictio))

client.disconnect_socket()
