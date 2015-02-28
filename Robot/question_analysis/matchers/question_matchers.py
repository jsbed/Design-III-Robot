import re

from Robot.question_analysis.matchers import *


class Matchers(object):

    def __init__(self):
        self._matchers = [CapitalIs(), CapitalStartsWith(), CapitalEndsWith(), UnemploymentRateIs(),
                          PopulationIs(), UrbanAreas(), NationalSymbolIs(), IsTheNationalSymbol(),
                          OneOfNationalSymbolIs(), ReligionsAre(), InternetCountryCodeIs(), HasInternetCountryCode(),
                          IsTheDateOfIndependence(), DeclaredIndependenceOn(), IndependenceDeclaredIn(),
                          PopulationGreaterThan(), GrowthRateOf(), GrowthRateBetween(), LatitudeIs(), LongitudeIs(),
                          ElectricityProductionBetween(), TotalAreaIs()]

    def __iter__(self):
        return iter(self._matchers)


class QuestionMatcher(object):

    def __init__(self, pattern, info_matcher):
        self._regex = re.compile(pattern, re.IGNORECASE)
        self._info_matcher = info_matcher

    def find_info(self, question):
        info_matcher = None
        match = self._regex.search(question)
        if match:
            info_matcher = self._info_matcher(match.group(1))
        return info_matcher


class QuestionWithListMatcher(QuestionMatcher):

    def __init__(self, pattern, info_matcher):
        super(QuestionWithListMatcher, self).__init__(pattern, info_matcher)

    def find_info(self, question):
        info_matcher = None
        match = self._regex.search(question)
        if match:
            infos = match.group(1)
            infos = self._extract_cities(infos)
            info_matcher = self._info_matcher(infos)
        return info_matcher

    def _extract_infos(self, infos):
        infos = re.split(', |\sand\s|and\s', infos)
        return infos

class UnemploymentRateIs(QuestionMatcher):

    def __init__(self):
        pattern = r'unemployment rate is ([\d.]+)%'
        info_matcher = UnemploymentRateMatcher
        super(UnemploymentRateIs, self).__init__(pattern, info_matcher)


class UrbanAreas(QuestionMatcher):

    def __init__(self):
        pattern = r'major urban areas.*(?:are|is) ((?:[\w\s,]+) and (?:[\w]+))'
        info_matcher = UrbanAreasMatcher
        super(UrbanAreas, self).__init__(pattern, info_matcher)

    def find_info(self, question):
        info_matcher = None
        urban_area_match = self._regex.search(question)
        if urban_area_match:
            urban_areas = urban_area_match.group(1)
            urban_areas = self._extract_cities(urban_areas)
            info_matcher = self._info_matcher(urban_areas)
        return info_matcher

    def _extract_cities(self, urban_areas):
        urban_areas = re.split(', |\sand\s|and\s', urban_areas)
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
            info_matcher = ReligionsMatcher(religions)
        return info_matcher

    def _extract_religions(self, religions):
        print(repr(religions))
        religions = re.split(',\s|\sand\s|and\s', religions)
        return religions


class TotalAreaIs(object):

    def __init__(self):
        self._regex = re.compile('total area of ([\d,]+ sq km)')

    def find_info(self, question):
        info_matcher = None
        area_match = self._regex.search(question)
        if area_match:
            area = area_match.group(1)
            info_matcher = TotalAreaMatcher(area)
        return info_matcher