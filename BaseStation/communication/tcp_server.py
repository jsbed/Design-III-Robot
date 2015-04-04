import json

from PySide.QtCore import QThread
import zmq

from BaseStation.ui.utilities.Signal import Signal
from Robot.communication.dtos.localization_dto import create_localization_dto
from Robot.configuration.config import Config


QUESTION_OK_SIGNAL = "question ok signal"
ASK_NEW_QUESTION_SIGNAL = "ask new question"
START_CYCLE_SIGNAL = "start cycle"


class TcpServer(QThread):

    def __init__(self):
        QThread.__init__(self)
        self._port = Config().get_base_station_port()
        self._ip = Config().get_base_station_ip()
        self._context = zmq.Context()
        self._socket = self._context.socket(zmq.DEALER)  # @UndefinedVariable
        self.signal = Signal()

    def send_question_ok_signal(self):
        self._socket.send(bytes(QUESTION_OK_SIGNAL, "utf-8"))

    def send_new_question_signal(self):
        self._socket.send(bytes(ASK_NEW_QUESTION_SIGNAL, "utf-8"))

    def send_start_cycle_signal(self):
        self._socket.send(bytes(START_CYCLE_SIGNAL, "utf-8"))

    def run(self):
        url = "tcp://{}:{}".format(self._ip, self._port)
        self._socket.bind(url)
        self._send_message("Base Station Request Server listening on port " +
                           str(self._port))
        self._wait_for_messages()

    def _wait_for_messages(self):
        while True:
            try:
                data = self._socket.recv().decode("utf-8")
                self.signal.custom_signal.emit(data)
            except Exception as e:
                self._send_message("Base Station Server error: " + str(e))

    def _send_message(self, message):
        self.signal.custom_signal.emit(json.dumps({"message": message}))

    def send_localization_response(self, localization):
        localization_dto = create_localization_dto(localization)
        self._socket.send(bytes(localization_dto, "utf-8"))
