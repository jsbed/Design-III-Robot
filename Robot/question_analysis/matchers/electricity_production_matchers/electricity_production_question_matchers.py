from Robot.question_analysis.matchers.electricity_production_matchers.electricity_production_info_matchers import \
    ElectricityProductionBetweenMatcher
from Robot.question_analysis.matchers.question_matchers import QuestionWithIntervalMatcher


class ElectricityProductionBetween(QuestionWithIntervalMatcher):

    def __init__(self):
        pattern = r'electricity production is between (\d+) and (\d+)'
        info_matcher = ElectricityProductionBetweenMatcher
        super(ElectricityProductionBetween, self).__init__(pattern, info_matcher)