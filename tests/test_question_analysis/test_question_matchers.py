from nose.tools import assert_true
from Robot.question_analysis.matchers import GrowthRateBetween

from Robot.question_analysis.matchers.question_matchers import UrbanAreasAre


def test_urban_areas(self):
    question = 'The major urban areas of this country are Santiago, Valparaiso and Concepcion.'
    urban_areas_are = UrbanAreasAre()
    assert_true(urban_areas_are.find_info(question))

def test_growth_rate_between(self):
    question = 'My population growth rate is between 15% and 25%'
    growth_rate_between = GrowthRateBetween()
    assert_true(growth_rate_between.find_info(question))