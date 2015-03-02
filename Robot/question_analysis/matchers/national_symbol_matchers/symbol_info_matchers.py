import re

from Robot.question_analysis.matchers.info_matchers import InfoMatcher


class NationalSymbolIsMatcher(InfoMatcher):

    def __init__(self, symbol):
        info_key = 'national symbol'
        regex = re.compile(r"([\s\w\d\-',]+\;){0,1}\s*" + symbol + r'$', re.IGNORECASE)
        super(NationalSymbolIsMatcher, self).__init__(info_key, regex)


class OneOfNationalSymbolIsMatcher(InfoMatcher):

    def __init__(self, symbol):
        info_key = 'national symbol'
        regex = re.compile('{0}'.format(symbol), re.IGNORECASE)
        super(OneOfNationalSymbolIsMatcher, self).__init__(info_key, regex)

