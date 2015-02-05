from Country.CountryRepository import CountryRepository


FIRST_ELEMENT = 0
LAST_ELEMENT = 1
NUMBER_OF_FLAG_PARTS = 9


class FlagCreator:

    def __init__(self, country):
        self._has_next_cubes = False
        self._cube_order = []
        self._creation_zone_height = 0
        self._creation_zone_width = 0
        self._country = CountryRepository().get(country)

        # TODO: Extract cube order from country

    def next_cube(self):
        try:
            next_cube = self.cube_order.pop()
            if not self.cube_order:
                self.has_next_cubes = False
            return next_cube
        except IndexError:
            self.has_next_cubes = False
            print("Cube order list is empty!")
