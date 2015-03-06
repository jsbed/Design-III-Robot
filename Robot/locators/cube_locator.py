from Robot.locators.contour import contours_finder
from Robot.locators.extractors import cube_extractor_factory
from Robot.resources import camera


def localize(cube):
    original_image = camera.get_data()
    extractor = cube_extractor_factory.create_cube_extractor(cube.get_color())
    extracted_cube = extractor.extract_cube(original_image)

    contours = contours_finder.find_contours(extracted_cube)

    # TODO : EXTRACT CUBE LOCALIZATION
