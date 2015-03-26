import re
from Robot.question_analysis.matchers.info_matchers import InfoMatcher


class BirthRateMatcher(InfoMatcher):

    def __init__(self, birth_rate):
        info_key = 'birth rate'
        regex = re.compile(birth_rate)
        super(BirthRateMatcher, self).__init__(info_key, regex)