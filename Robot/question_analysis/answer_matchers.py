import re

class InfoMatcher(object):

    def __init__(self, info_key):
        self._info_key = info_key

    def get_key(self):
        return self._info_key

    def match(self, info_data):
        return self._regex.search(info_data)


class CapitalMatcher(InfoMatcher):

    def __init__(self, info_key, capital):
        super(CapitalMatcher, self).__init__(info_key)
        self._regex = re.compile(capital)

class CapitalPrefixMatcher(InfoMatcher):

    def __init__(self, info_key, capital_prefix):
        super(CapitalPrefixMatcher, self).__init__(info_key)
        self._regex = re.compile('^{0}'.format(capital_prefix))

class CapitalSuffixMatcher(InfoMatcher):

    def __init__(self, info_key, capital_suffix):
        super(CapitalSuffixMatcher, self).__init__(info_key)
        self._regex = re.compile('{0}$'.format(capital_suffix))