from Robot.color import Color
import Robot.locators.segmentation as segmentation


class CubeSegmentor():

    def extract_cube(self, img):
        raise NotImplementedError


class CubeSegmentorFactory():

    def create_cube_segmentor(self, color):
        if color == Color.BLACK:
            return segmentation.black_cube_segmentor.BlackCubeSegmentor()
        elif color == Color.RED:
            return segmentation.red_cube_segmentor.RedCubeSegmentor()
        elif color == Color.GREEN:
            return segmentation.green_cube_segmentor.GreenCubeSegmentor()
        elif color == Color.WHITE:
            return segmentation.white_cube_segmentor.WhiteCubeSegmentor()
        elif color == Color.YELLOW:
            return segmentation.yellow_cube_segmentor.YellowCubeSegmentor()
        elif color == Color.BLUE:
            return segmentation.blue_cube_segmentor.BlueCubeSegmentor()
        else:
            raise Exception("Segmentor not found for color : " + color)
