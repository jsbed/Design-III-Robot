from PySide.QtCore import QThread
import json
import zmq

from BaseStation.ui.utilities.Signal import Signal
from Robot.communication import localization_request, localization_response
from Robot.communication.localization_request import ROBOT_LOCALIZATION_REQUEST,\
    CUBE_LOCALIZATION_REQUEST
from Robot.communication.localization_response import create_localization_response
from Robot.configuration.config import Config
from Robot.cycle.objects.color import Color
from Robot.locators import robot_locator, cube_locator


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
                self._interprete_received_data(data)
            except Exception as e:
                self._send_message("Base Station Server error: " + str(e))

    def _interprete_received_data(self, received_data):
        if "request" in received_data:
            self._handle_robot_request(received_data)
        else:
            self.signal.customSignal.emit(received_data)

    def _send_message(self, message):
        self.signal.customSignal.emit(json.dumps({"message": message}))

    def _handle_robot_request(self, received_data):
        received_data = json.loads(received_data)

        if received_data["request"] == ROBOT_LOCALIZATION_REQUEST:
            self._send_robot_localization_response()
        elif received_data["request"] == CUBE_LOCALIZATION_REQUEST:
            self._send_cube_localization_response(
                Color(received_data["color"]))

    def _send_robot_localization_response(self):
        robot_localization = robot_locator.localize()
        self._send_localization(robot_localization)

    def _send_cube_localization_response(self, color):
        cube_localization = cube_locator.localize_with_kinect(color)
        self._send_localization(cube_localization)

    def _send_localization(self, localization):
        localization_response = create_localization_response(localization)
        self._socket.send(bytes(localization_response, "utf-8"))