from Robot.locators.segmentation.cube_segmentation import CubeSegmentor


class BlackCubeSegmentor(CubeSegmentor):

    def extract_cube(self, img):
        return img
