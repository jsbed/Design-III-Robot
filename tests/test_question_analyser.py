from Robot.question_analysis.question_analyser import QuestionAnalyser
from nose.tools import assert_equal


class TestQuestionAnalyser(object):

    def __init__(self):
        self._question_analyser = QuestionAnalyser()

    def test_unemployment_rate(self):
        question = 'My unemployment rate is 40.6%.'
        assert_equal(self._question_analyser.answer_question(question), 'Haiti')

    def test_capital(self):
        question = 'My capital name starts with Moga.'
        assert_equal(self._question_analyser.answer_question(question), 'Somalia')

    def test_population(self):
        question = 'My population is 32 742.'
        assert_equal(self._question_analyser.answer_question(question), 'San Marino')

    def test_urban_areas(self):
        question = 'The major urban areas of this country are Santiago, Valparaiso and Concepcion.'
        assert_equal(self._question_analyser.answer_question(question), 'Chile')
