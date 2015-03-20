from Robot.locators.extractors.cube.cube_extractor import CubeExtractor
from Robot.locators.segmentation.cube.red_cube_segmentor import RedCubeSegmentor


class RedCubeExtractor(CubeExtractor):

    def extract_cube(self, img):
        return RedCubeSegmentor().segment_cube(img)
