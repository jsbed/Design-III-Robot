from Robot.question_analysis.question_analyser import QuestionAnalyser
from Robot.filler import country_repository_filler

qa = QuestionAnalyser()
country_repository_filler.fill_repository()
print(qa.answer_question('the capital is paris'))
print(qa.answer_question('One major urban area is Toronto.'))
print(qa.answer_question('The climate is tropical and has a capital that starts with the letters Phn?'))

