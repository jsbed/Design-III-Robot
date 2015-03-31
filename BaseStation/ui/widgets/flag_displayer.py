from Robot.country.country_repository import CountryRepository
from Robot.cycle.objects.color import Color

COLOR_LABELS = {Color.BLUE: ":resources/blue_flag.png",
                Color.GREEN: ":resources/green_flag.png",
                Color.RED: ":resources/red_flag.png",
                Color.YELLOW: ":resources/yellow_flag.png",
                Color.WHITE: ":resources/white_flag.png",
                Color.BLACK: ":resources/black_flag.png",
                Color.NONE: ":resources/transparency.png"}


class FlagDisplayer():

    def __init__(self, widget):
        self._widget = widget
        self._flag_labels = [self._widget.square_0_label,
                             self._widget.square_1_label,
                             self._widget.square_2_label,
                             self._widget.square_3_label,
                             self._widget.square_4_label,
                             self._widget.square_5_label,
                             self._widget.square_6_label,
                             self._widget.square_7_label,
                             self._widget.square_8_label]

        for label in self._flag_labels:
            label.setPixmap(COLOR_LABELS[Color.NONE])

    def display_country(self, country_name):
        country = CountryRepository().get(country_name)

        for index, label in enumerate(self._flag_labels):
            label.setPixmap(COLOR_LABELS[country.flag[index]])

        self._widget.countryLabel.setText(country_name)
        self._widget.flag_structure_label.raise_()

    def remove_country(self):
        self._widget.countryLabel.setText("-")

        for label in self._flag_labels:
            label.setPixmap(COLOR_LABELS[Color.NONE])
