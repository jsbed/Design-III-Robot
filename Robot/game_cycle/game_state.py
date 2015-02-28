from enum import Enum


class GameState(Enum):
    MOVE_TO_ATLAS_ZONE = 0
    GET_COUNTRY = 1
    DISPLAY_COUNTRY = 2
    CREATE_FLAG = 3
