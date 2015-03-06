import socket
import sys


class TCPClient():

    def __init__(self):
        self._host = 'localhost'
        self._port = 3000
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_socket(self):
        self._socket.connect((self._host, self._port))
        print('Socket Connected to ' + str(self._host))

    def diconnect_socket(self):
        self._socket.close()

    def send_data(self, data):
        try:
            self._socket.sendall(data)
        except socket.error:
            print('Send failed')
            sys.exit()
