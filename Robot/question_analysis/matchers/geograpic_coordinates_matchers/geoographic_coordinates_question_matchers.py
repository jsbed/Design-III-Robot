import re
from Robot.question_analysis.matchers.geograpic_coordinates_matchers.geographic_coordinates_info_matcher import \
    GeographicCoordinatesMatcher


class LatitudeIs(object):

    def __init__(self):
        self._regex = re.compile('latitude (?:is|of) (\d+[\s.]\d+\s[S|N])')

    def find_info(self, question):
        info_matcher = None
        latitude_match = self._regex.search(question)
        if latitude_match:
            latitude = latitude_match.group(1)
            info_matcher = GeographicCoordinatesMatcher(latitude)
        return info_matcher


class LongitudeIs(object):

    def __init__(self):
        self._regex = re.compile('longitude (?:is|of) (\d+\s\d+\s[E|W])')

    def find_info(self, question):
        info_matcher = None
        longitude_match = self._regex.search(question)
        if longitude_match:
            longitude = longitude_match.group(1)
            info_matcher = GeographicCoordinatesMatcher(longitude)
        return info_matcher