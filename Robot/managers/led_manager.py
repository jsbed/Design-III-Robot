import serial

'''
    - Manages the LEDs -

    String format: FXXXXXXXXXX

    First 9 'X' represents the 9 RGB colors for a flag
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


class LedManager():

    def __init__(self, serial_port):
        self._serial_port = serial.Serial(serial_port)

    def display_country(self, cube):
        pass  # ser.write("F0001510000".encode()) -> for Canada
