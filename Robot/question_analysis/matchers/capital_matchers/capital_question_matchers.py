import re

from Robot.question_analysis.matchers.capital_matchers.capital_info_matchers import CapitalFullNameMatcher
from Robot.question_analysis.matchers.capital_matchers.capital_info_matchers import CapitalPrefixMatcher
from Robot.question_analysis.matchers.capital_matchers.capital_info_matchers import CapitalSuffixMatcher


class CapitalIs(object):

    def __init__(self):
        self._regex = re.compile('.*country.*has (\w*).*capital')

    def find_info(self, question):
        capital_match = self._regex.search(question)
        answer_matcher = None
        if capital_match:
            answer_matcher = CapitalFullNameMatcher(capital_match.group(1))
        return answer_matcher


class CapitalStartsWith(object):

    def __init__(self):
        self._regex = re.compile('.*capital.*starts with (\w*)')

    def find_info(self, question):
        info_matcher = None
        capital_match = self._regex.search(question)
        if capital_match:
            info_matcher = CapitalPrefixMatcher(capital_match.group(1))
        return info_matcher


class CapitalEndsWith(object):

    def __init__(self):
        self._regex = re.compile('.*capital.*ends with (\w+)')

    def find_info(self, question):
        info_matcher = None
        capital_match = self._regex.search(question)
        if capital_match:
            info_matcher = CapitalSuffixMatcher(capital_match.group(1))
        return info_matcher
