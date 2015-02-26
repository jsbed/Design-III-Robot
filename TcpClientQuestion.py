import json
import random
import socket

from Robot.configuration.config import Config
from Robot.question_analysis.question_analyser import QuestionAnalyser


def get_random_question():
    with open('Experiments/NLP/questions_list') as f:
        line_number = random.randint(1, 26)
        counter = 1
        for line in f:
            if counter == line_number:
                return line
            else:
                counter += 1

Config("Robot/config.ini").load_config()


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (Config().get_base_station_communication_ip(),
                  Config().get_base_station_communication_port())

print('connecting to %s port %s' % server_address)
sock.connect(server_address)

analyser = QuestionAnalyser()
question = get_random_question().rstrip()
country = analyser.answer_question(question)
print("Question: " + question)
print("Country: " + country)
print("Sending to Base Station...")

sock.sendall(bytes(json.dumps({'question' : question, 'country': country}), "utf-8"))

sock.close()