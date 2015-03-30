from statistics import mean

from Robot.configuration.config import Config
from Robot.locators.localization import Localization
from Robot.path_finding.point import Point
from Robot.path_finding.point_adjustor import PointAdjustor
from Robot.utilities.observable import Observable


ROBOT_LOCALIZATION_UPDATED = "Robot localization updated"


class RobotLocalizationFilter(Observable):
    MAX_NUMBER_OF_DATA_POINTS = 10
    DISTANCE_THRESHOLD = 2
    ANGLE_THRESHOLD = 3

    def __init__(self):
        Observable.__init__(self)
        self._robot_localization = Localization(None, None, unknown=True)
        self._last_data_points = []
        self._filtering_new_position = True

    def update_localization(self, localization):
        if (self._validate_localization(localization)):
            if (self._filtering_new_position):
                self._filter_new_position(localization)
            else:
                self._filter_new_data_point(localization)

    def _filter_first_data_points(self):
        # TODO: algo filter first points
        if (len(self._last_data_points) == self.MAX_NUMBER_OF_DATA_POINTS):
            self._filtering_new_position = False
            localization = self._compute_mean_localization()
            self._update_localization(localization)

    def _filter_new_data_point(self, localization):
        distance_difference = PointAdjustor.calculate_distance_between_points(
            self._robot_localization.position, localization.position)
        angle_difference = PointAdjustor.calculate_angle_between_points(
            self._robot_localization.position, localization.position)

        # TODO: handle new data point
        if (distance_difference > self.DISTANCE_THRESHOLD or
                angle_difference > self.ANGLE_THRESHOLD):
            pass

    def _compute_mean_localization(self):
        x = mean([loc.position.x for loc in self._last_data_points])
        y = mean([loc.position.y for loc in self._last_data_points])
        orientation = mean([loc.orientation for loc in self._last_data_points])

        self._last_data_points.clear()

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
