from Robot.locators.location_computer import robot_location_computer
from Robot.locators.robot_corners import corner_locator
from Robot.resources.kinect import Kinect


def localize():
    img_bgr, img_cloud_map = Kinect.get_data()
    close_corner, far_corner = corner_locator.locate(img_bgr, img_cloud_map)

    return robot_location_computer.compute(close_corner, far_corner)
