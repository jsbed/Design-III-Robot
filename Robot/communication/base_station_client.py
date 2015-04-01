import json

from BaseStation.communication.tcp_server import QUESTION_OK_SIGNAL,\
    START_CYCLE_SIGNAL
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

    def send_question(self, question):
        self.send_data(json.dumps({'question': question}))

    def send_country(self, country):
        self.send_data(json.dumps({'country': country.name}))

        # Wait for user response
        response = self.get_data()

        if response == QUESTION_OK_SIGNAL:
            return True
        else:
            return False

    def wait_for_start_cycle_signal(self):
        while self.get_data() != START_CYCLE_SIGNAL:
            pass

    def send_path(self, target_point):
        self.send_data(json.dumps({'path': target_point}))

    def send_cubes_location(self, cube_order):
        cubes = []

        for cube in cube_order:
            cube_position = cube.get_target_zone_position()
            cube_position = [int(cube_position.x), int(cube_position.y)]
            cube_color = cube.get_color().value
            cubes.append({'cube position': cube_position,
                          'cube color': cube_color})

        self.send_data(json.dumps({"cubes": cubes}))

    def log(self, message):
        if message:
            self.send_data(json.dumps({'message': message}))

    def _wait_for_robot_localization_response(self):
        print("waiting response")
        response = self.get_data()
        print("response received")
        return create_localization_from_localization_dto(response)