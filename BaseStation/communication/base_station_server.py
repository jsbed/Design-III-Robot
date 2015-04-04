from PySide.QtCore import QThread
import json

from BaseStation.ui.utilities.Signal import Signal
from Robot.communication.dtos.localization_dto import create_localization_dto
from Robot.communication.tcp_server import TcpServer
from Robot.configuration.config import Config


QUESTION_OK_SIGNAL = "question ok signal"
ASK_NEW_QUESTION_SIGNAL = "ask new question"
START_CYCLE_SIGNAL = "start cycle"


class BaseStationServer(TcpServer, QThread):

    def __init__(self):
        TcpServer.__init__(self, Config().get_base_station_ip(),
                           Config().get_base_station_port())
        QThread.__init__(self)
        self.signal = Signal()

    def send_question_ok_signal(self):
        self.send_data(QUESTION_OK_SIGNAL)

    def send_new_question_signal(self):
        self.send_data(ASK_NEW_QUESTION_SIGNAL)

    def send_start_cycle_signal(self):
        self.send_data(START_CYCLE_SIGNAL)

    def run(self):
        self.start_server()
        self._send_message("Base Station Request Server listening on port " +
                           str(self._port))
        self._wait_for_messages()

    def _wait_for_messages(self):
        while True:
            try:
                self.signal.custom_signal.emit(self.get_data())
            except Exception as e:
                self._send_message("Base Station Server error: " + str(e))

    def _send_message(self, message):
        self.signal.custom_signal.emit(json.dumps({"message": message}))

    def send_localization_response(self, localization):
        localization_dto = create_localization_dto(localization)
        self._socket.send(bytes(localization_dto, "utf-8"))
