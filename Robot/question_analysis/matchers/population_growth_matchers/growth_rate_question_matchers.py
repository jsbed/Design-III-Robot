import re

from Robot.question_analysis.matchers.population_growth_matchers.growth_rate_info_matchers import GrowthRateMatcher
from Robot.question_analysis.matchers.population_growth_matchers.growth_rate_info_matchers import GrowthRateBetweenMatcher
from Robot.question_analysis.matchers.question_matchers import QuestionWithIntervalMatcher, QuestionMatcher


class GrowthRateOf(QuestionMatcher):

    def __init__(self):
        pattern = r'population growth rate of ([\d.]+)%'
        info_matcher = GrowthRateMatcher
        super(GrowthRateOf, self).__init__(pattern, info_matcher)


class GrowthRateBetween(QuestionWithIntervalMatcher):

    def __init__(self):
        pattern = r'population growth rate is between ([\d.]+)% and ([\d.]+)%'
        info_matcher = GrowthRateBetweenMatcher
        super(GrowthRateBetween, self).__init__(pattern, info_matcher)