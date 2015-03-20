from Robot.configuration.config import Config
from Robot.locators.extractors.robot_corner.robot_corner_extractor import RobotCornerExtractor
from Robot.locators.segmentation.robot_corners.robot_corner_segmentation import RobotCornerSegmentor


class BlueRobotCornerExtractor(RobotCornerExtractor):

    def __init__(self):
        self._segmentor = RobotCornerSegmentor()
        self._segmentor.set_lower_hsv_values(Config().
                                             get_robot_low_blue_hsv_values())
        self._segmentor.set_upper_hsv_values(Config().
                                             get_robot_high_blue_hsv_values())

    def extract(self, img):
        return self._segmentor.segment_robot_corner(img)
