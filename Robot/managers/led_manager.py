class LedManager():

    '''
    - Manages the LEDs -

    String format: FXXXXXXXXXX

    First 9 'X' are for the 9 RGB flag colors
        0 : Nothing (closed)
        1 : Red
        2 : Green
        3 : Blue
        4 : Yellow
        5 : White
        6 : Black

    Last 'X' is for the 10th LED which is used to ask something
        0 : Nothing (closed)
        1 : Opened

    Working example (Canada) : F0001510000
    '''

    def __init__(self, serial_port):
        self._led_status = "F0000000000"
        self._serial_port = serial_port

    def display_country(self, country):
        self._led_status = self._format_country_to_string(country)
        self._display_new_led_status()

    def close_leds(self):
        self._led_status = "F0000000000"
        self._display_new_led_status()

    def display_red_led(self):
        self._led_status = self._led_status[:-1] + "1"
        self._display_new_led_status()

    def close_red_led(self):
        self._led_status = self._led_status[:-1] + "0"
        self._display_new_led_status()

    def display_flag_led_for_next_cube(self, cube):
        color = cube.get_color()
        position = cube.get_index()
        self._led_status = self._led_status[:position + 1] + str(color.value) + \
            self._led_status[position + 2:]
        self._display_new_led_status()

    def _display_new_led_status(self):
        self._serial_port.send_string(self._led_status)

    def _format_country_to_string(self, country):
        formated_string = "F"

        for color in country.flag:
            formated_string += str(color.value)

        formated_string += "0"

        return formated_string
