from nose.tools import assert_true

from Robot.question_analysis.question_matchers import EqualsMatcher, GreaterThanMatcher, LessThanMatcher
from Robot.question_analysis.question_matchers import EndsWithMatcher, TextQuestionMatcher, StartsWithMatcher
from Robot.question_analysis.question_matchers import LatitudeMatcher, ContainsMatcher, ApproximationMatcher
from Robot.question_analysis.question_matchers import QuestionWithIntervalMatcher


def only_one(a_lst):
    true_found = False
    for v in a_lst:
        if v:
            if true_found:
                return False
            else:
                true_found = True
    return true_found


class TestQuestionMatchers(object):

    def assert_info_matcher_list(self, info_matchers, data):
        info_matcher_results = list(map(lambda el: el.match(data), info_matchers))
        assert_true(only_one(info_matcher_results))

    def test_equals_matcher(self):
        question = 'My public debt is 7.9% of GDP.'
        equals_matcher = EqualsMatcher('public debt')
        info_matcher = equals_matcher.find_info(question)
        self.assert_info_matcher_list(info_matcher, '7.9% (2013)')

    def test_greater_than_matcher(self):
        question = 'population is greater than 42.'
        greater_than_matcher = GreaterThanMatcher('population')
        info_matcher = greater_than_matcher.find_info(question)
        self.assert_info_matcher_list(info_matcher, '50 (2013)')

    def test_less_than_matcher(self):
        question = 'population is less than 42.'
        less_than_matcher = LessThanMatcher('population')
        info_matcher = less_than_matcher.find_info(question)
        self.assert_info_matcher_list(info_matcher, '40 (2013)')

    def test_starts_with_matcher(self):
        question = 'capital starts with ott.'
        starts_with_matcher = StartsWithMatcher('capital')
        info_matcher = starts_with_matcher.find_info(question)
        assert_true(info_matcher.match('Ottawa'))

    def test_ends_with_matcher(self):
        question = 'capital ends with cas.'
        ends_with_matcher = EndsWithMatcher('capital')
        info_matcher = ends_with_matcher.find_info(question)
        assert_true(info_matcher.match('Caracas'))

    def test_interval_matcher(self):
        question = 'My population growth rate is between 1.45% and 1.47%.'
        interval_matcher = QuestionWithIntervalMatcher('population growth rate')
        info_matcher = interval_matcher.find_info(question)
        self.assert_info_matcher_list(info_matcher, '1.46% (2015 est.)')

    def test_approximation_question_matcher(self):
        question = 'My birth rate is approximately 16 births/1000'
        text_question_matcher = ApproximationMatcher('birth rate')
        info_matcher = text_question_matcher.find_info(question)
        assert_true(info_matcher.match('16.15 deaths/1,000 population (2014 est.)'))

    def test_contains_matcher(self):
        question = 'capital contains 2 words'
        contains_matcher = ContainsMatcher('capital')
        info_matcher = contains_matcher.find_info(question)
        assert_true(info_matcher.match('washington dc'))

    def test_latitude_matcher(self):
        question = 'What country has a latitude of 41.00 S?'
        latitude_matcher = LatitudeMatcher()
        info_matchers = latitude_matcher.find_info(question)
        info_matcher_results = list(map(lambda el: el.match('41 00 S, 174 00 E'), info_matchers))
        assert_true(any(info_matcher_results))

    def test_text_matcher(self):
        question = 'The lotus blossom is the national symbol of this country.'
        text_matcher = TextQuestionMatcher('national symbol')
        info_matchers = text_matcher.find_info(question)
        info_matcher_results = list(map(lambda el: el.match('yellow, five-pointed star on red field; lotus blossom'),
                                        info_matchers))
        assert_true(any(info_matcher_results))