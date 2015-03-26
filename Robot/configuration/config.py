from configparser import ConfigParser
import json
import os

from Robot.path_finding.point import Point
from Robot.utilities.singleton import Singleton


CONFIG_FILE_NAME = "config.ini"

SECTION_DEFAULT = "DEFAULT"
SECTION_TABLE_CONFIGURATION = "TABLECONFIGURATION"
SECTION_CUBE_SEGMENTATION = "CUBESEGMENTATION"
SECTION_ROBOT_SEGMENTATION = "ROBOTSEGMENTATION"
SECTION_PATHFINDING = "PATHFINDING"
SECTION_FLAGCREATION = "FLAGCREATION"
SECTION_LEDS = "LEDS"
SECTION_GRIPPER = "GRIPPERDATA"
SECTION_PERSPECTIVE = "PERSPECTIVE"
SECTION_SERIAL_PORT = "SERIALPORT"


class Config(metaclass=Singleton):

    def __init__(self, path=CONFIG_FILE_NAME):
        self._parser = ConfigParser()
        self._parameters = {}
        self._path = path

    def load_config(self):
        self._parser.read(self._path)

    def get_atlas_url(self):
        return self._parser.get(SECTION_DEFAULT, "AtlasUrl")

    def get_base_station_communication_port(self):
        return int(self._parser.get(SECTION_DEFAULT,
                                    "BaseStationCommunicationPort"))

    def get_base_station_communication_ip(self):
        return self._parser.get(SECTION_DEFAULT, "BaseStationCommunicationIP")

    def get_kinect_mask_img_path(self):
        return os.path.join(self._parser.get(SECTION_TABLE_CONFIGURATION,
                                             "KinectMask"))

    def get_perspective_matrix_path(self):
        return os.path.join(self._parser.get(SECTION_TABLE_CONFIGURATION,
                                             "PerspectiveArray"))

    def get_cube_low_blue_hsv_values(self):
        return json.loads(self._parser.get(SECTION_CUBE_SEGMENTATION,
                                           "LowBlueHSV"))

    def get_cube_high_blue_hsv_values(self):
        return json.loads(self._parser.get(SECTION_CUBE_SEGMENTATION,
                                           "HighBlueHSV"))

    def get_cube_low_green_hsv_values(self):
        return json.loads(self._parser.get(SECTION_CUBE_SEGMENTATION,
                                           "LowGreenHSV"))

    def get_cube_high_green_hsv_values(self):
        return json.loads(self._parser.get(SECTION_CUBE_SEGMENTATION,
                                           "HighGreenHSV"))

    def get_cube_low_yellow_hsv_values(self):
        return json.loads(self._parser.get(SECTION_CUBE_SEGMENTATION,
                                           "LowYellowHSV"))

    def get_cube_high_yellow_hsv_values(self):
        return json.loads(self._parser.get(SECTION_CUBE_SEGMENTATION,
                                           "HighYellowHSV"))

    def get_cube_low_red_hsv_values(self):
        return json.loads(self._parser.get(SECTION_CUBE_SEGMENTATION,
                                           "LowRedHSV"))

    def get_cube_high_red_hsv_values(self):
        return json.loads(self._parser.get(SECTION_CUBE_SEGMENTATION,
                                           "HighRedHSV"))

    def get_robot_low_blue_hsv_values(self):
        return json.loads(self._parser.get(SECTION_ROBOT_SEGMENTATION,
                                           "LowBlueHSV"))

    def get_robot_high_blue_hsv_values(self):
        return json.loads(self._parser.get(SECTION_ROBOT_SEGMENTATION,
                                           "HighBlueHSV"))

    def get_robot_low_orange_hsv_values(self):
        return json.loads(self._parser.get(SECTION_ROBOT_SEGMENTATION,
                                           "LowOrangeHSV"))

    def get_robot_high_orange_hsv_values(self):
        return json.loads(self._parser.get(SECTION_ROBOT_SEGMENTATION,
                                           "HighOrangeHSV"))

    def get_robot_low_pink_hsv_values(self):
        return json.loads(self._parser.get(SECTION_ROBOT_SEGMENTATION,
                                           "LowPinkHSV"))

    def get_robot_high_pink_hsv_values(self):
        return json.loads(self._parser.get(SECTION_ROBOT_SEGMENTATION,
                                           "HighPinkHSV"))

    def get_perspective_translation_matrix(self):
        return json.loads(self._parser.get(SECTION_PERSPECTIVE,
                                           "TranslationMatrix"))

    def get_perspective_rotation_y(self):
        return float(self._parser.get(SECTION_PERSPECTIVE, "RotationYAxis"))

    def get_lower_gripper_values(self):
        return json.loads(self._parser.get(SECTION_GRIPPER,
                                           "LowerGripper"))

    def get_lift_gripper_values(self):
        return json.loads(self._parser.get(SECTION_GRIPPER,
                                           "LiftGripper"))

    def get_take_cube_gripper_values(self):
        return json.loads(self._parser.get(SECTION_GRIPPER,
                                           "TakeCube"))

    def get_release_cube_gripper_values(self):
        return json.loads(self._parser.get(SECTION_GRIPPER,
                                           "TakeCube"))

    def get_widest_gripper_values(self):
        return json.loads(self._parser.get(SECTION_GRIPPER,
                                           "WidestGripper"))

    def get_robot_corner_size(self):
        return float(self._parser.get(SECTION_PERSPECTIVE, "RobotCornerSize"))

    def get_table_width(self):
        return float(self._parser.get(SECTION_PATHFINDING, "TableWidth"))

    def get_table_height(self):
        return float(self._parser.get(SECTION_PATHFINDING, "TableHeight"))

    def get_robot_radius(self):
        return float(self._parser.get(SECTION_PATHFINDING, "RobotRadius"))

    def get_cube_radius(self):
        return float(self._parser.get(SECTION_PATHFINDING, "CubeRadius"))

    def get_distance_between_objects(self):
        return float(self._parser.get(SECTION_PATHFINDING,
                                      "DistanceBetweenObjects"))

    def get_check_points_distance(self):
        return float(self._parser.get(SECTION_PATHFINDING,
                                      "CheckPointsDistance"))

    def get_distance_uncertainty(self):
        return float(self._parser.get(SECTION_PATHFINDING,
                                      "DistanceUncertainty"))

    def get_orientation_uncertainty(self):
        return float(self._parser.get(SECTION_PATHFINDING,
                                      "OrientationUncertainty"))

    def get_push_cube_distance(self):
        return float(self._parser.get(SECTION_PATHFINDING,
                                      "PushCubeDistance"))

    def get_atlas_zone_position(self):
        return Point._make(json.loads(self._parser.get(SECTION_PATHFINDING,
                                                       "AtlasZonePosition")))

    def get_localize_cube_position(self):
        return Point._make(json.loads(self._parser.get(SECTION_PATHFINDING,
                                                       "LocalizeCubePosition")))

    def get_target_zone_position(self):
        return Point._make(json.loads(self._parser.get(SECTION_FLAGCREATION,
                                                       "TargetZonePosition")))

    def get_flag_creation_zone_position(self):
        return Point._make(json.loads(self._parser.get(
                           SECTION_FLAGCREATION, "FlagCreationZonePosition")))

    def get_cube_center_distance(self):
        return float(self._parser.get(SECTION_FLAGCREATION,
                                      "CubeCenterDistance"))

    def get_red_led_wait_time(self):
        return float(self._parser.get(SECTION_LEDS, "RedLedWaitTime"))

    def get_display_country_wait_time(self):
        return float(self._parser.get(SECTION_LEDS, "DisplayCountryWaitTime"))

    def get_pololu_serial_port_path(self):
        return self._parser.get(SECTION_SERIAL_PORT, "PololuSerialPort")

    def get_stm_serial_port_path(self):
        return self._parser.get(SECTION_SERIAL_PORT, "STMSerialPort")

    def get_stm_serial_port_baudrate(self):
        return int(self._parser.get(SECTION_SERIAL_PORT, "STMBaudRate"))
