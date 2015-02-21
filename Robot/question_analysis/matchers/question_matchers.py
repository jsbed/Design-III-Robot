import re

from Robot.question_analysis.matchers.capital_matchers.capital_question_matchers import CapitalIs, CapitalEndsWith
from Robot.question_analysis.matchers.capital_matchers.capital_question_matchers import CapitalStartsWith

from Robot.question_analysis.matchers.info_matchers import UnemploymentRateMatcher
class Matchers(object):

    def __init__(self):
        self._matchers = [CapitalIs(), CapitalStartsWith(), CapitalEndsWith(), UnemploymentRateIs()]

    def __iter__(self):
        return iter(self._matchers)

class UnemploymentRateIs(object):

    def __init__(self):
        self._regex = re.compile('unemployment rate is ([\d.]+)%')

    def find_info(self, question):
        answer_matcher = None
        rate_match = self._regex.search(question)
        if rate_match:
            answer_matcher = UnemploymentRateMatcher(rate_match.group(1))
        return answer_matcher