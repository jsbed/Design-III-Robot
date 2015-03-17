class Leds():

    def __init__(self, ui, tcp_client):
        self._ui = ui
        self._tcp_client = tcp_client
        self._setup_ui()

    def _setup_ui(self):
        self._ui.display_country_button.clicked.connect(self._display_country)
        self._ui.update_square_button.clicked.connect(self._update_square)
        self._ui.open_red_led_button.clicked.connect(self._open_red_led)
        self._ui.close_red_led_button.clicked.connect(self._close_red_led)
        self._ui.close_all_leds_button.clicked.connect(self._close_all_leds)

    def _display_country(self):
        country = self._ui.led_country_line_edit.text()

        if country and ":" not in country:
            self._tcp_client.send_data("display led country:" + country)

    def _update_square(self):
        self._tcp_client.send_data("update led square:{}:{}".format(
            self._ui.square_color_combo_box.currentText(),
            self._ui.square_number_combo_box.currentText()))

    def _open_red_led(self):
        self._tcp_client.send_data("open red led")

    def _close_red_led(self):
        self._tcp_client.send_data("close red led")

    def _close_all_leds(self):
        self._tcp_client.send_data("close all leds")
