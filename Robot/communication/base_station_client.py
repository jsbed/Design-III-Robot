import json

from Robot.communication.localization.localization_dto import create_localization_from_localization_dto
from Robot.communication.localization.localization_request import create_robot_localization_request
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

    def send_question_and_country(self, question, country):
        self.send_data(json.dumps({'question': question, 'country': country}))
        return self.get_data()

    def send_path(self, target_point):
        self.send_data(json.dumps({'path': target_point}))

    def log(self, message):
        if message:
            self.send_data(json.dumps({'message': message}))

    def _wait_for_robot_localization_response(self):
        return create_localization_from_localization_dto(self.get_data())
