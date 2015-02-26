import re

from Robot.question_analysis.matchers.info_matchers import InfoMatcher


class IndependenceDateMatcher(InfoMatcher):

    def __init__(self, date):
        info_key = 'independence date'
        regex = re.compile(date)
        super(IndependenceDateMatcher, self).__init__(info_key, regex)