from Robot.locators.contour import contours_finder
from Robot.locators.extractors.cube import cube_extractor_factory
from Robot.locators.localization import Localization
from Robot.locators.location_computer import cube_location_computer
from Robot.resources.camera import Camera
from Robot.resources.kinect import Kinect


def localize_with_camera(cube_color):
    original_image = Camera().get_data()
    extractor = cube_extractor_factory.create_cube_extractor(cube_color)
    extracted_cube = extractor.extract_cube(original_image)

    contours = contours_finder.find_contours(extracted_cube)

    # TODO : EXTRACT CUBE LOCALIZATION


# Does not work with a White or Black cube
def localize_with_kinect(cube_color):
    try:
        img_bgr, img_cloud = Kinect().get_data()
        cube_extractor = cube_extractor_factory.create_cube_extractor(
            cube_color)
        extracted_cube = cube_extractor.extract_cube(img_bgr)

        return cube_location_computer.compute(extracted_cube, img_cloud)
    except:
        return Localization(None, None, unknown=True)
