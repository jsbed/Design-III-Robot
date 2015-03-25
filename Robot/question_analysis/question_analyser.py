from Robot.configuration.config import Config
from Robot.question_analysis.attributes import QuestionMatcherGenerator
from Robot.question_analysis.factbook_parsing.country_info import Factbook, INFO_KEY_ALIAS
from Robot.question_analysis.question_segmentator import QuestionSegmentator


class QuestionAnalyser(object):

    def __init__(self):

        self._config = Config()
        self._question_segmentator = QuestionSegmentator()
        self._factbook = Factbook()
        self._question_matcher_generator = QuestionMatcherGenerator()

    def answer_question(self, question):
        country_matches = []
        questions = self._question_segmentator.segment_question(question)
        self._attributes = INFO_KEY_ALIAS
        for question in questions:
            info_matchers = []
            #find attribute, get question matchers
            question_attribute = None
            for attribute in self._attributes:
                if attribute in question:
                    question_attribute = attribute
            question_matchers = self._question_matcher_generator.get_question_matchers(question_attribute)

            for matcher in question_matchers:
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
