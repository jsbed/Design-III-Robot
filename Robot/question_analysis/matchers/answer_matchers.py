import re

class InfoMatcher(object):

    def __init__(self, info_key, regex):
        self._info_key = info_key
        self._regex = regex

    def get_key(self):
        return self._info_key

    def match(self, info_data):
        return self._regex.search(info_data)

class CapitalInfoMatcher(InfoMatcher):

    def __init__(self, regex):
        info_key = 'capital'
        super(CapitalInfoMatcher, self).__init__(info_key, regex)



class CapitalFullNameMatcher(CapitalInfoMatcher):

    def __init__(self, capital):
        regex = re.compile(capital)
        super(CapitalFullNameMatcher, self).__init__(regex)

class CapitalPrefixMatcher(CapitalInfoMatcher):

    def __init__(self, capital_prefix):
        regex = re.compile('^{0}'.format(capital_prefix))
        super(CapitalPrefixMatcher, self).__init__(regex)

class CapitalSuffixMatcher(CapitalInfoMatcher):

    def __init__(self, info_key, capital_suffix):
        regex = re.compile('{0}$'.format(capital_suffix))
        super(CapitalSuffixMatcher, self).__init__(regex)
