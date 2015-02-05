import csv
import os

from PIL import Image


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

if __name__ == "__main__":

    if (os.path.isdir(GIF_DIRECTORY)):
        with open('flags.csv', 'w', newline='') as csvfile:
            spamwriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            for filename in os.listdir(GIF_DIRECTORY):
                fig = Image.open(os.path.join(GIF_DIRECTORY, filename))
                fig_rgb = fig.convert("RGB")
                country = [os.path.splitext(filename)[0].split("_")[1]]
                flag_colors = [COLORS[fig_rgb.getpixel(position)]
                               for position in SQUARE_CENTERS]

                spamwriter.writerow(country + flag_colors)
