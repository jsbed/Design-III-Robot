from Robot.question_analysis.question_matchers import Matchers
from Robot.configuration.config import Config
from Robot.question_analysis.factbook_parsing.country_info import Factbook


class QuestionAnalyser(object):

    def __init__(self):
        self._config = Config()
        self._matchers = Matchers()
        self._factbook = Factbook()

    def answer_question(self, question):
        infos = []  # answer_matcher

        for matcher in self._matchers:
            info = matcher.find_info(question)
            if info:
                infos.append(info)

        country_matches = []
        for info in infos:
            matches = self._factbook.get_matches(info)
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
