import time

from Robot.communication.base_station_client import BaseStationClient
from Robot.controller.robot import INSTRUCTION_FINISHED, SWITCH_ACTIVATED,\
    SWITCH_DEACTIVATED
from Robot.controller.robot_controller import RobotController
from Robot.country.country import Country
from Robot.country.country_repository import CountryRepository
from Robot.country.flag_creator import FlagCreator
from Robot.cycle.cycle_state import CycleState
from Robot.cycle.objects.cube import Cube
from Robot.question_analysis.question_analyser import QuestionAnalyser
from Robot.utilities.observer import Observer


CHECK_FOR_CUBE_DELAY = 2
WAIT_TIME_BETWEEN_GRIPPERS_ACTION = 2


class Cycle(Observer):

    def __init__(self):
        self._country = Country("", [])
        self._robot_controller = RobotController()
        self._question = ""
        self._cube = Cube(None, None)
        self._state = CycleState.MOVE_TO_ATLAS_ZONE
        self._flag_creator = None
        self._robot_controller.get_robot().attach(INSTRUCTION_FINISHED, self)
        self._robot_controller.get_robot().attach(SWITCH_ACTIVATED, self)
        self._robot_controller.get_robot().attach(SWITCH_DEACTIVATED, self)

    def observer_update(self, event, value):
        if (event == SWITCH_ACTIVATED):
            self._robot_controller.turn_switch_on()
        elif (event == SWITCH_DEACTIVATED):
            self._robot_controller.turn_switch_off()
        elif (event == INSTRUCTION_FINISHED):
            self.continue_cycle()

    def start_cycle(self):
        self._state = CycleState.MOVE_TO_ATLAS_ZONE
        self._next_state()

    def continue_cycle(self):
        if not self._robot_controller.instruction_remaining():
            self._next_state()
        else:
            print("next instruction")
            self._robot_controller.next_instruction()

    def set_state(self, state):
        self._state = state

    def _next_state(self):
        if (self._state == CycleState.MOVE_TO_ATLAS_ZONE):
            print("move to atlas state")
            self._atlas_zone_state()

        elif (self._state == CycleState.DISPLAY_COUNTRY):
            print("display country state")
            self._display_country_state()

        elif (self._state == CycleState.ASK_FOR_CUBE):
            print("ask for cube")
            self._ask_for_cube_state()

        elif (self._state == CycleState.LOCALIZE_CUBE):
            print("localize cube")
            self._localize_cube_state()

        elif (self._state == CycleState.MOVE_TO_CUBE):
            print("move to cube")
            self._move_to_cube_state()

        elif (self._state == CycleState.PUSH_CUBE):
            print("push cube")
            self._push_cube_state()

        elif (self._state == CycleState.PICK_UP_CUBE):
            print("pick up cube")
            self._pick_up_cube_state()

        elif (self._state == CycleState.MOVE_TO_TARGET_ZONE):
            print("move to target zone")
            self._move_to_target_zone_state()

        elif (self._state == CycleState.MOVE_INTO_TARGET_ZONE):
            print("move into target zone")
            self._move_into_target_zone_state()

        elif (self._state == CycleState.PUT_DOWN_CUBE):
            print("put down cube")
            self._put_down_cube_state()

    def _atlas_zone_state(self):
        print("atlas zone state")
        if(self._robot_controller.arrived_at_zone_atlas()):
            print("arrived")
            self._state = CycleState.DISPLAY_COUNTRY
            self._next_state()
        else:
            print("moving to atlas")
            self._robot_controller.move_to_atlas()

    def _display_country_state(self):
        country_is_correct = False

        while not country_is_correct:
            self._get_question_from_atlas()
            country_is_correct = self._analyse_question()

        self._robot_controller.display_country_leds(self._country)
        self._flag_creator = FlagCreator(self._country)
        BaseStationClient().send_cubes_location(
            self._flag_creator.get_cube_order())
        self._state = CycleState.ASK_FOR_CUBE
        self._next_state()

    def _ask_for_cube_state(self):
        cycle_done = False

        if (self._flag_creator.has_next_cubes()):
            self._cube = self._flag_creator.next_cube()

        else:
            cycle_done = True

        if not cycle_done:
            self._robot_controller.ask_for_cube(self._cube)
            self._state = CycleState.LOCALIZE_CUBE
            self._robot_controller.move_robot_to_localize_cube()

    def _localize_cube_state(self):
        self._robot_controller.get_gripper().widest_gripper()
        time.sleep(WAIT_TIME_BETWEEN_GRIPPERS_ACTION)
        while (self._cube.get_localization().position is None):
            time.sleep(CHECK_FOR_CUBE_DELAY)
        self._state = CycleState.MOVE_TO_CUBE
        self._next_state()

    def _move_to_cube_state(self):
        cube_position = self._cube.get_localization().position

        if(self._robot_controller.
           robot_is_next_to_target_with_correct_orientation(cube_position)):
            self._state = CycleState.PUSH_CUBE
            self._next_state()

        else:
            self._robot_controller.move_robot_to(cube_position)

    def _push_cube_state(self):
        if (self._robot_controller.get_switch_status()):
            self._state = CycleState.PICK_UP_CUBE
            self._next_state()
        else:
            self._robot_controller.push_cube(
                self._cube.get_localization().position)

    def _pick_up_cube_state(self):
        self._robot_controller.get_gripper().take_cube()
        time.sleep(WAIT_TIME_BETWEEN_GRIPPERS_ACTION)
        self._robot_controller.get_gripper().lift_gripper()
        time.sleep(WAIT_TIME_BETWEEN_GRIPPERS_ACTION)
        self._state = CycleState.MOVE_TO_TARGET_ZONE
        self._next_state()

    def _move_to_target_zone_state(self):
        target_zone = self._cube.get_target_zone_position()

        if(self._robot_controller.
           robot_is_next_to_target_with_correct_orientation(target_zone)):
            self._state = CycleState.MOVE_INTO_TARGET_ZONE
            self._next_state()
        else:
            self._robot_controller.move_robot_to(target_zone)

    def _move_into_target_zone_state(self):
        self._state = CycleState.PUT_DOWN_CUBE
        self._robot_controller.move_forward_to_target_zone(
            self._cube.get_target_zone_position())

    def _put_down_cube_state(self):
        self._robot_controller.get_gripper().lower_gripper()
        time.sleep(WAIT_TIME_BETWEEN_GRIPPERS_ACTION)
        self._robot_controller.get_gripper().release_cube()
        time.sleep(WAIT_TIME_BETWEEN_GRIPPERS_ACTION)
        self._state = CycleState.ASK_FOR_CUBE
        self._robot_controller.move_backward()

    def _get_question_from_atlas(self):
        self._question = self._robot_controller.get_question_from_atlas()
        BaseStationClient().send_question(self._question)

    def _analyse_question(self):
        country_name = QuestionAnalyser().answer_question(self._question)
        self._country = CountryRepository().get(country_name)

        return BaseStationClient().send_country(self._country)
