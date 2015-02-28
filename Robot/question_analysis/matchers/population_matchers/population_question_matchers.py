import re
from Robot.question_analysis.matchers.population_matchers.population_info_matchers import PopulationMatcher
from Robot.question_analysis.matchers.population_matchers.population_info_matchers import PopulationGreaterThanMatcher
from Robot.question_analysis.matchers.question_matchers import QuestionMatcher

__author__ = 'dario'


class PopulationIs(QuestionMatcher):

    def __init__(self):
        pattern = r'population is ([\d\s]+)'
        info_matcher = PopulationMatcher
        super(PopulationIs, self).__init__(pattern, info_matcher)

    def find_info(self, question):
        info_matcher = None
        population_match = self._regex.search(question)
        if population_match:
            population = population_match.group(1)
            population = population.replace(' ', ',')
            info_matcher = self._info_matcher(population)
        return info_matcher


class PopulationGreaterThan(QuestionMatcher):

    def __init__(self):
        pattern = r'population greater than ([\d\s]*)'
        info_matcher = PopulationGreaterThanMatcher
        super(PopulationGreaterThan, self).__init__(pattern, info_matcher)

    def find_info(self, question):
        info_matcher = None
        population_match = self._regex.search(question)
        if population_match:
            population = population_match.group(1)
            population = population.replace(' ', ',')
            info_matcher = self._info_matcher(population)
        return info_matcher