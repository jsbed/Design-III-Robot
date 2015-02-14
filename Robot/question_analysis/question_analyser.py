import pickle

from Robot.question_analysis.question_matchers import Matchers
from Robot.configuration.config import Config

FIELDS_ALIAS = {'capital': ['capital', 'name']}


class QuestionAnalyser(object):

    def __init__(self):
        self._config = Config()
        self._matchers = Matchers()
        self._countries_info = self._load_countries_info()

    def answer_question(self, question):
        country_matches = []
        infos = []

        for matcher in self._matchers:
            info = matcher.find_info(question)
            if info:
                infos.append(info)

        for info in infos:
            for country in self._countries_info.iteritems():
                if info


    def _load_countries_info(self):
        try:
            with open(self._config.get_country_data_path()) as country_data_file:
                countries_info = pickle.load(country_data_file)
        except:
            raise Exception('Could not load country data file.')
        return countries_info
