from Robot.cycle.objects.color import Color
from Robot.locators.extractors.robot_corner import blue_robot_corner_extractor,\
    orange_robot_corner_extractor, pink_robot_corner_extractor,\
    purple_robot_corner_extractor


def create_robot_corner_extractor(color):
    if color == Color.BLUE:
        return blue_robot_corner_extractor.BlueRobotCornerExtractor()
    elif color == Color.ORANGE:
        return orange_robot_corner_extractor.OrangeRobotCornerExtractor()
    elif color == Color.PINK:
        return pink_robot_corner_extractor.PinkRobotCornerExtractor()
    elif color == Color.CYAN:
        return purple_robot_corner_extractor.PurpleRobotCornerExtractor()
    else:
        raise Exception("Segmentor not found for color : " + str(color))
