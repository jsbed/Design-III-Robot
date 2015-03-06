from Robot.locators.extractors.cube_extractor import CubeExtractor
from Robot.locators.segmentation.red_cube_segmentor import RedCubeSegmentor


class RedCubeExtractor(CubeExtractor):

    def extract_cube(self, img):
        return RedCubeSegmentor().segment_cube(img)
