from Robot.question_analysis.question_analyser import QuestionAnalyser
from Robot.filler import country_repository_filler

qa = QuestionAnalyser()
country_repository_filler.fill_repository()
print(qa.answer_question('population 2930050'))
print(qa.answer_question('My capital is Paris.'))

