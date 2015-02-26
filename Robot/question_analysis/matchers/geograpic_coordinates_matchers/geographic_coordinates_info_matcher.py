import re

from Robot.question_analysis.matchers.info_matchers import InfoMatcher


class GeographicCoordinatesMatcher(InfoMatcher):

    def __init__(self, latitude):
        regex = re.compile(latitude)
        info_key = 'geographic coordinates'
        super(GeographicCoordinatesMatcher, self).__init__(info_key, regex)
