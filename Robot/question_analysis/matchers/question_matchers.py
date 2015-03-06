import re

from Robot.question_analysis.matchers.info_matchers import UrbanAreasMatcher, UnemploymentRateMatcher, ReligionsMatcher, \
    NationalAnthemMatcher, IndustriesMatcher, InternetUsersMatcher, LanguagesMatcher, ImportPartnersMatcher, \
    PublicDebtMatcher
from Robot.question_analysis.matchers.info_matchers import TotalAreaMatcher


class QuestionMatcher(object):

    def __init__(self, pattern, info_matcher):
        self._regex = re.compile(pattern, re.IGNORECASE)
        self._info_matcher = info_matcher

    def find_info(self, question):
        info_matcher = None
        match = self._regex.search(question)
        if match:
            info_matcher = self._info_matcher(match.group(1))
        return info_matcher


class QuestionWithListMatcher(QuestionMatcher):
    """
    Matcher class for questions with multiple information joined by conjunctions.
    """

    def __init__(self, pattern, info_matcher):
        super(QuestionWithListMatcher, self).__init__(pattern, info_matcher)

    def find_info(self, question):
        info_matcher = None
        match = self._regex.search(question)
        if match:
            info_list = match.group(1)
            print(info_list)
            info_list = re.split(', and\s|, |\sand\s', info_list)
            print(info_list)
            info_matcher = self._info_matcher(info_list)
        return info_matcher


class QuestionWithIntervalMatcher(QuestionMatcher):

    def __init__(self, pattern, info_matcher):
        super(QuestionWithIntervalMatcher, self).__init__(pattern, info_matcher)

    def find_info(self, question):
        info_matcher = None
        match = self._regex.search(question)
        if match:
            lower_bound = match.group(1)
            upper_bound = match.group(2)
            info_matcher = self._info_matcher(lower_bound, upper_bound)
        return info_matcher


class UnemploymentRateIs(QuestionMatcher):

    def __init__(self):
        pattern = r'unemployment rate is ([\d.]+)%'
        info_matcher = UnemploymentRateMatcher
        super(UnemploymentRateIs, self).__init__(pattern, info_matcher)


class IndustriesInclude(QuestionWithListMatcher):

    def __init__(self):
        pattern = r'industries (?:include|including) .*?\s?((?:[\w]+,\s)*[\w]+ and [\w]+)'
        info_matcher = IndustriesMatcher
        super(IndustriesInclude, self).__init__(pattern, info_matcher)


class UrbanAreasAre(QuestionWithListMatcher):

    def __init__(self):
        pattern = r'major urban areas.*? (?:are|is) .*?\s?((?:[\w]+,\s)*[\w]+ and [\w]+)'
        info_matcher = UrbanAreasMatcher
        super(UrbanAreasAre, self).__init__(pattern, info_matcher)


class ReligionsAre(QuestionWithListMatcher):

    def __init__(self):
        pattern = r'religions.*? (?:including) .*?\s?((?:[\w]+,\s)*[\w]+,? and [\w]+)'
        info_matcher = ReligionsMatcher
        super(ReligionsAre, self).__init__(pattern, info_matcher)


class LanguagesInclude(QuestionWithListMatcher):

    def __init__(self):
        pattern = r'languages.*? (?:include) .*?\s?((?:[\w]+,\s)*[\w]+ and [\w]+)'
        info_matcher = LanguagesMatcher
        super(LanguagesInclude, self).__init__(pattern, info_matcher)


class ImportPartners(QuestionWithListMatcher):

    def __init__(self):
        pattern = r'import partners.*? (?:include) .*?\s?((?:[\w]+,\s)*[\w]+\sand\s[\w]+)'
        info_matcher = ImportPartnersMatcher
        super(ImportPartners, self).__init__(pattern, info_matcher)


class TotalAreaIs(QuestionMatcher):

    def __init__(self):
        pattern = r'total area of ([\d,]+) sq km'
        info_matcher = TotalAreaMatcher
        super(TotalAreaIs, self).__init__(pattern, info_matcher)


class NationalAnthemIs(QuestionMatcher):

    def __init__(self):
        pattern = r"national anthem is ([\w\s]+)"
        info_matcher = NationalAnthemMatcher
        super(NationalAnthemIs, self).__init__(pattern, info_matcher)


class InternetUsers(QuestionMatcher):

    def __init__(self):
        pattern = r'([\w\d,.]+(?:\smillion)?) internet users'
        info_matcher = InternetUsersMatcher
        super(InternetUsers, self).__init__(pattern, info_matcher)


class PublicDebt(QuestionMatcher):

    def __init__(self):
        pattern = r'public debt is ([\d.]+%)'
        info_matcher = PublicDebtMatcher
        super(PublicDebt, self).__init__(pattern, info_matcher)