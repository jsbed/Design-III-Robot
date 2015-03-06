from Robot.game_cycle.objects.color import Color
from Robot.locators.extractors import black_cube_extractor, red_cube_extractor,\
    green_cube_extractor, white_cube_extractor, yellow_cube_extractor,\
    blue_cube_extractor


def create_cube_extractor(color):
    if color == Color.BLACK:
        return black_cube_extractor.BlackCubeExtractor()
    elif color == Color.RED:
        return red_cube_extractor.RedCubeExtractor()
    elif color == Color.GREEN:
        return green_cube_extractor.GreenCubeExtractor()
    elif color == Color.WHITE:
        return white_cube_extractor.WhiteCubeExtractor()
    elif color == Color.YELLOW:
        return yellow_cube_extractor.YellowCubeExtractor()
    elif color == Color.BLUE:
        return blue_cube_extractor.BlueCubeExtractor()
    else:
        raise Exception("Segmentor not found for color : " + str(color))
