import re

from Robot.question_analysis.matchers.info_matchers import InfoMatcher


class ElectricityProductionBetweenMatcher(InfoMatcher):

    def __init__(self, lower_bound, upper_bound):
        self._lower_bound = float(lower_bound)
        self._upper_bound = float(upper_bound)
        regex = re.compile('([\d.]+)')
        info_key = 'electricity production'
        super(ElectricityProductionBetweenMatcher, self).__init__(info_key, regex)

    def match(self, info_data):
        electricity_production = self._regex.search(info_data)
        if electricity_production:
            electricity_production = electricity_production.group(1)
            electricity_production = float(electricity_production)
            return self._lower_bound < electricity_production < self._upper_bound
        else:
            return None
