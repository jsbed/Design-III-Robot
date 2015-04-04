import json

from BaseStation.communication.tcp_server import QUESTION_OK_SIGNAL,\
    START_CYCLE_SIGNAL
from Robot.communication.dtos.cube_order_dto import create_cube_order_dto
from Robot.communication.dtos.localization_dto import create_localization_from_localization_dto
from Robot.communication.requests.localization_request import create_robot_localization_request
from Robot.communication.tcp_client import TCPClient
from Robot.configuration.config import Config
from Robot.utilities.singleton import Singleton


class BaseStationClient(TCPClient, metaclass=Singleton):

    def __init__(self):
        TCPClient.__init__(self, Config().get_base_station_ip(),
                           Config().get_base_station_port())

    def request_robot_localization(self):
        robot_localization_request = create_robot_localization_request()
        self.send_data(robot_localization_request)

        return self._wait_for_robot_localization_response()

    def send_question(self, question):
        self.send_data(json.dumps({'question': question}))

    def send_country(self, country):
        self.send_data(json.dumps({'country': country.name}))

        return self._wait_for_user_country_response()

    def wait_for_start_cycle_signal(self):
        while self.get_data() != START_CYCLE_SIGNAL:
            pass

    def send_path(self, target_point):
        self.send_data(json.dumps({'path': target_point}))

    def send_end_signal(self):
        self.send_data(json.dumps({'end-signal': ""}))

    def send_cubes_location(self, cube_order):
        cube_order_dto = create_cube_order_dto(cube_order)
        self.send_data(cube_order_dto)

    def log(self, message):
        if message:
            self.send_data(json.dumps({'message': message}))

    def _wait_for_user_country_response(self):
        return QUESTION_OK_SIGNAL == self.get_data()

    def _wait_for_robot_localization_response(self):
        print("waiting response")
        response = self.get_data()
        print("response received")
        return create_localization_from_localization_dto(response)
