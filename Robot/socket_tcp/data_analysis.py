from Robot.question_analysis.question_analyser import QuestionAnalyser


class data_analysis():

    def __init__(self, data):
        self._data = data
        self._reply = 'Empty'
        self._question_analyser = QuestionAnalyser()
        self._question = 'My unemployment rate is 40.6%.'

    def analyse_data(self):
        if (self._data == (b'GET QUESTION')):
            self._reply = self._question
        elif (self._data == (b'GET ANSWER')):
            self._reply = self._question_analyser.answer_question(
                self._question)
        return self._reply
