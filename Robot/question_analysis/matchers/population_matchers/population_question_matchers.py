import re
from Robot.question_analysis.matchers.population_matchers.population_info_matchers import PopulationMatcher, PopulationGreaterThanMatcher

__author__ = 'dario'


class PopulationIs(object):

    def __init__(self):
        self._regex = re.compile('population is ([\d\s]+)')

    def find_info(self, question):
        info_matcher = None
        population_match = self._regex.search(question)
        if population_match:
            population = population_match.group(1)
            population = population.replace(' ', ',')
            info_matcher = PopulationMatcher(population)
        return info_matcher

class PopulationGreaterThan(object):

    def __init__(self):
        self._regex = re.compile('population greater than ([\d\s]*)')

    def find_info(self, question):
        info_matcher = None
        population_match = self._regex.search(question)
        if population_match:
            population = population_match.group(1)
            population = population.replace(' ', ',')
            info_matcher = PopulationGreaterThanMatcher(population)
        return info_matcher