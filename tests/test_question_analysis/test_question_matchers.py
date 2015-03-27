from nose.tools import assert_true

from Robot.question_analysis.attributes import EqualsMatcher, GreaterThanMatcher, LessThanMatcher, StartsWithMatcher, \
    EndsWithMatcher, QuestionWithIntervalMatcher, TextQuestionMatcher, ContainsMatcher, ApproximationMatcher


class TestQuestionMatchers(object):
    def __init__(self):
        pass

    def test_equals_matcher(self):
        question = 'My public debt is 7.9% of GDP.'
        equals_matcher = EqualsMatcher('public debt')
        info_matcher = equals_matcher.find_info(question)
        assert_true(info_matcher.match('7.9% (2013)'))

    def test_greater_than_matcher(self):
        question = 'population is greater than 42.'
        greater_than_matcher = GreaterThanMatcher('population')
        info_matcher = greater_than_matcher.find_info(question)
        assert_true(info_matcher.match('50 (2013)'))

    def test_less_than_matcher(self):
        question = 'population is less than 42.'
        less_than_matcher = LessThanMatcher('population')
        info_matcher = less_than_matcher.find_info(question)
        assert_true(info_matcher.match('40 (2013)'))

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
        question = 'population between 41 and 43'
        interval_matcher = QuestionWithIntervalMatcher('population')
        info_matcher = interval_matcher.find_info(question)
        assert_true(info_matcher.match('42'))

    def test_text_question_matcher(self):
        question = 'My birth rate is approximately 16 births/1000'
        text_question_matcher = ApproximationMatcher('birth rate')
        info_matcher = text_question_matcher.find_info(question)
        assert_true(info_matcher.match('16.15 deaths/1,000 population (2014 est.)'))

    def test_contains_matcher(self):
        question = 'capital contains 2 words'
        contains_matcher = ContainsMatcher('capital')
        info_matcher = contains_matcher.find_info(question)
        assert_true(info_matcher.match('washington dc'))