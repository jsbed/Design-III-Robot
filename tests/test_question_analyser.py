from Robot.question_analysis.question_analyser import QuestionAnalyser
from nose.tools import assert_equal


class TestQuestionAnalyser(object):

    def __init__(self):
        pass

    def test_unemployment_rate(self):
        question = 'My unemployment rate is 40.6%.'
        question_analyser = QuestionAnalyser()
        assert_equal(question_analyser.answer_question(question), 'Haiti')

    def test_capital(self):
        question = 'My capital name starts with Moga.'
        question_analyser = QuestionAnalyser()
        assert_equal(question_analyser.answer_question(question), 'Somalia')

    def test_population(self):
        question = 'My population is 32 742.'
        question_analyser = QuestionAnalyser()
        assert_equal(question_analyser.answer_question(question), 'San Marino')