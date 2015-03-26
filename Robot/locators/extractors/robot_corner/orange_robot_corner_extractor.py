from Robot.locators.extractors.robot_corner.robot_corner_extractor import RobotCornerExtractor
from Robot.locators.segmentation.robot_corners.orange_robot_corner_segmentor import OrangeRobotCornerSegmentor


class OrangeRobotCornerExtractor(RobotCornerExtractor):

    def extract(self, img):
        return OrangeRobotCornerSegmentor().segment_robot_corner(img)
