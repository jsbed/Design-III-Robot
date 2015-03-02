from Robot.question_analysis.matchers.national_symbol_matchers.symbol_info_matchers import NationalSymbolIsMatcher
from Robot.question_analysis.matchers.national_symbol_matchers.symbol_info_matchers import OneOfNationalSymbolIsMatcher
from Robot.question_analysis.matchers.question_matchers import QuestionMatcher


class OneOfNationalSymbolIs(QuestionMatcher):

    def __init__(self):
        pattern = r"one national symbol.* is the ([\w'\s]+)(?:.|\?| and)"
        info_matcher = OneOfNationalSymbolIsMatcher
        super(OneOfNationalSymbolIs, self).__init__(pattern, info_matcher)


class NationalSymbolIs(QuestionMatcher):

    def __init__(self):
        pattern = r"national symbol.* is the ([\w'\s]+)(?:.|\?| and)"
        info_matcher = NationalSymbolIsMatcher
        super(NationalSymbolIs, self).__init__(pattern, info_matcher)


class IsTheNationalSymbol(QuestionMatcher):

    def __init__(self):
        pattern = r"The ([\w\s']+) is the national symbol"
        info_match = OneOfNationalSymbolIsMatcher
        super(IsTheNationalSymbol, self).__init__(pattern, info_match)