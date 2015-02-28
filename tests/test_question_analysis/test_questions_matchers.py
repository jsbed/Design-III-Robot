from nose.tools import assert_true

from Robot.question_analysis.matchers.question_matchers import UrbanAreas


class TestQuestionMatchers(object):

    def __init__(self):
        pass

    def test_urban_areas(self):
        question = 'The major urban areas of this country are Santiago, Valparaiso and Concepcion.'
        info_data = 'SANTIAGO (capital) 6.034 million; Valparaiso 883,000; Concepcion 770,000 (2011)'
        urban_areas_matcher = UrbanAreas()
        info_matcher = urban_areas_matcher.find_info(question)
        assert_true(info_matcher.match(info_data))
