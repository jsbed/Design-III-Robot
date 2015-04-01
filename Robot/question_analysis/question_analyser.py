import collections

from Robot.configuration.config import Config
from Robot.question_analysis.factbook_parsing.country_info import Factbook, INFO_KEY_ALIAS
from Robot.question_analysis.question_matchers import QuestionMatcherGenerator
from Robot.question_analysis.question_segmentator import QuestionSegmentator


class QuestionAnalyser(object):

    def __init__(self):

        self._config = Config()
        self._question_segmentator = QuestionSegmentator()
        self._factbook = Factbook()
        self._question_matcher_generator = QuestionMatcherGenerator()
        self._attributes = INFO_KEY_ALIAS

    def answer_question(self, question):
        country_matches = []
        questions = self._question_segmentator.segment_question(question)
        for question in questions:
            info_matchers = []
            question_attribute = None
            for attribute in self._attributes:
                if attribute in question:
                    question_attribute = attribute
            question_matchers = self._question_matcher_generator.get_question_matchers(question_attribute)

            for matcher in question_matchers:
                info_matcher = matcher.find_info(question)
                if info_matcher:
                    if isinstance(info_matcher, collections.Iterable):
                        info_matchers.extend(info_matcher)
                    else:
                        info_matchers.append(info_matcher)

            for info_matcher in info_matchers:
                matches = self._factbook.get_matches(info_matcher)
                if matches:
                    country_matches.append(matches)

            if not country_matches:
                raise Exception("No country found")
        country_answer = country_matches[0]
        for country_match in country_matches[1:]:
            country_answer = list(filter(lambda el: el in country_match, country_answer))
        country_answer = list(country_answer)
        country_answer = self._remove_country_duplicates(country_answer)
        country_answer = self._get_best_matches(country_answer)
        country_answer = self._get_lowest_cube_country(country_answer)
        return country_answer[0].country_name

    def _remove_country_duplicates(self, country_answer):
        """
        Remove country duplicates and keep the one with the lowest score
        """
        if len(country_answer) > 1:
            country_answer.sort(key=lambda el: el.country_name)
            for index, country_result in enumerate(country_answer[:-1]):
                next_country = country_answer[index + 1]
                if country_result.country_name == next_country.country_name:
                    lowest_score = min(country_result.score, next_country.score)
                    country_answer[index].score, country_answer[index + 1].score = lowest_score, lowest_score
            country_answer = set(country_answer) #remove duplicates
        return list(country_answer)

    def _get_best_matches(self, country_result_list):
        best_matches = []
        country_result_list.sort(key=lambda el: el.score, reverse=True)
        best_matches.append(country_result_list[0])
        best_score = best_matches[0].score
        country_result_list.pop(0)
        country_result_list = list(filter(lambda el: el.score == best_score, country_result_list))
        best_matches.extend(country_result_list)
        return best_matches

    def _get_lowest_cube_country(self, country_result_list):
        return country_result_list