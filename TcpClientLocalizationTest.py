from Robot.communication.base_station_client import BaseStationClient
from Robot.configuration.config import Config


Config().load_config()


BaseStationClient().connect_socket()
print("waiting")
loc = BaseStationClient().request_robot_localization()
print("received")
print(loc.position)
print(loc.orientation)
print(loc.unknown)
