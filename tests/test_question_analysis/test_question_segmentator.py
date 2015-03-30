from nose.tools import assert_equal
from Robot.question_analysis.question_segmentator import QuestionSegmentator


class TestQuestionSegmentator(object):

    def __init__(self):
        self._question_segmentator = QuestionSegmentator()

    def test_segmentate_two_attributes_question(self):
        question = 'the capital starts with eth and the population is greater than 42.'
        expected = ['the capital starts with eth?', 'the population is greater than 42.']
        actual = self._question_segmentator.segment_question(question)
        assert_equal(actual, expected)

    def test_segmentate_list_question(self):
        question = """My import partners include Netherlands, France, China, Belgium, Switzerland and Austria
        and my capital starts with 1337."""
        expected = ['My import partners include Netherlands, France, China, Belgium, Switzerland and Austria?',
                    'my capital starts with 1337.']
        actual = self._question_segmentator.segment_question(question)
        assert_equal(actual, expected)

    def test_segmentate_multiple_attributes_question(self):
        question = """My import partners include Netherlands, France, China, Belgium, Switzerland and Austria,
        my population is greater than 12000 and my capital starts with 1337."""
        expected = ['My import partners include Netherlands, France, China, Belgium, Switzerland and Austria?',
                    'my population is greater than 12000?', 'my capital starts with 1337.']
        actual = self._question_segmentator.segment_question(question)
        assert_equal(actual, expected)

    def test_segmentate_single_attribute_question(self):
        question = 'What country has a population growth rate of 1.46%?'
        expected = ['What country has a population growth rate of 1.46%?']
        actual = self._question_segmentator.segment_question(question)
        assert_equal(actual, expected)