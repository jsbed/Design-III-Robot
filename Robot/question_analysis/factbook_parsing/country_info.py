import pickle
import os


INFO_KEY_ALIAS = {'capital': ['Capital', 'name']}


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
            if info:
                info = info.get(info_key)
            else:
                break
        return info

    def get_matches(self, answer_matcher):
        """
        :param info: tuple containing info name and regex matching the wanted info
        :return:
        """
        country_matches = set()
        for country in self._countries_info.keys():
            info_data = self.get_info_from_country(country, answer_matcher.get_key())  # info[0] -> answer_matcher.key_name
            if info_data:
                match = answer_matcher.match(info_data)  # answer_matcher.match
                if match:
                    country_matches.add(country)
        return country_matches