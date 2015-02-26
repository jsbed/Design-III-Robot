import re

from Robot.question_analysis.matchers.info_matchers import InfoMatcher

class CountryCodeMatcher(InfoMatcher):

    def __init__(self, country_code):
        info_key = 'country code'
        regex = re.compile(country_code)
        super(CountryCodeMatcher, self).__init__(info_key, regex)
