from PIL import Image
import csv
from goslate import Goslate
import os


GIF_DIRECTORY = "gif"

COLORS = {(250, 240, 230): "NONE",
          (255, 255, 255): "WHITE",
          (0, 0, 0): "BLACK",
          (0, 209, 0): "GREEN",
          (255, 0, 0): "RED",
          (0, 0, 255): "BLUE",
          (255, 255, 0): "YELLOW"}

SQUARE_CENTERS = [(15, 15), (45, 15), (80, 15), (15, 50), (50, 50),
                  (80, 50), (15, 80), (50, 80), (80, 80)]


def format_country_for_translation(country):
    upperLetterPositions = [index for index, character in
                            enumerate(country) if character.isupper()
                            and index > 0 and country[index-1] != "-"]

    for index, position in enumerate(upperLetterPositions):
        country = country[:position + index] + " " + country[position + index:]

    return country


if __name__ == "__main__":
    gs = Goslate()

    if (os.path.isdir(GIF_DIRECTORY)):
        with open('flags.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=';',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for filename in os.listdir(GIF_DIRECTORY):
                fig = Image.open(os.path.join(GIF_DIRECTORY, filename))
                fig_rgb = fig.convert("RGB")
                country = [os.path.splitext(filename)[0].split("_")[1]]
                formated_country = format_country_for_translation(country[0])
                translated_country = [gs.translate(formated_country, "en", "fr")]

                flag_colors = [COLORS[fig_rgb.getpixel(position)]
                               for position in SQUARE_CENTERS]

                spamwriter.writerow(country + translated_country + flag_colors)
