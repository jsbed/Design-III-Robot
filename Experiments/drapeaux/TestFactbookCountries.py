import csv

from Robot.question_analysis.factbook_parsing.country_info import Factbook


countries = Factbook().get_countries_list()

with open("flags.csv", newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    all_found = True

    for country_data in spamreader:
        country_name = country_data[0]
        translated_country_name = country_data[1].replace(";", ",")

        if (translated_country_name not in countries):
            print("Not Found ->", country_name, translated_country_name)
            all_found = False

    if (all_found):
        print("Each country has been found !")
