from Country.CountryRepository import CountryRepository
from Color import Color


class FlagCreator:

    def __init__(self, country):
        self._has_next_cubes = False
        self._cube_order = []
        self._creation_zone_height = 0
        self._creation_zone_width = 0
        self._country = CountryRepository().get(country)

        for color in self._country.flag:
            if color != Color.NONE:
                self._cube_order.append(color)

        for width in self._country.flag[:3]:
            if width != Color.NONE:
                self._creation_zone_width += 1

        for height in self._country.flag[:3]:
            if height != Color.NONE:
                self._creation_zone_height += 1
                break
        for height in self._country.flag[3:6]:
            if height != Color.NONE:
                self._creation_zone_height += 1
                break
        for height in self._country.flag[6:9]:
            if height != Color.NONE:
                self._creation_zone_height += 1
                break

    def next_cube(self):
        try:
            next_cube = self._cube_order.pop()
            if not self._cube_order:
                self._has_next_cubes = False
            return next_cube
        except IndexError:
            self._has_next_cubes = False
            print("Cube order list is empty!")
