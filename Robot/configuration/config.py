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
SECTION_VIDEO_SETTINGS = "VIDEOSETTINGS"


class Config(metaclass=Singleton):

    def __init__(self, path=CONFIG_FILE_NAME):
        self._parser = ConfigParser()
        self._parameters = {}
        self._path = path

    def load_config(self):
        self._parser.read(self._path)

    def get_atlas_url(self):
        return self._parser.get(SECTION_DEFAULT, "AtlasUrl")

    def get_base_station_port(self):
        return int(self._parser.get(SECTION_DEFAULT, "BaseStationPort"))

    def get_base_station_ip(self):
        return self._parser.get(SECTION_DEFAULT, "BaseStationIP")

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

    def get_robot_low_cyan_hsv_values(self):
        return json.loads(self._parser.get(SECTION_ROBOT_SEGMENTATION,
                                           "LowCyanHSV"))

    def get_robot_high_cyan_hsv_values(self):
        return json.loads(self._parser.get(SECTION_ROBOT_SEGMENTATION,
                                           "HighCyanHSV"))

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
                                           "ReleaseCube"))

    def get_widest_gripper_values(self):
        return json.loads(self._parser.get(SECTION_GRIPPER,
                                           "WidestGripper"))

    def get_robot_corner_size(self):
        return float(self._parser.get(SECTION_PERSPECTIVE, "RobotCornerSize"))

    def get_table_width(self):
        return float(self._parser.get(SECTION_PATHFINDING, "TableWidth"))

    def get_table_height(self):
        return float(self._parser.get(SECTION_PATHFINDING, "TableHeight"))

    def get_gripper_size(self):
        return float(self._parser.get(SECTION_PATHFINDING, "GripperSize"))

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

    def get_atlas_distance_uncertainty(self):
        return float(self._parser.get(SECTION_PATHFINDING,
                                      "AtlasDistanceUncertainty"))

    def get_distance_uncertainty(self):
        return float(self._parser.get(SECTION_PATHFINDING,
                                      "DistanceUncertainty"))

    def get_distance_uncertainty_with_cube(self):
        return float(self._parser.get(SECTION_PATHFINDING,
                                      "DistanceUncertaintyWithCube"))

    def get_move_backward_distance(self):
        return float(self._parser.get(SECTION_PATHFINDING,
                                      "BackwardDistance"))

    def get_orientation_uncertainty(self):
        return float(self._parser.get(SECTION_PATHFINDING,
                                      "OrientationUncertainty"))

    def get_target_zone_uncertainty(self):
        return float(self._parser.get(SECTION_PATHFINDING,
                                      "UncertaintyWithTargetZone"))

    def get_orientation_max(self):
        return float(self._parser.get(SECTION_PATHFINDING,
                                      "OrientationMax"))

    def get_rotation_min(self):
        return float(self._parser.get(SECTION_PATHFINDING,
                                      "RotationMin"))

    def get_distance_min(self):
        return float(self._parser.get(SECTION_PATHFINDING,
                                      "DistanceMin"))

    def get_push_cube_distance(self):
        return float(self._parser.get(SECTION_PATHFINDING,
                                      "PushCubeDistance"))

    def get_number_of_switches(self):
        return float(self._parser.get(SECTION_PATHFINDING,
                                      "SwitchNumber"))

    def get_atlas_zone_position(self):
        return Point._make(json.loads(self._parser.get(SECTION_PATHFINDING,
                                                       "AtlasZonePosition")))

    def get_localize_cube_position(self):
        return Point._make(json.loads(self._parser.get(SECTION_PATHFINDING,
                                                       "LocalizeCubePosition")))

    def get_adjusted_localization_rotation(self):
        return float(self._parser.get(SECTION_PATHFINDING,
                                      "AdjustedLocalizationRotation"))

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

    def get_stm_serial_port_timeout(self):
        return float(self._parser.get(SECTION_SERIAL_PORT, "STMTimeout"))

    def get_camera_width(self):
        return int(self._parser.get(SECTION_VIDEO_SETTINGS, "CamWidth"))

    def get_camera_height(self):
        return int(self._parser.get(SECTION_VIDEO_SETTINGS, "CamHeight"))

    def get_camera_index(self):
        return int(self._parser.get(SECTION_VIDEO_SETTINGS, "CameraIndex"))
