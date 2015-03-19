import re

from Robot.question_analysis.matchers.info_matchers import UrbanAreasMatcher, UnemploymentRateMatcher, ReligionsMatcher, \
    NationalAnthemMatcher, IndustriesMatcher, InternetUsersMatcher, LanguagesMatcher, ImportPartnersMatcher, \
    PublicDebtMatcher, NationalAnthemCompositorsMatcher, InfoListMatcher, InfoMatcher, ClimateMatcher, \
    ShortCountryNameLengthMatcher, IllicitDrugsActivitiesMatcher
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

    def __init__(self, attribute, descriptors, info_key=None):
        descriptors = '|'.join(descriptors)
        self._info_key = attribute if not info_key else info_key
        pattern = attribute + r'.* (?:' + descriptors + r') ((?:[.\w\d\s%]+,\s)*[.\w\d\s%]+,? and [.\w\d\s%]+)[\?|\.]'
        print(pattern)
        super(QuestionWithListMatcher, self).__init__(pattern, InfoListMatcher)

    def find_info(self, question):
        info_matcher = None
        match = self._regex.search(question)
        if match:
            info_list = match.group(1)
            print(info_list)
            info_list = re.split(', and\s|, |\sand\s', info_list)
            info_matcher = self._info_matcher(self._info_key, info_list)
            print(info_matcher._regex)
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
        descriptors = [r'including(?:.*? of)?', 'include']
        attribute = 'industries'
        super(IndustriesInclude, self).__init__(attribute, descriptors)


class UrbanAreasAre(QuestionWithListMatcher):

    def __init__(self):
        descriptors = ['are']
        attribute = 'major urban areas'
        super(UrbanAreasAre, self).__init__(attribute, descriptors)


class PopulationUrbanAreasAre(QuestionWithListMatcher):

    def __init__(self):
        descriptors = ['of']
        attribute = 'major urban areas'
        super(PopulationUrbanAreasAre, self).__init__(attribute, descriptors)


class ReligionsAre(QuestionWithListMatcher):

    def __init__(self):
        descriptors = ['including']
        attribute = 'religions'
        super(ReligionsAre, self).__init__(attribute, descriptors)


class LanguagesInclude(QuestionWithListMatcher):

    def __init__(self):
        descriptors = ['include']
        attribute = 'languages'
        super(LanguagesInclude, self).__init__(attribute, descriptors)


class ImportPartners(QuestionWithListMatcher):

    def __init__(self):
        descriptors = ['include', 'are']
        attribute = 'import partners'
        super(ImportPartners, self).__init__(attribute, descriptors)


class ExportPartners(QuestionWithListMatcher):

    def __init__(self):
        descriptors = ['include', 'are']
        attribute = 'export partners'
        super(ExportPartners, self).__init__(attribute, descriptors)


class NationalAnthemComposedBy(QuestionWithListMatcher):

    def __init__(self):
        descriptors = ['composed by']
        attribute = 'national anthem'
        info_key = 'national anthem compositors'
        super(NationalAnthemComposedBy, self).__init__(attribute, descriptors, info_key)


class EthnicGroups(QuestionWithListMatcher):

    def __init__(self):
        descriptors = ['including']
        attribute = 'ethnic groups'
        info_key = 'religions'
        super(EthnicGroups, self).__init__(attribute, descriptors, info_key)

    def find_info(self, question):
        info_matcher = None
        match = self._regex.search(question)
        if match:
            info_list = match.group(1)
            print(self._regex)
            info_list = info_list.replace(' of ', ' ').replace('%', '')
            info_list = re.split(', and\s|, |\sand\s', info_list)
            info_list = [info.split()[1] + ' ' + info.split()[0] for info in info_list]
            info_matcher = self._info_matcher(self._info_key, info_list)
        return info_matcher


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


class Climate(QuestionMatcher):

    def __init__(self):
        pattern = r'\s?([\w]+) climate'
        info_matcher = ClimateMatcher
        super(Climate, self).__init__(pattern, info_matcher)


class ShortCountryNameLength(QuestionMatcher):

    def __init__(self):
        pattern = r'local short country name contains (\d) words.'
        info_matcher = ShortCountryNameLengthMatcher
        super(ShortCountryNameLength, self).__init__(pattern, info_matcher)


class IllicitDrugsActivities(QuestionMatcher):

    def __init__(self):
        pattern = r'illicit drugs activities including a ([\w\s]+)(?: and ).*?'
        info_matcher = IllicitDrugsActivitiesMatcher
        super(IllicitDrugsActivities, self).__init__(pattern, info_matcher)