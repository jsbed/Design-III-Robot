import re

from Robot.question_analysis.matchers.national_symbol_matchers.symbol_info_matchers import NationalSymbolIsMatcher
from Robot.question_analysis.matchers.national_symbol_matchers.symbol_info_matchers import OneOfNationalSymbolIsMatcher
from Robot.question_analysis.matchers.national_symbol_matchers.symbol_info_matchers import IsTheNationalSymbolMatcher


class OneOfNationalSymbolIs(object):

    def __init__(self):
        self._regex = re.compile("one national symbol.* is the ([\w'\s]+)(?:.|\?| and)", re.IGNORECASE)

    def find_info(self, question):
        info_matcher = None
        symbol_match = self._regex.search(question)
        if symbol_match:
            print(symbol_match.group(1))
            info_matcher = OneOfNationalSymbolIsMatcher(symbol_match.group(1))
        return info_matcher


class NationalSymbolIs(object):

    def __init__(self):
        self._regex = re.compile("national symbol.* is the ([\w'\s]+)(?:.|\?| and)")

    def find_info(self, question):
        info_matcher = None
        symbol_match = self._regex.search(question)
        if symbol_match:
            info_matcher = NationalSymbolIsMatcher(symbol_match.group(1))
        return info_matcher


class IsTheNationalSymbol(object):

    def __init__(self):
        self._regex = re.compile("The ([\w\s']+) is the national symbol", re.IGNORECASE)

    def find_info(self, question):
        info_matcher = None
        symbol_match = self._regex.search(question)
        if symbol_match:
            info_matcher = IsTheNationalSymbolMatcher(symbol_match.group(1))
        return info_matcher
