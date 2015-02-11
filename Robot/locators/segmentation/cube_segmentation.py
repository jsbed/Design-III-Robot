from Robot.color import Color
import Robot.locators.segmentation as segmentation


class CubeSegmentator():

    def extract_cube(self, img):
        raise NotImplementedError


class CubeSegmentatorFactory():

    def create_cube_segmentator(self, color):
        if color == Color.BLACK:
            return segmentation.black_cube_segmentator.BlackCubeSegmentator()
        elif color == Color.RED:
            return segmentation.red_cube_segmentator.RedCubeSegmentator()
        elif color == Color.GREEN:
            return segmentation.green_cube_segmentator.GreenCubeSegmentator()
        elif color == Color.WHITE:
            return segmentation.white_cube_segmentator.WhiteCubeSegmentator()
        elif color == Color.YELLOW:
            return segmentation.yellow_cube_segmentator.YellowCubeSegmentator()
        elif color == Color.BLUE:
            return segmentation.blue_cube_segmentator.BlueCubeSegmentator()
        else:
            raise Exception("Segmentator not found for color : " + color)
