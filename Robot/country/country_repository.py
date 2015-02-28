from Robot.country.country import Country
from Robot.utilities.singleton import Singleton


class CountryRepository(metaclass=Singleton):

    def __init__(self):
        self._country_flags = {}

    def store(self, countries):
        self._country_flags = countries

    def get(self, country):
        if (not country or country not in self._country_flags):
            raise Exception("Country not found in repository")
        else:
            return Country(country, self._country_flags[country])

