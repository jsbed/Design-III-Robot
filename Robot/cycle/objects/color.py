from enum import Enum


class Color(Enum):
    NONE = 0
    RED = 1
    GREEN = 2
    BLUE = 3
    YELLOW = 4
    WHITE = 5
    BLACK = 6
    PINK = 7
    ORANGE = 8

    @staticmethod
    def is_segmentable(color):
        return color.value != 5 and color.value != 6 and color.value != 0
