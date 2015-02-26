import re

from Robot.question_analysis.matchers.info_matchers import InfoMatcher


class GrowthRateMatcher(InfoMatcher):

    def __init__(self, growth_rate):
        regex = re.compile(growth_rate)
        info_key = 'population growth rate'
        super(GrowthRateMatcher, self).__init__(info_key, regex)


class GrowthRateBetweenMatcher(InfoMatcher):

    def __init__(self, growth_rate_lower_bound, growth_rate_upper_bound):
        regex = re.compile('([\d.]+)%')
        info_key = 'population growth rate'
        self._lower_bound = float(growth_rate_lower_bound)
        self._upper_bound = float(growth_rate_upper_bound)
        super(GrowthRateBetweenMatcher, self).__init__(info_key, regex)

    def match(self, info_data):
        growth_rate = self._regex.search(info_data)
        if growth_rate:
            growth_rate = growth_rate.group(1)
            growth_rate = float(growth_rate)
            return self._lower_bound < growth_rate < self._upper_bound
        else:
            return None