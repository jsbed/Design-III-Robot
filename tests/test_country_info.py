from nose.tools import assert_equal

from Robot.question_analysis.factbook_parsing.country_info import Factbook
from Robot.question_analysis.matchers.answer_matchers import CapitalFullNameMatcher


class TestCountryInfo():

    def __init__(self):
        self._factbook = Factbook()

    def test_get_info_from_country(self):
        country = 'Canada'
        info_name = 'capital'

        actual = self._factbook.get_info_from_country(country, info_name)
        expected = 'Ottawa'
        assert_equal(actual, expected)

    def test_get_matches(self):
        expected = set()
        expected.add('Canada')
        assert_equal(self._factbook.get_matches(CapitalFullNameMatcher('Ottawa')), expected)