import json
import random

import zmq

from Robot.configuration.config import Config
from Robot.question_analysis.question_analyser import QuestionAnalyser


def get_random_question():
    with open('Experiments/NLP/questions_list') as f:
        line_number = random.randint(1, 21)
        counter = 1
        for line in f:
            if counter == line_number:
                return line
            else:
                counter += 1

Config().load_config()


# Create a TCP/IP socket
context = zmq.Context()
socket = context.socket(zmq.DEALER)
url = "tcp://{}:{}".format(
    Config().get_base_station_communication_ip(),
    Config().get_base_station_communication_port())
socket.connect(url)
print('connecting to ' + url)

analyser = QuestionAnalyser()
question = get_random_question().rstrip()
print("Question: " + question)
country = analyser.answer_question(question)

print("Country: " + country)
print("Sending to Base Station...")

socket.send(
    bytes(json.dumps({'question': question, 'country': country}), "utf-8"))
