from Robot.locators.segmentation.cube_segmentation import CubeSegmentatorFactory
from Robot.resources import Camera


def localize(cube):
    original_image = Camera.get_data()
    segmentator = CubeSegmentatorFactory.create_cube_segmentator(cube.color)
    extracted_cube = segmentator.extract_cube(original_image)

    # TODO : EXTRACT CUBE LOCALIZATION
