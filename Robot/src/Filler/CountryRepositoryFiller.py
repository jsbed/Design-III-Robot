import csv

from Color import Color
from Country.CountryRepository import CountryRepository


class CountryRepositoryFiller:

    def fill_repository_from_file(self, file_path):

        with open(file_path, newline='') as csvfile:
            country_dictionary = {}
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

            for country_data in spamreader:
                country_name = country_data[0]
                flag_colors = [Color[color] for color in country_data[1:]]
                country_dictionary[country_name] = flag_colors

            CountryRepository().store(country_dictionary)
