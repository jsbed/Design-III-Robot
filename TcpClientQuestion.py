import json
import os
import socket

from Robot.configuration.config import Config


Config("Robot/config.ini").load_config()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = (Config().get_base_station_communication_ip(),
                  Config().get_base_station_communication_port())

print('connecting to %s port %s' % server_address)

sock.connect(server_address)
question = input('question: ')
country = input('country: ')

sock.sendall(bytes(json.dumps({'question' : question, 'country': country}), "utf-8"))

sock.close()