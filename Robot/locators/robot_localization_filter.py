from statistics import mean

from Robot.configuration.config import Config
from Robot.locators.localization import Localization
from Robot.path_finding.point import Point
from Robot.path_finding.point_adjustor import PointAdjustor
from Robot.utilities.observable import Observable


ROBOT_LOCALIZATION_UPDATED = "Robot localization updated"


class RobotLocalizationFilter(Observable):
    MAX_NUMBER_OF_DATA_POINTS = 5
    DISTANCE_THRESHOLD = 2
    ANGLE_THRESHOLD = 3

    def __init__(self):
        Observable.__init__(self)
        self._robot_localization = Localization(None, None, unknown=True)
        self._last_data_points = []
        self._filtering_new_position = True

    def update_localization(self, localization):
        if (self._validate_localization(localization)):
            self._filter_new_position(localization)

    def get_localization(self):
        return self._robot_localization

    def _filter_new_position(self, localization):
        if (len(self._last_data_points) < self.MAX_NUMBER_OF_DATA_POINTS):
            self._last_data_points.append(localization)

        if (len(self._last_data_points) == self.MAX_NUMBER_OF_DATA_POINTS):
            localization = self._find_mean_localization()
            self._last_data_points.clear()

            if (not localization.unknown):
                if (self._robot_localization.unknown):
                    self._update_localization(localization)
                else:
                    new_distance = PointAdjustor.calculate_distance_between_points(
                        localization.position, self._robot_localization.position)
                    new_orientation = localization.orientation

                    if (self._can_update_new_localization(localization,
                                                          new_distance,
                                                          new_orientation)):
                        self._update_localization(localization)

    def _find_mean_localization(self):
        good_points, wrong_points = self._find_good_and_wrong_points(
            self._last_data_points)

        if len(wrong_points) <= 1:
            self._last_data_points.pop(0)

            return self._compute_mean_localization(good_points)
        elif len(wrong_points) == 4:
            good_points, wrong_points = self._find_good_and_wrong_points(
                wrong_points)

            if len(good_points) == 4:
                self._last_data_points.pop(0)

                return self._compute_mean_localization(good_points)

        return Localization(None, None, unknown=True)

    def _compute_mean_localization(self, localization):
        x = mean([loc.position.x for loc in localization])
        y = mean([loc.position.y for loc in localization])
        orientation = mean([loc.orientation for loc in localization])

        return Localization(Point(x, y), orientation)

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

    def _can_update_new_localization(self, localization, new_distance, new_orientation):
        return (new_distance > self.DISTANCE_THRESHOLD or
                new_orientation > self.ANGLE_THRESHOLD)

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
