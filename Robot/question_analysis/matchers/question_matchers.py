import re

from Robot.question_analysis.matchers.info_matchers import UrbanAreasMatcher, UnemploymentRateMatcher, ReligionsMatcher, \
    NationalAnthemMatcher
from Robot.question_analysis.matchers.info_matchers import TotalAreaMatcher


class QuestionMatcher(object):

    def __init__(self, pattern, info_matcher):
        self._regex = re.compile(pattern, re.IGNORECASE)
        self._info_matcher = info_matcher

    def find_info(self, question):
        info_matcher = None
        match = self._regex.search(question)
        if match:
            info_matcher = self._info_matcher(match.group(1))
        return info_matcher


class QuestionWithListMatcher(QuestionMatcher):
    """
    Matcher class for questions with multiple information joined by conjunctions.
    """

    def __init__(self, pattern, info_matcher):
        super(QuestionWithListMatcher, self).__init__(pattern, info_matcher)

    def find_info(self, question):
        info_matcher = None
        match = self._regex.search(question)
        if match:
            info_list = match.group(1)
            info_list = re.split(', |\sand\s|and\s', info_list)
            info_matcher = self._info_matcher(info_list)
        return info_matcher


class QuestionWithIntervalMatcher(QuestionMatcher):

    def __init__(self, pattern, info_matcher):
        super(QuestionWithIntervalMatcher, self).__init__(pattern, info_matcher)

    def find_info(self, question):
        info_matcher = None
        match = self._regex.search(question)
        if match:
            lower_bound = match.group(1)
            upper_bound = match.group(2)
            info_matcher = self._info_matcher(lower_bound, upper_bound)
        return info_matcher


class UnemploymentRateIs(QuestionMatcher):

    def __init__(self):
        pattern = r'unemployment rate is ([\d.]+)%'
        info_matcher = UnemploymentRateMatcher
        super(UnemploymentRateIs, self).__init__(pattern, info_matcher)


class UrbanAreasAre(QuestionWithListMatcher):

    def __init__(self):
        pattern = r'major urban areas.*(?:are|is) ((?:[\w\s,]+) and (?:[\w]+))'
        info_matcher = UrbanAreasMatcher
        super(UrbanAreasAre, self).__init__(pattern, info_matcher)


class ReligionsAre(QuestionWithListMatcher):

    def __init__(self):
        pattern = r'religions.*(?:including) ((?:[\w\s,]+) and (?:[\w]+))'
        info_matcher = ReligionsMatcher
        super(ReligionsAre, self).__init__(pattern, info_matcher)


class TotalAreaIs(QuestionMatcher):

    def __init__(self):
        pattern = r'total area of ([\d,]+) sq km'
        info_matcher = TotalAreaMatcher
        super(TotalAreaIs, self).__init__(pattern, info_matcher)


class NationalAnthemIs(QuestionMatcher):

    def __init__(self):
        pattern = r"national anthem is ([\w\s]+)"
        info_matcher = NationalAnthemMatcher
        super(NationalAnthemIs, self).__init__(pattern, info_matcher)