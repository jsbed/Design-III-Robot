from Robot.game_cycle.objects.color import Color
from Robot.locators.segmentation import cube_segmentation, red_cube_segmentor


STANDARD_COLORS = [Color.GREEN, Color.BLUE, Color.YELLOW]


def create_cube_segmentor(color):
    if color in STANDARD_COLORS:
        return cube_segmentation.CubeSegmentor()
    elif color == Color.RED:
        return red_cube_segmentor.RedCubeSegmentor()
    else:
        raise Exception("Segmentor not found for color : " + str(color))
