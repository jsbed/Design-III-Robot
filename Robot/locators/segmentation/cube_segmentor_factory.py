from Robot.game_cycle.objects.color import Color
from Robot.locators.segmentation import blue_cube_segmentor, \
    black_cube_segmentor, red_cube_segmentor, green_cube_segmentor, \
    white_cube_segmentor, yellow_cube_segmentor


def create_cube_segmentor(color):
    if color == Color.BLACK:
        return black_cube_segmentor.BlackCubeSegmentor()
    elif color == Color.RED:
        return red_cube_segmentor.RedCubeSegmentor()
    elif color == Color.GREEN:
        return green_cube_segmentor.GreenCubeSegmentor()
    elif color == Color.WHITE:
        return white_cube_segmentor.WhiteCubeSegmentor()
    elif color == Color.YELLOW:
        return yellow_cube_segmentor.YellowCubeSegmentor()
    elif color == Color.BLUE:
        return blue_cube_segmentor.BlueCubeSegmentor()
    else:
        raise Exception("Segmentor not found for color : " + str(color))
