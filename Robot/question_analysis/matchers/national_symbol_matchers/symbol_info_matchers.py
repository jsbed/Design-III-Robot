import re

from Robot.question_analysis.matchers.info_matchers import InfoMatcher


class NationalSymbolIsMatcher(InfoMatcher):

    def __init__(self, symbol):
        info_key = 'national symbol'
        regex = re.compile(symbol, re.IGNORECASE)
        super(NationalSymbolIsMatcher, self).__init__(info_key, regex)
