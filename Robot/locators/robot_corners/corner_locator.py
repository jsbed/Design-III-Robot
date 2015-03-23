import cv2
import numpy
import os

from Robot.configuration.config import Config
from Robot.cycle.objects.color import Color
from Robot.locators.contour import contours_finder
from Robot.locators.extractors.robot_corner import robot_corner_extractor_factory
from Robot.locators.perspective import perspective_transformation
from Robot.locators.robot_corners.robot_corner import RobotCorner
from Robot.path_finding.point import Point


def locate(img_bgr, img_cloud):
    corners = []

    try:  # Try extracting a blue corner
        blue_corner = _extract_robot_corner_position(
            img_bgr, img_cloud, Color.BLUE)

        corners.append(RobotCorner(blue_corner, Color.BLUE))
    except:
        pass

    try:  # Try extracting a orange corner
        orange_corner = _extract_robot_corner_position(
            img_bgr, img_cloud, Color.ORANGE)

        corners.append(RobotCorner(orange_corner, Color.ORANGE))
    except:
        pass

    try:  # Try extracting a pink corner
        pink_corner = _extract_robot_corner_position(
            img_bgr, img_cloud, Color.PINK)

        corners.append(RobotCorner(pink_corner, Color.PINK))
    except:
        pass

    corners.sort(key=lambda corner: corner[0][1])

    if len(corners) < 2:
        raise Exception("Not enough robot corners found.")
    else:
        return corners[0], corners[1]


def _extract_robot_corner_position(img_bgr, img_cloud, color):
    extractor = robot_corner_extractor_factory.create_robot_corner_extractor(
        color)

    robot_corner = extractor.extract(img_bgr)
    corner_contours = contours_finder.find_contours(robot_corner)

    if len(corner_contours) == 1:
        return _find_corner_position_from_contour(corner_contours, img_cloud)
    elif len(corner_contours) == 2:
        point_a = _find_corner_position_from_contour(corner_contours[0],
                                                     img_cloud)
        point_b = _find_corner_position_from_contour(corner_contours[1],
                                                     img_cloud)

        # Returns the closest point
        return point_a if point_a.y < point_b.y else point_b

    else:
        raise Exception("Corner not found")


def _find_corner_position_from_contour(contour, img_cloud):
    new_contour = numpy.squeeze(numpy.concatenate(contour))
    moments = cv2.moments(new_contour)
    centroid_x = int(moments['m10'] / moments['m00'])
    centroid_y = int(moments['m01'] / moments['m00'])
    new_point = perspective_transformation.transform(img_cloud[centroid_y,
                                                               centroid_x])

    return Point(new_point[0] * 100, new_point[1] * 100 + Config().
                 get_robot_corner_size())


Config("../../../config.ini").load_config()

img_bgr = cv2.imread("ss_98.jpg")
img_cloud = numpy.load("ss_98_p.npy")

table_mask = cv2.imread(os.path.join("..", "..", "resources",
                                     Config().get_kinect_mask_img_path()), 0)

img_bgr = cv2.bitwise_and(img_bgr, img_bgr, mask=table_mask)

color = Color.PINK

pink_corner = _extract_robot_corner_position(
    img_bgr, img_cloud, color)

extractor = robot_corner_extractor_factory.create_robot_corner_extractor(
    color)

robot_corner = extractor.extract(img_bgr)
corner_contour = contours_finder.find_contours(robot_corner)

# print(numpy.squeeze(numpy.concatenate(corner_contour)))

moments = cv2.moments(numpy.squeeze(numpy.concatenate(corner_contour[1])))
centroid_x = int(moments['m10'] / moments['m00'])
centroid_y = int(moments['m01'] / moments['m00'])

copy = robot_corner.copy()
cv2.drawContours(copy, corner_contour, -1, (0, 255, 0), 1)
copy[(centroid_y, centroid_x)] = (255, 0, 0)

print(locate(img_bgr, img_cloud))

while(1):
    cc = cv2.waitKey(1)

    cv2.imshow("test", img_bgr)
    #cv2.imshow("test2", robot_corner)
    #cv2.imshow("test3", copy)

    if cc == 1048603:  # ESC
        break
