from Robot.locators.segmentation.cube_segmentation import CubeSegmentator


class BlackCubeSegmentator(CubeSegmentator):

    def __init__(self):
        self._params = None

    def extract_cube(self, img):
        pass