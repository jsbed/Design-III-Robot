import os

import zmq

from Robot.communication.serial_port import SerialPort
from Robot.configuration.config import Config
from Robot.country.country_repository import CountryRepository
from Robot.cycle.objects.color import Color
from Robot.cycle.objects.cube import Cube
from Robot.filler import country_repository_filler
from Robot.managers.gripper_manager import GripperManager
from Robot.managers.led_manager import LedManager


PORT = 5000
ADDRESS = "127.0.0.1"

DEPLACEMENT_ENABLE = False
LEDS_ENABLE = False
QUESTION_ENABLE = False
GRIPPER_ENABLED = False

led_manager = None
gripper_manager = None
stm_serial = None

Config().load_config()

if DEPLACEMENT_ENABLE or LEDS_ENABLE:
    stm_serial = SerialPort(Config().get_stm_serial_port_path(
    ), baudrate=Config().get_stm_serial_port_baudrate())

if LEDS_ENABLE:
    flags_file_path = os.path.join("Robot", "resources", "flags.csv")
    country_repository_filler.fill_repository_from_file(flags_file_path)
    led_manager = LedManager(stm_serial)

if GRIPPER_ENABLED:
    pololu_serial = SerialPort(Config().get_pololu_serial_port_path())
    gripper_manager = GripperManager(pololu_serial)


def up():
    print("up command")


def down():
    print("down command")


def left():
    print("left command")


def right():
    print("right command")


def rotate_right():
    print("rotate-right command")


def rotate_left():
    print("rotate-left command")


def ask_question():
    print("ask question")


def display_led_country(message):
    country = message.split(":")[1]

    try:
        country = CountryRepository().get(country)
    except:
        print("Country '{}' not found.".format(country))
    else:
        led_manager.display_country(country)


def display_specific_led(message):
    parameters = message.split(":")
    cube = Cube(Color[parameters[1].upper()], None,
                index=int(parameters[2]) - 1)
    led_manager.display_flag_led_for_next_cube(cube)


context = zmq.Context()
socket = context.socket(zmq.DEALER)
url = "tcp://{}:{}".format(ADDRESS, PORT)
socket.bind(url)
print("Listening on", url)

while True:
    #  Wait for next request from client
    message = socket.recv().decode("utf-8")

    if message == "up" and DEPLACEMENT_ENABLE:
        up()
    elif message == "down" and DEPLACEMENT_ENABLE:
        down()
    elif message == "left" and DEPLACEMENT_ENABLE:
        left()
    elif message == "right" and DEPLACEMENT_ENABLE:
        right()
    elif message == "rotate-right" and DEPLACEMENT_ENABLE:
        rotate_right()
    elif message == "rotate-left" and DEPLACEMENT_ENABLE:
        rotate_left()
    elif message == "ask-question" and QUESTION_ENABLE:
        ask_question()
    elif message.startswith("display led country") and LEDS_ENABLE:
        display_led_country(message)
    elif message.startswith("update led square") and LEDS_ENABLE:
        display_specific_led(message)
    elif message == "open red led" and LEDS_ENABLE:
        led_manager.display_red_led()
    elif message == "close red led" and LEDS_ENABLE:
        led_manager.close_red_led()
    elif message == "close all leds" and LEDS_ENABLE:
        led_manager.close_leds()
    elif message == "take cube" and GRIPPER_ENABLED:
        gripper_manager.take_cube()
    elif message == "drop cube" and GRIPPER_ENABLED:
        gripper_manager.release_cube()
    elif message == "open gripper" and GRIPPER_ENABLED:
        gripper_manager.widest_gripper()
    elif message == "lift gripper" and GRIPPER_ENABLED:
        gripper_manager.lift_gripper()
    elif message == "lower cube" and GRIPPER_ENABLED:
        gripper_manager.lower_gripper()
    else:
        print("Message filtered:", message)
