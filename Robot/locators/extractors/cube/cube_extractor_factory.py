from Robot.cycle.objects.color import Color
from Robot.locators.extractors.cube import red_cube_extractor,\
    green_cube_extractor, yellow_cube_extractor, blue_cube_extractor


def create_cube_extractor(color):
    if color == Color.RED:
        return red_cube_extractor.RedCubeExtractor()
    elif color == Color.GREEN:
        return green_cube_extractor.GreenCubeExtractor()
    elif color == Color.YELLOW:
        return yellow_cube_extractor.YellowCubeExtractor()
    elif color == Color.BLUE:
        return blue_cube_extractor.BlueCubeExtractor()
    else:
        raise Exception("Segmentor not found for color : " + str(color))
