import os
import pickle


INFO_KEY_ALIAS = {'capital': ['Capital', 'name'], 'unemployment rate': ['Unemployment rate', 'description'],
                  'population': ['Population', 'description'],
                  'major urban areas': ['Major urban areas - population', 'description'],
                  'national symbol': ['National symbol(s)'], 'religions': ['Religions', 'description'],
                  'country code': ['Internet country code'], 'independence': ['Independence', 'description'],
                  'population growth rate': ['Population growth rate', 'description'],
                  'geographic coordinates': ['Geographic coordinates', 'description'],
                  'electricity production': ['Electricity - production', 'description'],
                  'total area': ['Area', 'total'], 'national anthem': ['National anthem', 'name'],
                  'death rate': ['Death rate', 'description'], 'industries': ['Industries', 'description'],
                  'internet users': ['Internet users', 'description'], 'languages': ['Languages', 'description'],
                  'import partners': ['Imports - partners', 'description'],
                  'public debt': ['Public debt', 'description'], 'export partners': ['Exports - partners', 'description'],
                  'national anthem compositors': ['National anthem', ''], 'birth rate': ['Birth rate', 'description'],
                  'ethnic groups': ['Ethnic groups', 'description'], 'climate': ['Climate', 'description'],
                  'local short form': ['Country name', 'local short form'],
                  'illicit drugs': ['Illicit drugs', 'description']}


class Factbook(object):

    def __init__(self):
        self._path = os.path.join(os.path.dirname(__file__), 'countries_dump')
        self._countries_info = self._load_countries_info()

    def _load_countries_info(self):
        with open(self._path, 'rb') as countries_file:
            countries_info = pickle.load(countries_file)
        return countries_info

    def get_info_from_country(self, country, info_key):
        info_keys = INFO_KEY_ALIAS[info_key]
        info = self._countries_info.get(country)
        for info_key in info_keys:
            if isinstance(info, dict):
                info = info.get(info_key)
            else:
                break
        return info

    def get_matches(self, info_matcher):
        country_matches = set()
        for country in self._countries_info.keys():
            info_data = self.get_info_from_country(country, info_matcher.get_key())
            if info_data:
                if info_matcher.match(info_data):
                    country_matches.add(country)
        return country_matches

    def get_countries_list(self):
        return self._countries_info.keys()