import re

from Robot.question_analysis.matchers.internet_code_matchers.country_code_info_matchers import CountryCodeMatcher
from Robot.question_analysis.matchers.question_matchers import QuestionMatcher


class InternetCountryCodeIs(QuestionMatcher):

    def __init__(self):
        pattern = r'internet country code is (.[\w]+)'
        info_matcher = CountryCodeMatcher
        super(InternetCountryCodeIs, self).__init__(pattern, info_matcher)


class HasInternetCountryCode(QuestionMatcher):

    def __init__(self):
        pattern = r'has (.[\w]+).*internet country code'
        info_matcher = CountryCodeMatcher
        super(HasInternetCountryCode, self).__init__(pattern, info_matcher)
