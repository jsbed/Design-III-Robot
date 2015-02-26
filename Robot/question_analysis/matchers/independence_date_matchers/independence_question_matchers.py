import re

from Robot.question_analysis.matchers.independence_date_matchers.independence_info_matcher import IndependenceDateMatcher


class IsTheDateOfIndependence(object):

    def __init__(self):
        self._regex = re.compile('([\w\s]+) is the date of independence')

    def find_info(self, question):
        info_matcher = None
        independence_date_match = self._regex.search(question)
        if independence_date_match:
            date = independence_date_match.group(1)
            info_matcher = IndependenceDateMatcher(date)
        return info_matcher


class DeclaredIndependenceOn(object):

    def __init__(self):
        self._regex = re.compile('declared its independence on ((?:\w*\s\d*){1,3})')

    def find_info(self, question):
        info_matcher = None
        independence_date_match = self._regex.search(question)
        if independence_date_match:
            date = independence_date_match.group(1)
            info_matcher = IndependenceDateMatcher(date)
        return info_matcher


class IndependenceDeclaredIn(object):

    def __init__(self):
        self._regex = re.compile('independence was declared in ((?:\w*\s\d*){1,3})')

    def find_info(self, question):
        info_matcher = None
        independence_date_match = self._regex.search(question)
        if independence_date_match:
            date = independence_date_match.group(1)
            info_matcher = IndependenceDateMatcher(date)
        return info_matcher