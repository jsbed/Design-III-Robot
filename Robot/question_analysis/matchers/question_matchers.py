import re

from Robot.question_analysis.matchers.capital_matchers.capital_question_matchers import CapitalIs, CapitalEndsWith
from Robot.question_analysis.matchers.capital_matchers.capital_question_matchers import CapitalStartsWith
from Robot.question_analysis.matchers.national_symbol_matchers.symbol_question_matchers import NationalSymbolIs
from Robot.question_analysis.matchers.national_symbol_matchers.symbol_question_matchers import IsTheNationalSymbol
from Robot.question_analysis.matchers.national_symbol_matchers.symbol_question_matchers import OneOfNationalSymbolIs

from Robot.question_analysis.matchers.info_matchers import UnemploymentRateMatcher, PopulationMatcher, UrbanAreasMatcher


class Matchers(object):

    def __init__(self):
        self._matchers = [CapitalIs(), CapitalStartsWith(), CapitalEndsWith(), UnemploymentRateIs(),
                          PopulationIs(), UrbanAreas(), NationalSymbolIs(), IsTheNationalSymbol(),
                          OneOfNationalSymbolIs()]

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
        self._regex = re.compile('major urban areas.*(?:are|is) ((?:[\w\s,]+) and (?:[\w]+))')

    def find_info(self, question):
        info_matcher = None
        urban_area_match = self._regex.search(question)
        if urban_area_match:
            urban_areas = urban_area_match.group(1)
            urban_areas = self._extract_cities(urban_areas)
            info_matcher = UrbanAreasMatcher(urban_areas)
        return info_matcher

    def _extract_cities(self, urban_areas):
        urban_areas = re.split(', |\sand\s', urban_areas)
        return urban_areas


class ReligionsAre(object):

    def __init__(self):
        self._regex = re.compile('religions.*(?:including) ((?:[\w\s,]+) and (?:[\w]+))', re.IGNORECASE)

    def find_info(self, question):
        info_matcher = None
        religions_match = self._regex.search(question)
        if religions_match:
            religions = religions_match.group(1)
            religions = self._extract_religions(religions)
            info_matcher

    def _extract_cities(self, religions):
        religions = re.split(', |\sand\s', religions)
        return religions

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

