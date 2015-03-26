from Robot.communication.localization.localization_request import create_robot_localization_request
from Robot.communication.localization.localization_response import create_localization_from_localization_response
from Robot.communication.tcp_client import TCPClient
from Robot.configuration.config import Config
from Robot.utilities.singleton import Singleton


class BaseStationClient(TCPClient, metaclass=Singleton):

    def __init__(self):
        TCPClient.__init__(self, Config().get_base_station_communication_ip(),
                           Config().get_base_station_communication_port())

    def request_robot_localization(self):
        robot_localization_request = create_robot_localization_request()
        self.send_data(robot_localization_request)

        return self._wait_for_robot_localization_response()

    def _wait_for_robot_localization_response(self):
        return create_localization_from_localization_response(self.get_data())
