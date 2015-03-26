from Robot.question_analysis.matchers.birth_rate_matchers.birth_rate_info_matchers import BirthRateMatcher
from Robot.question_analysis.matchers.question_matchers import QuestionMatcher


class BirthRateIs(QuestionMatcher):

    def __init__(self):
        #TODO: closest match
        pattern = r'birth rate .* ([\d.]+) birth[s]?\/[\s]*1000'
        info_matcher = BirthRateMatcher
        super(BirthRateIs, self).__init__(pattern, info_matcher)