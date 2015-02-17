from Robot.locators.segmentation.cube_segmentation import CubeSegmentorFactory
from Robot.resources import Camera


def localize(cube):
    original_image = Camera.get_data()
    segmentator = CubeSegmentorFactory.create_cube_segmentor(cube.color)
    extracted_cube = segmentator.extract_cube(original_image)

    # TODO : EXTRACT CUBE LOCALIZATION
