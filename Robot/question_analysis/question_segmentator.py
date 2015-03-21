from collections import namedtuple
from operator import attrgetter
from Robot.question_analysis.factbook_parsing.country_info import INFO_KEY_ALIAS


class QuestionSegmentator(object):
    """
    Segments the question around the 'and' word
    """
    def __init__(self):
        self._subquestions = []
        self._separators = [' and ', ', ']
        self._attributes = INFO_KEY_ALIAS.keys()

    def segment_question(self, question):
        question = self._clean_question(question)
        attributes_position = self._find_attributes_in_question(question)
        while(len(attributes_position) > 1):
            question = self._remove_subquestion(question, attributes_position[1])
            del attributes_position[0]
        self._subquestions.append(question)
        return self._subquestions

    def _clean_question(self, question):
        question = question.replace('\n', '').replace('\r\n', '').replace('\r', '')
        question = ' '.join(question.split())
        return question

    def _find_attributes_in_question(self, question):
        """
        Returns positions of attributes in the question. Positions are sorted.
        """
        attributes_position = []
        for attribute in self._attributes:
            position = question.find(attribute)
            if position != -1:
                attributes_position.append(position)
        return sorted(attributes_position)

    def _remove_subquestion(self, question, attribute_position):
        """
        remove and return the subquestion before the given attribute position
        """
        SeparatorPosition = namedtuple('SeparatorPositions', ['separator', 'position'])
        separator_positions = []
        subquestion = question[:attribute_position]

        for separator in self._separators:
            separator_position = SeparatorPosition(separator, subquestion.rfind(separator))
            if separator_position.position != -1:
                separator_positions.append(separator_position)
        separator_positions = sorted(separator_positions, key=attrgetter('position'))

        subquestion = subquestion[:separator_positions[-1].position]
        self._subquestions.append(subquestion)
        return question[separator_positions[-1].position + len(separator_positions[-1].separator):]