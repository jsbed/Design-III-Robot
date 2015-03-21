from Robot.question_analysis.matchers.death_rate_matchers.death_rate_info_matcher import DeathRateGreaterThanMatcher, \
    DeathRateLessThanMatcher
from Robot.question_analysis.matchers.question_matchers import QuestionMatcher


class DeathRateGreaterThan(QuestionMatcher):

    def __init__(self):
        pattern = r'death rate .* greater than ([\d.]+) death[s]?\/1000'
        info_matcher = DeathRateGreaterThanMatcher
        super(DeathRateGreaterThan, self).__init__(pattern, info_matcher)


class DeathRateLessThan(QuestionMatcher):

    def __init__(self):
        pattern = r'death rate .* less than ([\d.]+) death[s]?\/1000'
        info_matcher = DeathRateLessThanMatcher
        super(DeathRateLessThan, self).__init__(pattern, info_matcher)