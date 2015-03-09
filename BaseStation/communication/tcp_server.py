import json

from PySide.QtCore import QThread
import zmq

from BaseStation.ui.utilities.Signal import Signal
from Robot.configuration.config import Config


class TcpServer(QThread):

    def __init__(self):
        QThread.__init__(self)
        self._port = Config().get_base_station_communication_port()
        self._ip = Config().get_base_station_communication_ip()
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.DEALER)
        self.signal = Signal()

    def run(self):
        url = "tcp://{}:{}".format(self._ip, self._port)
        self._socket.bind(url)
        self._send_message("Base Station Server listening on port " +
                           str(self._port))
        self._wait_for_messages()

    def _wait_for_messages(self):
        while True:
            try:
                data = self._socket.recv().decode("utf-8")
                self.signal.customSignal.emit(data)
            except Exception as e:
                print(e)
                self._send_message("Base Station Server error: " + str(e))

    def _send_message(self, message):
        self.signal.customSignal.emit(json.dumps({"message": message}))
