from Robot.locators.contour import contours_finder
from Robot.locators.extractors.cube import cube_extractor_factory
from Robot.resources.camera import Camera


def localize(cube):
    original_image = Camera().get_data()
    extractor = cube_extractor_factory.create_cube_extractor(cube.get_color())
    extracted_cube = extractor.extract_cube(original_image)

    contours = contours_finder.find_contours(extracted_cube)

    # TODO : EXTRACT CUBE LOCALIZATION
