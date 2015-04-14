from Robot.question_analysis.question_analyser import QuestionAnalyser
from Robot.filler import country_repository_filler

qa = QuestionAnalyser()
country_repository_filler.fill_repository()
print(qa.answer_question('My population is 2 9 3 0 0 5 0.'))
print(qa.answer_question('My capital is Phnom Penh?'))

