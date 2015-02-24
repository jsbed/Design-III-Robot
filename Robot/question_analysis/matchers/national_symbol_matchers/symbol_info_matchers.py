import re

from Robot.question_analysis.matchers.info_matchers import InfoMatcher

class NationalSymbolMatcher(InfoMatcher):

    def __init__(self, symbol):
        info_key = 'national symbol'
        regex = re.compile('^{0}$'.format(symbol), re.IGNORECASE)
        super(NationalSymbolMatcher, self).__init__(info_key, regex)
