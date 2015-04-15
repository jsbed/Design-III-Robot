import numpy

from Robot.configuration.config import Config
from Robot.cycle.objects.color import Color
from Robot.locators.contour import contours_finder
from Robot.locators.extractors.robot_corner import robot_corner_extractor_factory
from Robot.locators.perspective import perspective_transformation
from Robot.locators.robot_corners.robot_corner import RobotCorner
from Robot.path_finding.point import Point, Point3D


def locate(img_bgr, img_cloud):
    corners = []

    _try_extracting_robot_corner_for_specific_color(
        corners, img_bgr, img_cloud, Color.BLUE)
    _try_extracting_robot_corner_for_specific_color(
        corners, img_bgr, img_cloud, Color.ORANGE)
    _try_extracting_robot_corner_for_specific_color(
        corners, img_bgr, img_cloud, Color.PINK)
    _try_extracting_robot_corner_for_specific_color(
        corners, img_bgr, img_cloud, Color.CYAN)

    print(corners)

    corners.sort(key=lambda corner: corner[0][1])

    if len(corners) < 2:
        raise Exception("Not enough robot corners found.")
    else:
        return corners[0], corners[1]


def _try_extracting_robot_corner_for_specific_color(corners, img_bgr,
                                                    img_cloud, color):
    try:
        corner = _extract_robot_corner_position(
            img_bgr, img_cloud, color)

        corners.append(RobotCorner(corner, color))
    except:
        pass


def _extract_robot_corner_position(img_bgr, img_cloud, color):
    extractor = robot_corner_extractor_factory.create_robot_corner_extractor(
        color)

    robot_corner = extractor.extract(img_bgr)
    corner_contours = contours_finder.find_extracted_shape_contour(
        robot_corner)

    if len(corner_contours) == 1:
        return _find_corner_position_from_contour(corner_contours, img_cloud)
    elif len(corner_contours) >= 2:
        points = []

        for contour in corner_contours:
            points.append(_find_corner_position_from_contour(contour,
                                                             img_cloud))

        points.sort(key=lambda point: point.z, reverse=True)

        # Returns the highest point
        return Point(points[0].x, points[0].y)

    else:
        raise Exception("Corner not found")


def _find_corner_position_from_contour(contour, img_cloud):
    new_contour = numpy.squeeze(numpy.concatenate(contour))
    x, y = contours_finder.get_central_pixel_from_contour(new_contour)

    new_point = perspective_transformation.transform(img_cloud[y, x])

    return Point3D(new_point[0] * 100, new_point[1] * 100 +
                   Config().get_robot_corner_size(), new_point[2])
