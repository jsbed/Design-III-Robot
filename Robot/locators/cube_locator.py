from Robot.locators.contour import contours_finder
from Robot.locators.segmentation import cube_segmentor_factory
from Robot.resources import Camera


def localize(cube):
    original_image = Camera.get_data()
    segmentor = cube_segmentor_factory.create_cube_segmentor(cube.get_color())
    extracted_cube = segmentor.extract_cube(original_image)

    contours = contours_finder.find_contours(extracted_cube)

    # TODO: Improve localization
