from Robot.question_analysis.question_analyser import QuestionAnalyser
from nose.tools import assert_equal


class TestQuestionAnalyser(object):

    def __init__(self):
        pass

    def test_capital(self):
        question = 'My death rate is greater than 13 death/1000 and my capital starts with Mos.'
        question_analyser = QuestionAnalyser()
        assert_equal(question_analyser.answer_question(question), 'Russia')
