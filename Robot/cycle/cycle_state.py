from enum import Enum


class CycleState(Enum):
    MOVE_TO_ATLAS_ZONE = 0
    DISPLAY_COUNTRY = 1
    ASK_FOR_CUBE = 2
    MOVE_TO_CUBE = 3
    PICK_UP_CUBE = 4
    MOVE_TO_TARGET_ZONE = 5
    PUT_DOWN_CUBE = 6
