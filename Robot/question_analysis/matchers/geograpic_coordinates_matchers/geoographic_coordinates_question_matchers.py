import re
from Robot.question_analysis.matchers.geograpic_coordinates_matchers.geographic_coordinates_info_matcher import \
    GeographicCoordinatesMatcher
from Robot.question_analysis.matchers.question_matchers import QuestionMatcher


class LatitudeIs(QuestionMatcher):

    def __init__(self):
        pattern = r'latitude (?:is|of) (\d+[\s.]\d+\s[S|N])'
        info_matcher = GeographicCoordinatesMatcher
        super(LatitudeIs, self).__init__(pattern, info_matcher)


class LongitudeIs(QuestionMatcher):

    def __init__(self):
        pattern = r'longitude (?:is|of) (\d+\s\d+\s[E|W])'
        info_matcher = GeographicCoordinatesMatcher
        super(LongitudeIs, self).__init__(pattern, info_matcher)