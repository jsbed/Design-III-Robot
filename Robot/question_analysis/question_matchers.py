import re


class Matchers(object):

    def __init__(self):
        self._matchers = [CapitalIs(), CapitalStartsWith(), CapitalEndsWith()]

    def __iter__(self):
        return iter(self._matchers)


class CapitalIs(object):

    def __init__(self):
        self._info_name = 'capital'
        self._regex = re.compile('.*country.*has (\w*).*capital')

    def find_info(self, question):
        info = {}
        capital_match = self._regex.search(question)
        if capital_match:
            info = (self._info_name, re.compile(capital_match.group(1)))
        return info  # will become answer matcher


class CapitalStartsWith(object):

    def __init__(self):
        self._info_name = 'capital'
        self._regex = re.compile('.*capital.*starts with (\w*)')

    def find_info(self, question):
        info = {}
        capital_match = self._regex.search(question)
        if capital_match:
            info = (self._info_name, re.compile('^{0}'.format(capital_match.group(1))))
        return info


class CapitalEndsWith(object):

    def __init__(self):
        self._info_name = 'capital'
        self._regex = re.compile('.*capital.*ends with (\w+)')

    def find_info(self, question):
        info = {}
        capital_match = self._regex.search(question)
        if capital_match:
            info = (self._info_name, re.compile('{0}$'.format(capital_match.group(1))))
        return info