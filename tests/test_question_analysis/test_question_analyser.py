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
        question = 'My death rate is greater than 13 death/1000 and my capital starts with Mos'
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
        assert_true(self._question_analyser.answer_question(question) in ['Thailand', 'Central African Republic',
                                                                          'Laos', 'Swaziland', "Cote d'Ivoire",
                                                                          'Congo, Republic of the'])

    def test_one_national_symbol_is(self):
        question = 'One national symbol of this country is the edelweiss.'
        assert_equal(self._question_analyser.answer_question(question), 'Austria')

    def test_is_the_national_symbol(self):
        question = 'The lotus blossom is the national symbol of this country.'
        assert_equal(self._question_analyser.answer_question(question), 'Vietnam')

    def test_religions(self):
        question = 'What country has religions including hindu, muslim, Christian, and sikh?'
        assert_true(self._question_analyser.answer_question(question) in ['India', 'Fiji', 'United Arab Emirates',
                                                                          'Canada'])

    def test_internet_country_code_is(self):
        question = 'My internet country code is .br.'
        assert_equal(self._question_analyser.answer_question(question), 'Brazil')

    def test_has_internet_country_code(self):
        question = 'What country has .dz as its internet country code?'
        assert_equal(self._question_analyser.answer_question(question), 'Algeria')

    def test_is_the_independence(self):
        question = '22 September 1960 is the date of independence of this country.'
        assert_equal(self._question_analyser.answer_question(question), 'Mali')

    def test_declared_independence_on(self):
        question = 'What country has declared its independence on 22 May 1990?'
        assert_equal(self._question_analyser.answer_question(question), 'Yemen')

    def test_independence_declared_in(self):
        question = 'My independence was declared in August 1971.'
        assert_equal(self._question_analyser.answer_question(question), 'Bahrain')

    def test_population_greater_than(self):
        question = 'What country has a population greater than 1 300 692 576?'
        assert_equal(self._question_analyser.answer_question(question), 'China')

    def test_growth_rate_of(self):
        question = 'What country has a population growth rate of 1.46%?'
        assert_equal(self._question_analyser.answer_question(question), 'Israel')

    def test_growth_rate_between(self):
        question = 'My population growth rate is between 1.45% and 1.47%.'
        assert_equal(self._question_analyser.answer_question(question), 'Israel')

    def test_latitude_of(self):
        question = 'What country has a latitude of 41.00 S?'
        assert_equal(self._question_analyser.answer_question(question), 'New Zealand')

    def test_latitude_longitude(self):
        question = 'My latitude is 16 00 S and my longitude is 167 00 E.'
        assert_equal(self._question_analyser.answer_question(question), 'Vanuatu')

    def test_electricity_production(self):
        question = 'My electricity production is between 600 and 650 billion kWh.'
        assert_equal(self._question_analyser.answer_question(question), 'Canada')

    def test_area_is(self):
        question = 'What country has a total area of 390757 sq km?'
        assert_equal(self._question_analyser.answer_question(question), 'Zimbabwe')

    def test_national_anthem_is(self):
        question = 'The title of my national anthem is Advance Australia Fair.'
        assert_equal(self._question_analyser.answer_question(question), 'Australia')

    def test_death_rate_less_greater(self):
        question = """The death rate of this country is greater than 10.37 deaths/1000 population
        and less than 10.40 deaths/1000 population."""
        assert_equal(self._question_analyser.answer_question(question), 'Austria')

    def test_unemployement_industries_include(self):
        question = 'My unemployment rate is greater than 25% and my industries include tourism and footwear.'
        assert_true(self._question_analyser.answer_question(question) in ['Saint Kitts and Nevis', 'Spain',
                                                                           'Indonesia', 'Malta'])

    def test_industries_include(self):
        question = 'What country has industries including the world’s largest producer of platinum, gold and chromium?'
        assert_equal(self._question_analyser.answer_question(question), 'South Africa')

    def test_internet_users(self):
        question = 'What country has 13.694 million internet users?'
        assert_equal(self._question_analyser.answer_question(question), 'Argentina')

    def test_languages(self):
        question = 'My languages include german, french and romansch.'
        assert_equal(self._question_analyser.answer_question(question), 'Switzerland')

    def test_import_partners(self):
        question = 'My import partners include Netherlands, France, China, Belgium, Switzerland and Austria.'
        assert_equal(self._question_analyser.answer_question(question), 'Germany')

    def test_in_declared_independence(self):
        question = 'In 1923, we proclaimed our independence.'
        assert_equal(self._question_analyser.answer_question(question), 'Turkey')

    def test_public_debt(self):
        question = 'My public debt is 7.9% of GDP.'
        assert_true(self._question_analyser.answer_question(question) in ['Russia', 'Botswana'])

    def test_national_anthem_composed_by(self):
        question = 'The music of my national anthem was composed by Routhier, Weir and Lavallee.'
        assert_equal(self._question_analyser.answer_question(question), 'Canada')

    def test_major_urban_areas_population(self):
        question = 'What country has major urban areas of 5.068 million and 1.098 million?'
        assert_equal(self._question_analyser.answer_question(question), 'Angola')

    def test_birth_rate_is(self):
        question = 'What country has a birth rate of 46.12 births/ 1000 population?'
        assert_equal(self._question_analyser.answer_question(question), 'Niger')

    def test_ethnic_groups(self):
        question = 'What country has ethnic groups including 51.3% of protestant and 0.7% of buddhist?'
        assert_equal(self._question_analyser.answer_question(question), 'United States')

    def test_climate_capital(self):
        question = 'What country has a tropical climate and has a capital that starts with the letters Phn?'
        assert_equal(self._question_analyser.answer_question(question), 'Cambodia')

    def test_export_partners(self):
        question = 'My export partners are US, Germany, UK, France, Spain, Canada and Italy.'
        assert_equal(self._question_analyser.answer_question(question), 'Bangladesh')

    def test_short_form_length(self):
        question = 'My birth rate is approximately 16 births/1000 and my local short country name contains 2 words.'
        assert_true(self._question_analyser.answer_question(question) in ['Maldives', 'Vietnam', 'Sri Lanka', 'Costa Rica'])

    def test_illicit_drugs(self):
        question = 'What country has illicit drugs activities including a transshipment point for cocaine from South America to North America and illicit cultivation of cannabis?'
        assert_equal(self._question_analyser.answer_question(question), 'Jamaica')

    def test_telephone_lines(self):
        question = 'My telephone lines in use are 1.217 million.'
        assert_equal(self._question_analyser.answer_question(question), 'Jamaica')

from statistics import mean