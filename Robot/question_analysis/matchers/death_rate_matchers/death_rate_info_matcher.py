import re

from Robot.question_analysis.matchers.info_matchers import InfoMatcher


class DeathRateGreaterThanMatcher(InfoMatcher):

    def __init__(self, death_rate):
        self._death_rate = float(death_rate)
        info_key = 'death rate'
        regex = re.compile('([\d.]+) death[s]?\/1,000')
        super(DeathRateGreaterThanMatcher, self).__init__(info_key, regex)

    def match(self, info_data):
        match = self._regex.search(info_data)
        if match:
            death_rate = match.group(1)
            death_rate = float(death_rate)
            return death_rate > self._death_rate

        return False


class DeathRateLessThanMatcher(InfoMatcher):

    def __init__(self, death_rate):
        self._death_rate = float(death_rate)
        info_key = 'death rate'
        regex = re.compile('([\d.]+) death[s]?\/1,000')
        super(DeathRateLessThanMatcher, self).__init__(info_key, regex)

    def match(self, info_data):
        match = self._regex.search(info_data)
        if match:
            death_rate = match.group(1)
            death_rate = float(death_rate)
            return death_rate < self._death_rate

        return False