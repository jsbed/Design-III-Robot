from Robot.communication.base_station_client import BaseStationClient
from Robot.configuration.config import Config
from Robot.path_finding.point import Point


Config().load_config()
BaseStationClient().connect_socket()

path = [Point(80, 80), Point(30, 150)]
BaseStationClient().remove_path()
