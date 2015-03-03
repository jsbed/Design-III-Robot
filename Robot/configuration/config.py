from configparser import ConfigParser
import collections
import json

from Robot.utilities.singleton import Singleton


CONFIG_FILE_NAME = "config.ini"

SECTION_DEFAULT = "DEFAULT"
SECTION_SEGMENTATION = "SEGMENTATION"
SECTION_PATHFINDING = "PATHFINDING"


class Config(metaclass=Singleton):

    def __init__(self, path=CONFIG_FILE_NAME):
        self._parser = ConfigParser()
        self._parameters = {}
        self._path = path

    def load_config(self):
        self._parser.read(self._path)

    def get_atlas_url(self):
        return self._parser.get(SECTION_DEFAULT, "AtlasUrl")

    def get_kinect_connection_port(self):
        return int(self._parser.get(SECTION_DEFAULT, "KinectConnectionPort"))

    def get_base_station_communication_port(self):
        return int(self._parser.get(SECTION_DEFAULT,
                                    "BaseStationCommunicationPort"))

    def get_base_station_communication_ip(self):
        return self._parser.get(SECTION_DEFAULT, "BaseStationCommunicationIP")

    def get_low_blue_hsv_values(self):
        return json.loads(self._parser.get(SECTION_SEGMENTATION,
                                           "LowBlueHSV"))

    def get_high_blue_hsv_values(self):
        return json.loads(self._parser.get(SECTION_SEGMENTATION,
                                           "HighBlueHSV"))

    def get_low_green_hsv_values(self):
        return json.loads(self._parser.get(SECTION_SEGMENTATION,
                                           "LowGreenHSV"))

    def get_high_green_hsv_values(self):
        return json.loads(self._parser.get(SECTION_SEGMENTATION,
                                           "HighGreenHSV"))

    def get_low_yellow_hsv_values(self):
        return json.loads(self._parser.get(SECTION_SEGMENTATION,
                                           "LowYellowHSV"))

    def get_high_yellow_hsv_values(self):
        return json.loads(self._parser.get(SECTION_SEGMENTATION,
                                           "HighYellowHSV"))

    def get_low_red_hsv_values(self):
        return json.loads(self._parser.get(SECTION_SEGMENTATION,
                                           "LowRedHSV"))

    def get_high_red_hsv_values(self):
        return json.loads(self._parser.get(SECTION_SEGMENTATION,
                                           "HighRedHSV"))

    def get_table_width(self):
        return int(self._parser.get(SECTION_PATHFINDING, "TableWidth"))

    def get_table_height(self):
        return int(self._parser.get(SECTION_PATHFINDING, "TableHeight"))

    def get_robot_radius(self):
        return int(self._parser.get(SECTION_PATHFINDING, "RobotRadius"))

    def get_cube_radius(self):
        return int(self._parser.get(SECTION_PATHFINDING, "CubeRadius"))

    def get_atlas_zone_position(self):
        return collections.__main__.Point(self._parser.get(SECTION_PATHFINDING,
                                                           "AtlasZonePosition"))
