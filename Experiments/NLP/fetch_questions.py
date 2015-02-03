import requests

FILENAME = "questions_list"


questions = []
server_address = "https://132.203.14.228/"

for _ in range(500):
    r = requests.get(server_address, verify=False)
    questions.append(r.json()["question"])
questions = set(questions)
with open(FILENAME, 'w') as questions_file:
    for question in questions:
        questions_file.write(question + '\n')
