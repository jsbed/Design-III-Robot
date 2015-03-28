import serial


class SerialPort():

    def __init__(self, serial_port, baudrate=9600, timeout=0):
        self._serial = serial.Serial(serial_port, baudrate=baudrate,
                                     timeout=timeout)

    def send_string(self, data):
        self._serial.write(data.encode())

    def send_array_of_ints(self, array):
        self._serial.write(bytearray(array))

    def wait_for_read_line(self):
        while not self._serial.readline():
            pass
