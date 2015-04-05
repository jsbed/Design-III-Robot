from nose.tools import assert_equal, assert_true, assert_false

from Robot.question_analysis.info_matchers import InfoMatcher, NumericApproximationInfoMatcher, NumericInfoMatcher
from Robot.question_analysis.info_matchers import BetweenInfoMatcher, InfoListMatcher, LengthMatcher
from Robot.question_analysis.info_matchers import IllicitDrugsActivitiesMatcher


class TestInfoMatchers(object):

    def test_get_most_recent_info(self):
        info_matcher = InfoMatcher('info key', 'test')
        info_data = ['NA% (2013 est.)', '5% (2012 est.)']
        info_data = info_matcher.get_most_recent_info(info_data)
        expected_info_data = '5% (2012 est.)'
        assert_equal(info_data, expected_info_data)

    def test_info_matcher(self):
        info_matcher = InfoMatcher('capital', 'Berlin')
        info_data = 'Berlin'
        assert_true(info_matcher.match(info_data))

    def test_fail_info_matcher(self):
        info_matcher = InfoMatcher('capital', 'Berlin')
        info_data = 'Bogotá'
        assert_false(info_matcher.match(info_data))

    def test_numeric_approximation(self):
        info_matcher = NumericApproximationInfoMatcher('population', '31 000 000')
        info_data = '31 000 200'
        actual_score = info_matcher.match(info_data)
        assert_true(0.9 < actual_score < 1.0)

    def test_fail_numeric_approximation(self):
        info_matcher = NumericApproximationInfoMatcher('population', '31 000 000')
        info_data = '35 000 000'
        actual_score = info_matcher.match(info_data)
        assert_true(0.5 < actual_score < 0.9)

    def test_lower_than_info_matcher(self):
        info_matcher = NumericInfoMatcher('population', '50,000', '<')
        info_data = '48 000'
        assert_true(info_matcher.match(info_data))

    def test_fail_lower_than_info_matcher(self):
        info_matcher = NumericInfoMatcher('population', '50,000', '<')
        info_data = '52 000'
        assert_false(info_matcher.match(info_data))

    def test_greater_than_info_matcher(self):
        info_matcher = NumericInfoMatcher('population', '7 500 000', '>')
        info_data = '7 600 000'
        assert_true(info_matcher.match(info_data))

    def test_fail_greater_than_info_matcher(self):
        info_matcher = NumericInfoMatcher('population', '7 500 000', '>')
        info_data = '7 400 000'
        assert_false(info_matcher.match(info_data))

    def test_equal_info_matcher(self):
        info_matcher = NumericInfoMatcher('population', '42', '=')
        info_data = '42'
        assert_true(info_matcher.match(info_data))

    def test_fail_equal_info_matcher(self):
        info_matcher = NumericInfoMatcher('population', '42', '=')
        info_data = '42 000 000'
        assert_false(info_matcher.match(info_data))

    def test_between_matcher(self):
        info_matcher = BetweenInfoMatcher('population', '55 125', '55127')
        info_data = '55,126'
        assert_true(info_matcher.match(info_data))

    def test_fail_between_matcher(self):
        info_matcher = BetweenInfoMatcher('population', '55 125', '55127')
        info_data = '55,128'
        assert_false(info_matcher.match(info_data))

    def test_info_list_matcher(self):
        info_matcher = InfoListMatcher('religions', ['atheism', 'islam', 'catholicism'])
        info_data = 'Islam, Atheism, Catholicism'
        assert_true(info_matcher.match(info_data))

    def test_fail_info_list_matcher(self):
        info_matcher = InfoListMatcher('religions', ['atheism', 'islam', 'catholicism'])
        info_data = 'Islam, Atheism, Buddhism'
        assert_false(info_matcher.match(info_data))

    def test_length_matcher(self):
        info_matcher = LengthMatcher('capital', '3')
        info_data = 'Andorra la Vella'
        assert_true(info_matcher.match(info_data))

    def test_fail_length_matcher(self):
        info_matcher = LengthMatcher('capital', '2')
        info_data = 'Ottawa'
        assert_false(info_matcher.match(info_data))

    def test_illicit_drugs_matcher(self):
        info_matcher = IllicitDrugsActivitiesMatcher('illicit drug', 'illicit producer cannabis hashish')
        info_data = """illicit producer of cannabis and hashish for the domestic and international drug markets;
                    transit point for opiates from Southeast Asia to the West"""
        actual_score = info_matcher.match(info_data)
        expected_score = 1.0
        assert_equal(actual_score, expected_score)

    def test_partial_match_illicit_drugs_matcher(self):
        info_matcher = IllicitDrugsActivitiesMatcher('illicit drug', 'illicit producer cannabis hashish')
        info_data = """illicit producer of cannabis for the domestic and international drug markets;
                    transit point for opiates from Southeast Asia to the West"""
        actual_score = info_matcher.match(info_data)
        expected_score = 0.75
        assert_equal(actual_score, expected_score)