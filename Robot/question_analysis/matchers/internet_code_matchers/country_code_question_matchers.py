import re

from Robot.question_analysis.matchers.internet_code_matchers.country_code_info_matchers import CountryCodeMatcher


class InternetCountryCodeIs(object):

    def __init__(self):
        self._regex = re.compile('internet country code is (.[\w]+)')

    def find_info(self, question):
        info_matcher = None
        country_code_match = self._regex.search(question)
        if country_code_match:
            country_code = country_code_match.group(1)
            info_matcher = CountryCodeMatcher(country_code)
        return info_matcher


class HasInternetCountryCode(object):

    def __init__(self):
        self._regex = re.compile('has (.[\w]+).*internet country code')

    def find_info(self, question):
        info_matcher = None
        country_code_match = self._regex.search(question)
        if country_code_match:
            country_code = country_code_match.group(1)
            info_matcher = CountryCodeMatcher(country_code)
        return info_matcher
