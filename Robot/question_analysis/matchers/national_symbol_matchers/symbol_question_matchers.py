import re

from Robot.question_analysis.matchers.national_symbol_matchers.symbol_info_matchers import NationalSymbolMatcher
class NationalSymbolIs(object):

    def __init__(self):
        self._regex = re.compile("national symbol.* is the ([\w'\s]+)(?:.|\?)")

    def find_info(self, question):
        info_matcher = None
        symbol_match = self._regex.search(question)
        if symbol_match:
            info_matcher = NationalSymbolMatcher(symbol_match.group(1))
        return info_matcher

