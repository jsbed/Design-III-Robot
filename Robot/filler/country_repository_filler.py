import csv

from Robot.country.country_repository import CountryRepository
from Robot.game_cycle.objects.color import Color


def fill_repository_from_file(file_path):

    with open(file_path, newline='') as csvfile:
        country_dictionary = {}
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')

        for country_data in spamreader:
            country_name = country_data[1].replace(";", ",")
            flag_colors = [Color[color] for color in country_data[2:]]
            country_dictionary[country_name] = flag_colors

        CountryRepository().store(country_dictionary)
