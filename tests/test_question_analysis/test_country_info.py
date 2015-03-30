from nose.tools import assert_equal

from Robot.question_analysis.factbook_parsing.country_info import Factbook


class TestCountryInfo():

    def __init__(self):
        self._factbook = Factbook()

    def test_get_info_from_country(self):
        country = 'Canada'
        info_name = 'capital'

        actual = self._factbook.get_info_from_country(country, info_name)
        expected = 'Ottawa'
        assert_equal(actual, expected)
