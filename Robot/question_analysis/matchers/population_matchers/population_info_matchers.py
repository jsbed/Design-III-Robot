import re
from Robot.question_analysis.matchers.info_matchers import InfoMatcher

__author__ = 'dario'


class PopulationMatcher(InfoMatcher):

    def __init__(self, population):
        info_key = 'population'
        regex = re.compile('{0}'.format(population))
        super(PopulationMatcher, self).__init__(info_key, regex)


class PopulationGreaterThanMatcher(InfoMatcher):

    def __init__(self, population_threshold):
        info_key = 'population'
        regex = re.compile('([\d,]+).*est')
        self._population_threshold = int(population_threshold.replace(',', ''))
        super(PopulationGreaterThanMatcher, self).__init__(info_key, regex)

    def match(self, info_data):
        population = self._regex.search(info_data)
        if population:
            population = population.group(1)
            population = population.replace(',', '')
            population = int(population)
            return population > self._population_threshold
        else:
            return None
