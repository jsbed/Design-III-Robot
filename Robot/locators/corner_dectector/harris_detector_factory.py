from Robot.cycle.objects.color import Color
from Robot.locators.corner_dectector import black_cube_harris_detector,\
    white_cube_harris_detector


def create_detector(color):

    if color == Color.BLACK:
        return black_cube_harris_detector.BlackCubeHarrisDectector()
    elif color == Color.WHITE:
        return white_cube_harris_detector.WhiteCubeHarrisDectector()
    else:
        raise Exception("Detector not found for color :", color)
