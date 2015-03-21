from Robot.configuration.config import Config
from Robot.question_analysis.factbook_parsing.country_info import Factbook
from Robot.question_analysis.matchers import *
from Robot.question_analysis.matchers.question_matchers import UnemploymenRateGreaterThan
from Robot.question_analysis.question_segmentator import QuestionSegmentator


class QuestionAnalyser(object):

    def __init__(self):

        self._config = Config()
        self._question_segmentator = QuestionSegmentator()
        self._question_matchers = [CapitalIs(), CapitalStartsWith(), CapitalEndsWith(), UnemploymentRateIs(),
                          PopulationIs(), UrbanAreasAre(), NationalSymbolIs(), IsTheNationalSymbol(),
                          OneOfNationalSymbolIs(), ReligionsAre(), InternetCountryCodeIs(), HasInternetCountryCode(),
                          IsTheDateOfIndependence(), DeclaredIndependenceOn(), IndependenceDeclaredIn(),
                          PopulationGreaterThan(), GrowthRateOf(), GrowthRateBetween(), LatitudeIs(), LongitudeIs(),
                          ElectricityProductionBetween(), TotalAreaIs(), NationalAnthemIs(), DeathRateGreaterThan(),
                          DeathRateLessThan(), IndustriesInclude(), InternetUsers(), LanguagesInclude(),
                          ImportPartners(), InDeclaredIndependence(), PublicDebt(), NationalAnthemComposedBy(),
                          BirthRateIs(), EthnicGroups(), PopulationUrbanAreasAre(), Climate(), ExportPartners(),
                          ShortCountryNameLength(), IllicitDrugsActivities(), UnemploymenRateGreaterThan()]
        self._factbook = Factbook()

    def answer_question(self, question):
        country_matches = []
        questions = self._question_segmentator.segment_question(question)
        for question in questions:
            info_matchers = []

            for matcher in self._question_matchers:
                info_matcher = matcher.find_info(question)
                if info_matcher:
                    info_matchers.append(info_matcher)

            for info_matcher in info_matchers:
                matches = self._factbook.get_matches(info_matcher)
                if matches:
                    country_matches.append(matches)

            if not country_matches:
                raise Exception("No country found")

        country_answer = country_matches[0]
        for country_match in country_matches[1:]:
            country_answer = country_answer.intersection(country_match)
        if(len(country_answer) > 1):
            print(country_answer)
        country_answer = country_answer.pop()
        return country_answer
