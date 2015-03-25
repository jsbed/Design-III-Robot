import re
from Robot.question_analysis.matchers.info_matchers import InfoMatcher, NumericInfoMatcher, InfoListMatcher, \
    LengthMatcher, IllicitDrugsActivitiesMatcher, ClimateMatcher, BetweenMatcher

"""
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


class Climate(QuestionMatcher):

    def __init__(self):
        pattern = r'\s?([\w]+) climate'
        info_matcher = ClimateMatcher
        super(Climate, self).__init__(pattern, info_matcher)


class IllicitDrugsActivities(QuestionMatcher):

    def __init__(self):
        pattern = r'illicit drugs activities including a ([\w\s]+)(?: and ).*?'
        info_matcher = IllicitDrugsActivitiesMatcher
        super(IllicitDrugsActivities, self).__init__(pattern, info_matcher)


class ShortCountryNameLength(QuestionMatcher):

    def __init__(self):
        pattern = r'local short country name contains (\d) words.'
        info_matcher = ShortCountryNameLengthMatcher
        super(ShortCountryNameLength, self).__init__(pattern, info_matcher)


class CapitalIs(QuestionMatcher):

    def __init__(self):
        pattern = r'.*country.*has ([\s\w]*) as its capital'
        info_matcher = CapitalFullNameMatcher
        super(CapitalIs, self).__init__(pattern, info_matcher)
"""
##value_matcher for latitude/longitude
#value matcher for date ((?:\w*\s\d*){1,3})
#value matcher national symbol ([\w'\s]+)(?:.|\?| and| is the), shouyld be for all


class QuestionMatcher(object):

    def __init__(self, pattern, info_matcher, attribute):
        self._attribute = attribute
        self._regex = re.compile(pattern, re.IGNORECASE)
        self._info_matcher = info_matcher

    def find_info(self, question):
        info_matcher = None
        match = self._regex.search(question)
        if match:
            info_matcher = self._info_matcher(self._attribute, match.group(1))
        return info_matcher


class QuestionWithListMatcher(QuestionMatcher):
    """
    Matcher class for questions with multiple information joined by conjunctions.
    """

    def __init__(self, attribute, info_key=None):
        descriptors = [r'including(?:.*? of)?', 'include', 'including', 'are', 'of', 'composed by']
        descriptors = '|'.join(descriptors)
        info_key = attribute if not info_key else info_key
        pattern = attribute + r'.* (?:' + descriptors + r') ((?:[\.\w\d\s%]+,\s)*[.\w\d\s%]+,? and [\.\w\d\s%]+)[\?|\.]'
        super(QuestionWithListMatcher, self).__init__(pattern, InfoListMatcher, info_key)

    def find_info(self, question):
        info_matcher = None
        match = self._regex.search(question)
        if match:
            info_list = match.group(1)
            info_list = re.split(', and\s|, |\sand\s', info_list)
            info_matcher = self._info_matcher(self._attribute, info_list)
        return info_matcher


class StartsWithMatcher(QuestionMatcher):

    def __init__(self, attribute):
        self._attribute = attribute
        pattern = 'starts with (?:the letters )?([\w\d,]+)'
        info_matcher = InfoMatcher
        super(StartsWithMatcher, self).__init__(pattern, info_matcher, attribute)

    def find_info(self, question):
        info_matcher = None
        match = self._regex.search(question)
        if match:
            info_matcher = self._info_matcher(self._attribute, r'^' + match.group(1))
        return info_matcher


class EndsWithMatcher(QuestionMatcher):

    def __init__(self, attribute):
        self._attribute = attribute
        pattern = "ends with (?:the letters )?([\w\d']+)"
        info_matcher = InfoMatcher
        super(EndsWithMatcher, self).__init__(pattern, info_matcher, attribute)

    def find_info(self, question):
        info_matcher = None
        match = self._regex.search(question)
        if match:
            info_matcher = self._info_matcher(self._attribute, match.group(1) + r'$')
        return info_matcher


class TextQuestionMatcher(QuestionMatcher):

    def __init__(self, attribute, value_matcher=r"[.\s\w']+"):
        pattern = r'(?:is|has|of|in|on|the) (' + value_matcher + r')(?: as| and| is|\?|\.)?'
        info_matcher = InfoMatcher
        super(TextQuestionMatcher, self).__init__(pattern, info_matcher, attribute)


class Contains(QuestionMatcher):

    def __init__(self, attribute):
        pattern = r'contains (\d) words.'
        info_matcher = LengthMatcher
        super(Contains, self).__init__(pattern, info_matcher, attribute)


class NumericQuestionMatcher(QuestionMatcher):

    def __init__(self, attribute, pattern, op):
        self._op = op
        info_matcher = NumericInfoMatcher
        super(NumericQuestionMatcher, self).__init__(pattern, info_matcher, attribute)

    def find_info(self, question):
        info_matcher = None
        match = self._regex.search(question)
        if match:
            info_matcher = self._info_matcher(self._attribute, match.group(1), self._op)
        return info_matcher


class QuestionWithIntervalMatcher(QuestionMatcher):

    def __init__(self, attribute):
        pattern = r'between ([\d\.\s,]+) and ([\d\.\s,]+)(?: and| is|\?|\.)?'
        info_matcher = BetweenMatcher
        super(QuestionWithIntervalMatcher, self).__init__(pattern, info_matcher, attribute)

    def find_info(self, question):
        info_matcher = None
        match = self._regex.search(question)
        if match:
            lower_bound = match.group(1)
            upper_bound = match.group(2)
            info_matcher = self._info_matcher(self._attribute, lower_bound, upper_bound)
        return info_matcher


class LessThanMatcher(NumericQuestionMatcher):

    def __init__(self, attribute):
        pattern = r'less than ([\d\.\s,]+)(?: and| is|\?|\.)?'
        super(LessThanMatcher, self).__init__(attribute, pattern, '<')


class GreaterThanMatcher(NumericQuestionMatcher):

    def __init__(self, attribute):
        pattern = r'greater than ([\d\.\s,]+)(?: and| is|\?|\.)?'
        super(GreaterThanMatcher, self).__init__(attribute, pattern, '>')


class EqualsMatcher(NumericQuestionMatcher):

    def __init__(self, attribute):
        pattern = r'is (?:approximately )?([\d\.\s,]+)(?: and| is|\?|\.)?'
        super(EqualsMatcher, self).__init__(attribute, pattern, '=')


class LatitudeMatcher(TextQuestionMatcher):

    def __init__(self):
        value_matcher = r'(\d+[\s.]\d+\s[S|N])'
        attribute = 'latitude'
        super(LatitudeMatcher, self).__init__(attribute, value_matcher)


class LongitudeMatcher(TextQuestionMatcher):

    def __init__(self):
        value_matcher = r'(\d+\s\d+\s[E|W])'
        attribute = 'longitude'
        super(LongitudeMatcher, self).__init__(attribute, value_matcher)


class IndependenceMatcher(TextQuestionMatcher):

    def __init__(self):
        value_matcher = r'((?:\w*\s\d*){1,3})'
        attribute = 'independence'
        super(IndependenceMatcher, self).__init__(attribute, value_matcher)


class Climate(QuestionMatcher):

    def __init__(self):
        pattern = r'\s?([\w]+) climate'
        attribute = 'climate'
        info_matcher = ClimateMatcher
        super(Climate, self).__init__(pattern, info_matcher, attribute)


class NationalAnthemComposedBy(QuestionWithListMatcher):

    def __init__(self):
        attribute = 'national anthem'
        info_key = 'national anthem compositors'
        super(NationalAnthemComposedBy, self).__init__(attribute, info_key)


class EthnicGroups(QuestionWithListMatcher):

    def __init__(self):
        attribute = 'ethnic groups'
        info_key = 'religions'
        super(EthnicGroups, self).__init__(attribute, info_key)

    def find_info(self, question):
        info_matcher = None
        match = self._regex.search(question)
        if match:
            info_list = match.group(1)
            print(self._regex)
            info_list = info_list.replace(' of ', ' ').replace('%', '')
            info_list = re.split(', and\s|, |\sand\s', info_list)
            info_list = [info.split()[1] + ' ' + info.split()[0] for info in info_list]
            info_matcher = self._info_matcher(self._attribute, info_list)
        return info_matcher


class IllicitDrugsActivities(QuestionMatcher):

    def __init__(self):
        pattern = r'illicit drugs activities including a ([\w\s]+)(?: and ).*?'
        info_matcher = IllicitDrugsActivitiesMatcher
        attribute = 'illicit drugs'
        super(IllicitDrugsActivities, self).__init__(pattern, info_matcher, attribute)


class QuestionMatcherGenerator(object):

    def __init__(self):

        self._attributes_with_exception = ['independence', 'illicit drugs', 'climate', 'ethnic groups',
                                           'national anthem']

    def get_question_matchers(self, attribute):

        if attribute not in self._attributes_with_exception:
            return [QuestionWithListMatcher(attribute), StartsWithMatcher(attribute), EndsWithMatcher(attribute),
                    TextQuestionMatcher(attribute), Contains(attribute), QuestionWithIntervalMatcher(attribute),
                    LessThanMatcher(attribute), GreaterThanMatcher(attribute), EqualsMatcher(attribute)]