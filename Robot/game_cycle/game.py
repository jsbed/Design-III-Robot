from Robot.controller.robot_controller import RobotController
from Robot.country.country import Country
from Robot.country.flag_creator import FlagCreator
from Robot.game_cycle.game_state import GameState
from Robot.locators.localization import Localization
from Robot.path_finding.point import Point
from Robot.question_analysis.question_analyser import QuestionAnalyser


class Game:

    def __init__(self):
        self._state = GameState.MOVE_TO_ATLAS_ZONE
        self._target_zone_location = []
        self._country = Country("", [])
        self._robot_controller = RobotController()
        self._question = ""
        self._question_analyser = QuestionAnalyser()
        self._cube_position = Localization(Point(0, 0), 0)
        self._current_cube = 0

    def get_state(self):
        return self._state

    def start(self):
        self._robot_controller.move_to_atlas()

    def localise_cube(self):
        pass

    def analyze_question(self):
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
        while (self._flag_creator.has_next_cubes()):
            next_cube = self._flag_creator.next_cube()
            self._robot_controller.ask_for_cube(next_cube)
            # TODO: Localize Cube
            self._robot_controller.get_cube(
                self._cube_list[self._current_cube])
            self._robot_controller.move_cube(
                self._cube_list[self._current_cube])
            self._current_cube = self._current_cube + 1

    def display_country(self):
        self._robot_controller.display_country_leds(self._country)

    def construct_flag(self):
        self._flag_creator = FlagCreator(self._country)
