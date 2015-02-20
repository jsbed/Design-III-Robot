import re
from Robot.question_analysis.answer_matchers import CapitalFullNameMatcher, CapitalSuffixMatcher, CapitalPrefixMatcher


class Matchers(object):

    def __init__(self):
        self._matchers = [CapitalIs(), CapitalStartsWith(), CapitalEndsWith()]

    def __iter__(self):
        return iter(self._matchers)


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
        answer_matcher = None
        capital_match = self._regex.search(question)
        if capital_match:
            answer_matcher = CapitalPrefixMatcher(capital_match.group(1))
        return answer_matcher


class CapitalEndsWith(object):

    def __init__(self):
        self._info_name = 'capital'
        self._regex = re.compile('.*capital.*ends with (\w+)')

    def find_info(self, question):
        answer_matcher = None
        capital_match = self._regex.search(question)
        if capital_match:
            answer_matcher = CapitalSuffixMatcher(self._info_name, capital_match.group(1))
        return answer_matcher