import re

from Robot.question_analysis.matchers.capital_matchers.capital_question_matchers import CapitalIs, CapitalEndsWith
from Robot.question_analysis.matchers.capital_matchers.capital_question_matchers import CapitalStartsWith

from Robot.question_analysis.matchers.info_matchers import UnemploymentRateMatcher, PopulationMatcher


class Matchers(object):

    def __init__(self):
        self._matchers = [CapitalIs(), CapitalStartsWith(), CapitalEndsWith(), UnemploymentRateIs(),
                          PopulationIs()]

    def __iter__(self):
        return iter(self._matchers)

class UnemploymentRateIs(object):

    def __init__(self):
        self._regex = re.compile('unemployment rate is ([\d.]+)%')

    def find_info(self, question):
        info_matcher = None
        rate_match = self._regex.search(question)
        if rate_match:
            info_matcher = UnemploymentRateMatcher(rate_match.group(1))
        return info_matcher


class UrbanAreas(object):

    def __init__(self):
        pass


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