from Robot.question_analysis.matchers.capital_matchers.capital_info_matchers import CapitalFullNameMatcher
from Robot.question_analysis.matchers.capital_matchers.capital_info_matchers import CapitalPrefixMatcher
from Robot.question_analysis.matchers.capital_matchers.capital_info_matchers import CapitalSuffixMatcher
from Robot.question_analysis.matchers.question_matchers import QuestionMatcher, QuestionWithListMatcher


class CapitalIs(QuestionMatcher):

    def __init__(self):
        pattern = r'.*country.*has (\w*).*capital'
        info_matcher = CapitalFullNameMatcher
        super(CapitalIs, self).__init__(pattern, info_matcher)


class CapitalStartsWith(QuestionMatcher):

    def __init__(self):
        pattern = r'.*capital.*starts with (\w*)'
        info_matcher = CapitalPrefixMatcher
        super(CapitalStartsWith, self).__init__(pattern, info_matcher)


class CapitalEndsWith(QuestionMatcher):

    def __init__(self):
        pattern = r'.*capital.*ends with (\w+)'
        info_matcher = CapitalSuffixMatcher
        super(CapitalEndsWith, self).__init__(pattern, info_matcher)
