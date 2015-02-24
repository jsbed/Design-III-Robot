import socket
import sys


class TCPClient():

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect_socket(self):
        self._socket.connect((self._host, self._port))
        print('Socket Connected to ' + str(self._host))

    def diconnect_socket(self):
        self._socket = None

    def send_data(self, data):
        try:
            self._socket.sendall(data)
        except socket.error:
            print('Send failed')
            sys.exit()

    def get_data(self):
        try:
            reply = self._socket.recv(1024)
            return reply
        except socket.error:
            print('No data to receive')
            sys.exit()
