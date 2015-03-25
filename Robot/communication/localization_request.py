import json

ROBOT_LOCALIZATION_REQUEST = "robot-localization"
CUBE_LOCALIZATION_REQUEST = "cube-localization"


def create_robot_localization_request():
    return json.dumps({"request": ROBOT_LOCALIZATION_REQUEST}, "utf-8")


def create_cube_localization_request():
    return json.dumps({"request": CUBE_LOCALIZATION_REQUEST}, "utf-8")
