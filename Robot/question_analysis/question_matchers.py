import re
from Robot.question_analysis.info_matchers import InfoMatcher, InfoListMatcher, LengthMatcher, BetweenMatcher, \
    NumericInfoMatcher, ClimateMatcher, IllicitDrugsActivitiesMatcher, NumericApproximationInfoMatcher


END_DELIMITERS = [r' and ', r' as ', r' is ', r'\?$', r'\.$', ', ']
BEGIN_DELIMITERS = [r'(?:\s|^)is ', r'(?:\s|^)has ', r'(?:\s|^)of ', r'(?:\s|^)in ', r'(?:\s|^)on ',
                    r'(?:\s|^)the ', r'^']


class QuestionMatcher(object):

    def __init__(self, pattern, info_matcher, attribute):
        self._attribute = attribute
        self._regex = re.compile(pattern, re.IGNORECASE)
        self._info_matcher = info_matcher

    def find_info(self, question):
        return self.get_info_matcher(question)

    def get_match(self, question):
        match = self._regex.search(question)
        if match:
            match = match.group(1)
        return match

    def get_info_matcher(self, question):
        info_matcher = None
        match = self.get_match(question)
        if match:
            info_matcher = self._info_matcher(self._attribute, match)
        return info_matcher


class QuestionWithListMatcher(QuestionMatcher):
    """
    Matcher class for questions with multiple information joined by conjunctions.
    """

    def __init__(self, attribute, info_key=None, descriptors=None):
        if not descriptors:
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

    def __init__(self, attribute, value_matcher=r"(.?[\sa-zA-Z']+)", info_matcher=InfoMatcher):
        super(TextQuestionMatcher, self).__init__(value_matcher, info_matcher, attribute)

    def find_info(self, question):
        info_matchers = set()
        for begin_delimiter in BEGIN_DELIMITERS:
            begin_positions = [position.end() for position in re.finditer(begin_delimiter, question, re.IGNORECASE)]
            substrings = [question[position:] for position in begin_positions]

            for end_delimiter in END_DELIMITERS:
                for substring in substrings:
                    end_positions = [position.start() for position in re.finditer(end_delimiter, substring, re.IGNORECASE)]
                    values = [substring[:position] for position in end_positions]
                    for value in values:
                        info_matcher = self.get_info_matcher(value)
                        if info_matcher:
                            info_matchers.add(info_matcher)
        return info_matchers


class LatitudeMatcher(TextQuestionMatcher):

    def __init__(self):
        value_matcher = r'(\d+[\s.]\d+\s[S|N])'
        attribute = 'latitude'
        super(LatitudeMatcher, self).__init__(attribute, value_matcher)

    def get_match(self, question):
        match = self._regex.search(question)
        if match:
            match = match.group(1).replace('.', ' ')
        return match


class LongitudeMatcher(TextQuestionMatcher):

    def __init__(self):
        value_matcher = r'(\d+[\s.]\d+\s[E|W])'
        attribute = 'longitude'
        super(LongitudeMatcher, self).__init__(attribute, value_matcher)

    def get_match(self, question):
        match = self._regex.search(question)
        if match:
            match = match.group(1).replace('.', ' ')
        return match


class IndependenceMatcher(TextQuestionMatcher):

    def __init__(self):
        value_matcher = r'((?:[\d]+\s)?(?:January |February |March |April |May |June |July |August |September |October |November |December )?[\d]+)'
        attribute = 'independence'
        super(IndependenceMatcher, self).__init__(attribute, value_matcher)


class ContainsMatcher(QuestionMatcher):

    def __init__(self, attribute):
        pattern = r'contains (\d) words(?: as| and| is|\?|\.)?'
        info_matcher = LengthMatcher
        super(ContainsMatcher, self).__init__(pattern, info_matcher, attribute)


class QuestionWithIntervalMatcher(TextQuestionMatcher):

    def __init__(self, attribute):
        pattern = r'between ([\d\.\s,]+)%? and ([\d\.\s,]+)%?'
        info_matcher = BetweenMatcher
        super(QuestionWithIntervalMatcher, self).__init__(attribute, pattern, info_matcher)

    def get_info_matcher(self, question):
        info_matcher = None
        match = self.get_match(question)
        if match:
            lower_bound = match.group(1)
            upper_bound = match.group(2)
            info_matcher = self._info_matcher(self._attribute, lower_bound, upper_bound)
        return info_matcher

    def get_match(self, question):
        return self._regex.search(question)


class NumericQuestionMatcher(TextQuestionMatcher):

    def __init__(self, attribute, pattern, op):
        self._op = op
        info_matcher = NumericInfoMatcher
        super(NumericQuestionMatcher, self).__init__(attribute, pattern, info_matcher)

    def get_info_matcher(self, question):
        info_matcher = None
        match = self.get_match(question)
        if match:
            info_matcher = self._info_matcher(self._attribute, match, self._op)
        return info_matcher


class LessThanMatcher(NumericQuestionMatcher):

    def __init__(self, attribute):
        pattern = r'less than ([\d\.\s,]+)%?'
        super(LessThanMatcher, self).__init__(attribute, pattern, '<')


class GreaterThanMatcher(NumericQuestionMatcher):

    def __init__(self, attribute):
        pattern = r'greater than ([\d\.\s,]+)%?'
        super(GreaterThanMatcher, self).__init__(attribute, pattern, '>')


class EqualsMatcher(NumericQuestionMatcher):

    def __init__(self, attribute):
        pattern = r'([\d\.\s,]+)%?'
        super(EqualsMatcher, self).__init__(attribute, pattern, '=')


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
        super(EthnicGroups, self).__init__(attribute, info_key, descriptors=['including'])

    def find_info(self, question):
        info_matcher = None
        match = self._regex.search(question)
        if match:
            info_list = match.group(1)
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


class ApproximationMatcher(QuestionMatcher):

    def __init__(self, attribute):
        pattern = r'is approximately ([\d\.\s,]+)(?: and| is|\?|\.)?'
        info_matcher = NumericApproximationInfoMatcher
        super(ApproximationMatcher, self).__init__(pattern, info_matcher, attribute)


class QuestionMatcherGenerator(object):

    def __init__(self):

        self._specific_matchers = {'latitude': [LatitudeMatcher()], 'longitude': [LongitudeMatcher()],
                                   'climate': [Climate()], 'independence': [IndependenceMatcher()],
                                   'illicit drugs': [IllicitDrugsActivities()], 'ethnic groups': [EthnicGroups()],
                                   'national anthem': [NationalAnthemComposedBy(),
                                                       TextQuestionMatcher('national anthem')]}

    def get_question_matchers(self, attribute):

        if attribute not in self._specific_matchers.keys():
            return [QuestionWithListMatcher(attribute), StartsWithMatcher(attribute), EndsWithMatcher(attribute),
                    ContainsMatcher(attribute), QuestionWithIntervalMatcher(attribute), TextQuestionMatcher(attribute),
                    LessThanMatcher(attribute), GreaterThanMatcher(attribute), EqualsMatcher(attribute),
                    ApproximationMatcher(attribute)]
        else:
            return self._specific_matchers[attribute]