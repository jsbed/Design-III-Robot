import socket
import sys
from Robot.socket_tcp.data_analysis import data_analysis


HOST = ''
PORT = 4444

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    server_socket.bind((HOST, PORT))
except socket.error as msg:
    print ('Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1])
    sys.exit()

server_socket.listen(10)
print ('Socket listening')

while True:
    connection, address = server_socket.accept()
    print ('Connected with ' + address[0] + ':' + str(address[1]))

    while True:
        data = connection.recv(1024)
        if not data:
            break
        analysis = data_analysis(data)
        reply = analysis.analyse_data()
        connection.sendall(bytes(reply, 'utf-8'))

server_socket.close()
