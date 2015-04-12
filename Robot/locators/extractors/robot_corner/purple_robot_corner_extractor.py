from Robot.configuration.config import Config
from Robot.locators.extractors.robot_corner.robot_corner_extractor import RobotCornerExtractor
from Robot.locators.segmentation.robot_corners.robot_corner_segmentation import RobotCornerSegmentor


class PurpleRobotCornerExtractor(RobotCornerExtractor):

    def __init__(self):
        self._segmentor = RobotCornerSegmentor()
        self._segmentor.set_lower_hsv_values([81, 60, 70])
        self._segmentor.set_upper_hsv_values([105, 255, 255])

    def extract(self, img):
        return self._segmentor.segment_robot_corner(img)
