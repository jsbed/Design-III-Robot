import re

from Robot.question_analysis.matchers.independence_date_matchers.independence_info_matcher import IndependenceDateMatcher
from Robot.question_analysis.matchers.question_matchers import QuestionMatcher


class IsTheDateOfIndependence(QuestionMatcher):

    def __init__(self):
        pattern = r'([\w\s]+) is the date of independence'
        info_matcher = IndependenceDateMatcher
        super(IsTheDateOfIndependence, self).__init__(pattern, info_matcher)


class DeclaredIndependenceOn(QuestionMatcher):

    def __init__(self):
        pattern = r'declared its independence on ((?:\w*\s\d*){1,3})'
        info_matcher = IndependenceDateMatcher
        super(DeclaredIndependenceOn, self).__init__(pattern, info_matcher)


class IndependenceDeclaredIn(QuestionMatcher):

    def __init__(self):
        pattern = r'independence was declared in ((?:\w*\s\d*){1,3})'
        info_matcher = IndependenceDateMatcher
        super(IndependenceDeclaredIn, self).__init__(pattern, info_matcher)


class InDeclaredIndependence(QuestionMatcher):

    def __init__(self):
        pattern = r'In ([\w\s]+),? we proclaimed our independence'
        info_matcher = IndependenceDateMatcher
        super(InDeclaredIndependence, self).__init__(pattern, info_matcher)
