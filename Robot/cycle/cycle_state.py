from enum import Enum


class CycleState(Enum):
    MOVE_TO_ATLAS_ZONE = 0
    DISPLAY_COUNTRY = 1
    ASK_FOR_CUBE = 2
    MOVE_TO_CUBE = 3
    PUSH_CUBE = 4
    PICK_UP_CUBE = 5
    MOVE_TO_TARGET_ZONE = 6
    MOVE_INTO_TARGET_ZONE = 7
    PUT_DOWN_CUBE = 8
