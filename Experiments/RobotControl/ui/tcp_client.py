import socket


class TCPClient():

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def set_host(self, value):
        self._host = value

    def set_port(self, value):
        self._port = value

    def connect_socket(self):
        try:
            self._socket.connect((self._host, self._port))
        except (ConnectionRefusedError, socket.gaierror, OverflowError) as e:
            print(str(e))
            return False
        else:
            return True

    def diconnect_socket(self):
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def send_data(self, data):
        try:
            self._socket.sendall(data)
        except socket.error:
            print('Send failed')
