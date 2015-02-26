import json
import socket

from PySide.QtCore import QThread

from BaseStation.ui.utilities.Signal import Signal
from Robot.configuration.config import Config


BUFFER_SIZE = 999


class TcpServer(QThread):

    def __init__(self):
        QThread.__init__(self)
        self._port = Config().get_base_station_communication_port()
        self._ip = Config().get_base_station_communication_ip()
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind((self._ip, self._port))
        self.signal = Signal()

    def run(self):
        self._socket.listen(1)
        self._send_message("Base Station Server listening on port " + str(self._port))
        self._wait_for_messages()

    def _wait_for_messages(self):
        while True:
            connection, _ = self._socket.accept()

            try:
                data = connection.recv(BUFFER_SIZE)
                self.signal.customSignal.emit(data.decode("utf-8"))
            except Exception as e:
                print(e)
                self._send_message("Base Station Server error: " + str(e))
                #connection.close()

    def _send_message(self, message):
        self.signal.customSignal.emit(json.dumps({"message": message}))
