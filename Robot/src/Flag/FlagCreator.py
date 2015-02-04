from collections.__main__ import Point
from turtledemo.chaos import line

from Cube import Cube


FIRST_ELEMENT = 0
LAST_ELEMENT = 1
NUMBER_OF_FLAG_PARTS = 9


class FlagCreator:

    def __init__(self):
        self.has_next_cubes = False
        self.cube_order = []
        self.creation_zone_height = 0
        self.creation_zone_width = 0

    def FlagCreator(self, country):
        flags = open("flags.txt", "r")

        for line in flags:
            if country.name in line:
                no_end_line = line.rsplit('\n')[FIRST_ELEMENT]
                for color_position in range(1, 10):
                    color_split = no_end_line.rsplit(',', NUMBER_OF_FLAG_PARTS)[color_position]
                    color = color_split.rsplit(' ')[LAST_ELEMENT]
                    if color != "NONE":
                        self.cube_order.append(Cube(color, color_position, False, (Point(0, 0), 0)))
                        '''
                        TODO:
                        creation zone size
                        '''
        flags.close()

    def next_cube(self):
        try:
            next_cube = self.cube_order.pop()
            if not self.cube_order:
                self.has_next_cubes = False
            return next_cube
        except IndexError:
            self.has_next_cubes = False
            print("Cube order list is empty!")
