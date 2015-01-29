import requests

FILENAME = "questions_list"


questions = []
server_address = "https://132.203.14.228/"

for _ in range(500):
    r = requests.get(server_address, verify=False)
    questions.append(r.json()["question"])
questions = set(questions)
print(questions)
with open(FILENAME, 'a') as questions_file:
    for question in questions:
        questions_file.write(question + '\n')
