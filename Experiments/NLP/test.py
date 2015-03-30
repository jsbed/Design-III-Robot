from Robot.question_analysis.question_analyser import QuestionAnalyser

lines = [line.rstrip('\n') for line in open("new_questions_list")]

for question in lines:
    print(QuestionAnalyser().answer_question(question))
