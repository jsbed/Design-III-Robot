from Robot.locators.location_computer import robot_location_computer
from Robot.locators.robot_corners import corner_locator
from Robot.resources import kinect


def localize():
    img = kinect.get_data()
    close_corner, far_corner = corner_locator.locate(img)

    return robot_location_computer.compute(close_corner, far_corner)
