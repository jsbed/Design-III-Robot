from Robot.question_analysis.question_analyser import QuestionAnalyser
from nose.tools import assert_equal, assert_true, nottest


class TestQuestionAnalyser(object):

    def __init__(self):
        self._question_analyser = QuestionAnalyser()

    def test_unemployment_rate(self):
        question = 'My unemployment rate is 40.6%.'
        assert_equal(self._question_analyser.answer_question(question), 'Haiti')

    def test_capital_start_with(self):
        question = 'My capital name starts with Moga.'
        assert_equal(self._question_analyser.answer_question(question), 'Somalia')

    def test_capital_starts_with_and_death_rate(self):
        question = 'My death rate is greater than 13 death/1000 and my capital starts with Mos.'
        assert_equal(self._question_analyser.answer_question(question), 'Russia')

    def test_country_has_as_capital(self):
        question = 'What country has Yaounde as its capital?'
        assert_equal(self._question_analyser.answer_question(question), 'Cameroon')

    def test_capital_ends_with(self):
        question = 'My capital name starts with Ath and ends with ens.'
        assert_equal(self._question_analyser.answer_question(question), 'Greece')

    def test_population(self):
        question = 'My population is 32 742.'
        assert_equal(self._question_analyser.answer_question(question), 'San Marino')

    def test_urban_areas(self):
        question = 'The major urban areas of this country are Santiago, Valparaiso and Concepcion.'
        assert_equal(self._question_analyser.answer_question(question), 'Chile')

    def test_national_symbol(self):
        question = 'My national symbol is the elephant.'
        assert_true(self._question_analyser.answer_question(question) in ["Cote d'Ivoire", 'Laos', 'Central African Republic'])

    def test_one_national_symbol_is(self):
        question = 'One national symbol of this country is the edelweiss.'
        assert_equal(self._question_analyser.answer_question(question), 'Austria')

    def test_is_the_national_symbol(self):
        question = 'The lotus blossom is the national symbol of this country.'
        assert_equal(self._question_analyser.answer_question(question), 'Macau')

    def test_religions(self):
        question = 'What country has religions including hindu, muslim, Christian, and sikh?'
        assert_true(self._question_analyser.answer_question(question) in ['India', 'Fiji', 'United Arab Emirates',
                                                                          'Canada'])
