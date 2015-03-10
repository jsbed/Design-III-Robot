from Robot.controller.robot_controller import RobotController
from Robot.country.country import Country
from Robot.country.flag_creator import FlagCreator
from Robot.game_cycle.game_state import GameState
from Robot.question_analysis.question_analyser import QuestionAnalyser
from time import sleep


class Game:

    def __init__(self):
        self._country = Country("", [])
        self._robot_controller = RobotController()
        self._question = ""
        self._question_analyser = QuestionAnalyser()
        self._cycle_done = False

    def get_state(self):
        return self._state

    def start(self):
        self._state = GameState.MOVE_TO_ATLAS_ZONE
        self.next_state()

    def localize_cube(self):
        while not(self._cube.get_localization().position.x == -1) \
                and not(self._cube.get_localization().position.y == -1):
            # Check if cube is found every 2 seconds.
            sleep(2)
        self._state = GameState.MOVE_TO_CUBE
        self.next_state()

    def analyze_question(self):
        self._country = self._question_analyser.answer_question(self._question)

    def next_state(self):
        if (self._state == GameState.MOVE_TO_ATLAS_ZONE):
            if(self._robot_controller.move_to_atlas(self._robot)):
                self._state = GameState.DISPLAY_COUNTRY
                self.next_state()
        elif (self._state == GameState.DISPLAY_COUNTRY):
            self._question = self._robot_controller.get_question_from_atlas()
            self.analyze_question()
            self.construct_flag()
            self.display_country()
            self._state = GameState.ASK_FOR_CUBE
            self.next_state()
        elif (self._state == GameState.ASK_FOR_CUBE):
            self.add_new_cube()
            if not(self._cycle_done):
                self._robot_controller.ask_for_cube(self._cube)
                self.localize_cube()
            else:
                self.start()  # Start a new cycle.
        elif (self._state == GameState.MOVE_TO_CUBE):
            if(self._robot_controller.get_cube(self._cube)):
                self._state = GameState.PICK_UP_CUBE
                self.next_state()
        elif (self._state == GameState.PICK_UP_CUBE):
            # TODO: Pick up cube
            pass
        elif (self._state == GameState.MOVE_TO_TARGET_ZONE):
            if(self._robot_controller.move_cube(self._cube)):
                self._state = GameState.PUT_DOWN_CUBE
                self.next_state()
        elif (self._state == GameState.PUT_DOWN_CUBE):
            # TODO: Put down cube
            self._state = GameState.ASK_FOR_CUBE
            self.next_state()

    def add_new_cube(self):
        if (self._flag.has_next_cubes()):
            self._cube = self._flag.next_cube()
            self._cycle_done = False
        else:
            print("Game cycle is done")
            self._cycle_done = True

    def display_country(self):
        # TODO: Send question and country to base station.
        self._robot_controller.display_country_leds(self._country)

    def construct_flag(self):
        self._flag = FlagCreator(self._country)
