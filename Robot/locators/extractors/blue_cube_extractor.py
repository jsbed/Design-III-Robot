from Robot.configuration.config import Config
from Robot.locators.extractors.cube_extractor import CubeExtractor
from Robot.locators.segmentation.cube_segmentation import CubeSegmentor


class BlueCubeExtractor(CubeExtractor):

    def __init__(self):
        self._cube_segmentor = CubeSegmentor()

        self._cube_segmentor.set_lower_hsv_values(
            Config().get_cube_low_blue_hsv_values())
        self._cube_segmentor.set_upper_hsv_values(
            Config().get_cube_high_blue_hsv_values())

    def extract_cube(self, img):
        return self._cube_segmentor.segment_cube(img)
