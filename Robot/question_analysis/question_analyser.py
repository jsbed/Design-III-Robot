from Robot.question_analysis.matchers.question_matchers import Matchers
from Robot.configuration.config import Config
from Robot.question_analysis.factbook_parsing.country_info import Factbook


class QuestionAnalyser(object):

    def __init__(self):
        self._config = Config()
        self._matchers = Matchers()
        self._factbook = Factbook()

    def answer_question(self, question):
        answer_matchers = []  # answer_matcher

        for matcher in self._matchers:
            answer_matcher = matcher.find_info(question)
            if answer_matcher:
                answer_matchers.append(answer_matcher)

        country_matches = []
        for answer_matcher in answer_matchers:
            matches = self._factbook.get_matches(answer_matcher)
            if matches:
                country_matches.append(matches)

        if not country_matches:
            raise Exception("No country found")

        country_answer = country_matches[0]
        for country_match in country_matches[1:]:
            country_answer.intersection(country_match)

        if len(country_answer) > 1:
            raise Exception("More than one country found as answer")
        country_answer = country_answer.pop()
        return country_answer
