from time import sleep

from Robot.communication.tcp_client import TCPClient
from Robot.configuration.config import Config
from Robot.controller.robot_controller import RobotController
from Robot.country.country import Country
from Robot.country.flag_creator import FlagCreator
from Robot.cycle.cycle_state import CycleState
from Robot.question_analysis.question_analyser import QuestionAnalyser

CHECK_FOR_CUBE_DELAY = 2
POSITION_NOT_FOUND = [(-1, -1), (-1, 1), (1, -1)]


class Cycle:

    def __init__(self):
        self._country = Country("", [])
        self._robot_controller = RobotController()
        self._question = ""
        self._question_analyser = QuestionAnalyser()
        self._client = TCPClient(Config().
                                 get_base_station_communication_ip(),
                                 Config().
                                 get_base_station_communication_port())

    def get_state(self):
        return self._state

    def start_cycle(self):
        self._state = CycleState.MOVE_TO_ATLAS_ZONE
        self._next_state()

    def _next_state(self):
        if (self._state == CycleState.MOVE_TO_ATLAS_ZONE):
            self._atlas_zone_state()

        elif (self._state == CycleState.DISPLAY_COUNTRY):
            self._display_country_state()

        elif (self._state == CycleState.ASK_FOR_CUBE):
            self._ask_for_cube_state()

        elif (self._state == CycleState.MOVE_TO_CUBE):
            self._move_to_cube_state()

        elif (self._state == CycleState.PICK_UP_CUBE):
            self._pick_up_cube_state()

        elif (self._state == CycleState.MOVE_TO_TARGET_ZONE):
            self._move_to_target_zone_state()

        elif (self._state == CycleState.PUT_DOWN_CUBE):
            self._put_down_cube_state()

    def _atlas_zone_state(self):
        if(self._robot_controller.arrived_at_zone_atlas()):
            self._state = CycleState.DISPLAY_COUNTRY
            self._next_state()

        else:
            self._robot_controller.move_to_atlas()

    def _display_country_state(self):
        self._question = self._robot_controller.get_question_from_atlas()
        self._country = self._question_analyser.answer_question(self._question)
        self._flag = FlagCreator(self._country)
        self._state = CycleState.ASK_FOR_CUBE

        self._display_country()
        self._next_state()

    def _ask_for_cube_state(self):
        cycle_done = False

        if (self._flag.has_next_cubes()):
            self._cube = self._flag.next_cube()

        else:
            cycle_done = True

        if not(cycle_done):
            self._robot_controller.ask_for_cube(self._cube)
            self._localize_cube()

        else:
            self.start_cycle()

    def _move_to_cube_state(self):
        cube_position = self._cube.get_localization().position

        if(self._robot_controller.
           robot_is_next_to_target_with_correct_orientation(cube_position)):
            self._state = CycleState.PICK_UP_CUBE
            self._next_state()

        else:
            self._robot_controller.move_robot_to(cube_position)

    def _pick_up_cube_state(self):
        # TODO: Pick up cube
        pass

    def _move_to_target_zone_state(self):
        target_zone = self._cube.get_target_zone_position()

        if(self._robot_controller.
           robot_is_next_to_target_with_correct_orientation(target_zone)):
            self._state = CycleState.PUT_DOWN_CUBE
            self._next_state()

        else:
            self._robot_controller.move_robot_to(target_zone)

    def _put_down_cube_state(self):
        # TODO: Put down cube
        self._state = CycleState.ASK_FOR_CUBE
        self._next_state()

    def _localize_cube(self):
        while (self._cube.get_localization().position in POSITION_NOT_FOUND):
            sleep(CHECK_FOR_CUBE_DELAY)

        self._state = CycleState.MOVE_TO_CUBE
        self._next_state()

    def _display_country(self):
        self._client.connect_socket()
        self._client.send_data({'question': self._question,
                                'country': self._country})
        self._client.disconnect_socket()

        self._robot_controller.display_country_leds(self._country)
