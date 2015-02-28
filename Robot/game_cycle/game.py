from collections.__main__ import Point

from Robot.controller.robot_controller import RobotController
from Robot.country.country import Country
from Robot.country.flag_creator import FlagCreator
from Robot.game_cycle.game_state import GameState
from Robot.game_cycle.object.cube import Cube
from Robot.locators.localization import Localization
from Robot.question_analysis.question_analyser import QuestionAnalyser


class Game:

    def __init__(self):
        self._state = GameState.MOVE_TO_ATLAS_ZONE
        self._target_zone_location = []
        self._cube_list = []
        self._country = Country("", [])
        self._robot_service = RobotController()
        self._question = ""
        self._question_analyser = QuestionAnalyser()
        self._cube_position = Localization(Point(0, 0), 0)
        self._current_cube = 0

    def get_state(self):
        return self._state

    def start(self):
        self._robot_service.move_to_atlas()

    def localise_cube(self):
        pass

    def localise_atlas(self):
        pass

    def localise_target_zone(self):
        pass

    def analyze_question(self):
        # self._question = atlas.get_question()
        # self._country = self._question_analyser.answer_question(self._question)
        pass

    def next_state(self):
        if (self._state == GameState.MOVE_TO_ATLAS_ZONE):
            self._state = GameState.GET_COUNTRY
            self.analyze_question()
        elif (self._state == GameState.GET_COUNTRY):
            self._state = GameState.DISPLAY_COUNTRY
            self.display_country()
        elif (self._state == GameState.DISPLAY_COUNTRY):
            self._state = GameState.CREATE_FLAG
            self.construct_flag()
            self.add_new_cube()
        elif (self._state == GameState.CREATE_FLAG):
            self._state = GameState.MOVE_TO_ATLAS_ZONE
            self.start()

    def add_new_cube(self):
        while (self._flag.get_has_next_cubes()):
            self._cube_list.append(
                Cube(self._flag.next_cube(),
                     self._target_zone_location[self._current_cube],
                     False,
                     self._cube_position))
            self._robot_service.ask_for_cube(
                self._cube_list[self._current_cube])
            # TODO: Localize Cube
            self._robot_service.get_cube(self._cube_list[self._current_cube])
            self._robot_service.move_cube(self._cube_list[self._current_cube])
            self._current_cube = self._current_cube + 1

    def display_country(self):
        self._robot_service.display_country_leds(self._country)

    def construct_flag(self):
        self._flag = FlagCreator(self._country)
