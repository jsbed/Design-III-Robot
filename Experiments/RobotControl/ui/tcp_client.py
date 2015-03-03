import zmq


class TCPClient():

    def __init__(self, host, port):
        self._host = host
        self._port = port
        self._context = zmq.Context()
        self._socket = None

    def set_host(self, value):
        self._host = value

    def set_port(self, value):
        self._port = value

    def connect_socket(self):
        try:
            self._socket.connect("tcp://{}:{}".format(self._host, self._port))
        except:
            return False
        else:
            return True

    def disconect_socket(self):
        try:
            self._socket.close()
        except:
            pass

        self._socket = self._context.socket(zmq.DEALER)

    def send_data(self, data):
        try:
            self._socket.send(data)
        except:
            print('Send failed')
