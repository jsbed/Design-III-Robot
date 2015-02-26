import re

from Robot.question_analysis.matchers.population_growth_matchers.growth_rate_info_matchers import GrowthRateMatcher
from Robot.question_analysis.matchers.population_growth_matchers.growth_rate_info_matchers import GrowthRateBetweenMatcher


class GrowthRateOf(object):

    def __init__(self):
        self._regex = re.compile('population growth rate of ([\d.]+)%')

    def find_info(self, question):
        info_matcher = None
        growth_match = self._regex.search(question)
        if growth_match:
            growth_rate = growth_match.group(1)
            info_matcher = GrowthRateMatcher(growth_rate)
        return info_matcher


class GrowthRateBetween(object):

    def __init__(self):
        self._regex = re.compile('population growth rate is between ([\d.]+)% and ([\d.]+)%')

    def find_info(self, question):
        info_matcher = None
        growth_match = self._regex.search(question)
        if growth_match:
            growth_rate_lower_bound = growth_match.group(1)
            growth_rate_upper_bound = growth_match.group(2)
            info_matcher = GrowthRateBetweenMatcher(growth_rate_lower_bound, growth_rate_upper_bound)
        return info_matcher
