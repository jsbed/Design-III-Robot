from Robot.game_cycle.objects.color import Color


class FlagCreator:

    def __init__(self, country):
        self._has_next_cubes = True
        self._cube_order = []
        self._creation_zone_height = 0
        self._creation_zone_width = 0
        self._country = country

        for color in self._country.flag:
            if color != Color.NONE:
                self._cube_order.append(color)

    def get_has_next_cubes(self):
        return self._has_next_cubes

    def get_cube_order(self):
        return self._cube_order

    def get_creation_zone_height(self):
        return self._creation_zone_height

    def get_creation_zone_width(self):
        return self._creation_zone_width

    def get_country(self):
        return self._country

    def next_cube(self):
        try:
            next_cube = self._cube_order.pop()
            if not self._cube_order:
                self._has_next_cubes = False
            return next_cube
        except IndexError:
            self._has_next_cubes = False
            print("Cube order list is empty!")
