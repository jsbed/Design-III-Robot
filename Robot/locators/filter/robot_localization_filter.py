from math import radians, cos, sin, atan2, degrees
from statistics import mean, median

from Robot.configuration.config import Config
from Robot.locators.localization import Localization
from Robot.path_finding.point import Point
from Robot.path_finding.point_adjustor import PointAdjustor
from Robot.utilities.observable import Observable


ROBOT_LOCALIZATION_UPDATED = "Robot localization updated"


class RobotLocalizationFilter(Observable):
    MAX_NUMBER_OF_DATA_POINTS = 5
    DISTANCE_THRESHOLD = 1
    ANGLE_THRESHOLD = 2

    def __init__(self):
        Observable.__init__(self)
        self._robot_localization = Localization(None, None, unknown=True)
        self._last_data_points = []
        self._filtering_new_position = True

    def update_localization(self, localization):
        if (self._validate_localization(localization)):
            print(localization.position, localization.orientation)
            self._filter_new_position(localization)

    def get_localization(self):
        return self._robot_localization

    def _filter_new_position(self, localization):
        if (len(self._last_data_points) < self.MAX_NUMBER_OF_DATA_POINTS):
            self._last_data_points.append(localization)

        if (len(self._last_data_points) == self.MAX_NUMBER_OF_DATA_POINTS):
            localization = self._find_mean_localization()
            self._last_data_points.clear()

            if (self._robot_localization.unknown):
                self._update_localization(localization)
            else:
                new_distance = PointAdjustor.calculate_distance_between_points(
                    localization.position, self._robot_localization.position)
                orientation_diff = self._find_angle_difference(
                    self._robot_localization.orientation,
                    localization.orientation)

                if (self._can_update_new_localization(new_distance,
                                                      orientation_diff)):
                    self._update_localization(localization)

    def _find_mean_localization(self):
        points = [loc.position for loc in self._last_data_points]
        orientations = [loc.orientation for loc in self._last_data_points]
        median_x = median(point.x for point in points)
        median_y = median(point.y for point in points)
        median_orientation = self._find_median_of_orientation(orientations)

        return Localization(Point(median_x, median_y), median_orientation)

    def _get_positions_from_localization(self, localizations):
        return [loc.position for loc in localizations]

    def _compute_mean_localization(self, localization):
        x = mean([loc.position.x for loc in localization])
        y = mean([loc.position.y for loc in localization])
        orientation = self._compute_mean_orientation(
            [loc.orientation for loc in localization])

        return Localization(Point(x, y), orientation)

    def _compute_mean_orientation(self, orientations):
        x, y = 0, 0

        for orientation in orientations:
            x += cos(radians(orientation))
            y += sin(radians(orientation))

        return degrees(atan2(y / len(orientations),
                             x / len(orientations)))

    def _find_median_of_orientation(self, values):
        if all(value < 350 for value in values):
            return median(values)
        else:
            for index, value in enumerate(values):
                if (value < 180):
                    values[index] += 360

            orientation = median(values)

        return orientation if orientation < 360 else orientation - 360

    def _update_localization(self, localization):
        self._robot_localization = localization
        self.notify(ROBOT_LOCALIZATION_UPDATED, localization)

    def _validate_localization(self, localization):
        valid = True
        position = localization.position

        if (localization.unknown):
            valid = False
        elif (position.x > (Config().get_table_width() -
                            Config().get_robot_radius())):
            valid = False
        elif (position.x < Config().get_robot_radius()):
            valid = False
        elif (position.y > (Config().get_table_height() -
                            Config().get_robot_radius())):
            valid = False
        elif (position.y < Config().get_robot_radius()):
            valid = False

        return valid

    def _can_update_new_localization(self, new_distance, orientation_diff):
        return (new_distance > self.DISTANCE_THRESHOLD or
                orientation_diff > self.ANGLE_THRESHOLD)

    def _find_good_and_wrong_points(self, localizations):
        first_point = localizations[0]

        distances = [(PointAdjustor.calculate_distance_between_points(
            loc.position, first_point.position), loc) for loc in
            localizations[1:]]

        wrong_loc = [distance[1] for distance in list(
            filter(lambda x: x[0] > 2 * self.DISTANCE_THRESHOLD, distances))]

        good_loc = [distance[1] for distance in list(
            filter(lambda x: x[0] <= 2 * self.DISTANCE_THRESHOLD, distances))]

        return good_loc, wrong_loc

    def _find_angle_difference(self, a, b):
        distance = abs(a - b) % 360
        return distance if distance <= 180 else 360 - distance
