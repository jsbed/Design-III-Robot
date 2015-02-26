import re

from Robot.question_analysis.matchers.electricity_production_matchers.electricity_production_info_matchers import \
    ElectricityProductionBetweenMatcher


class ElectricityProductionBetween(object):

    def __init__(self):
        self._regex = re.compile('electricity production is between (\d+) and (\d+)')

    def find_info(self, question):
        info_matcher = None
        growth_match = self._regex.search(question)
        if growth_match:
            electricity_production_lower_bound = growth_match.group(1)
            electricity_production_upper_bound = growth_match.group(2)
            info_matcher = ElectricityProductionBetweenMatcher(electricity_production_lower_bound,
                                                               electricity_production_upper_bound)
        return info_matcher