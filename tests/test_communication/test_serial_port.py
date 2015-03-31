from unittest.mock import patch, MagicMock, Mock
import unittest

from Robot.communication.serial_port import SerialPort


DATA = "simpletext"
ARRAY = [0, 1, 2, 3]
ENCODED_DATA = DATA.encode()
ENCODED_ARRAY = bytearray(ARRAY)


class SerialPortTest(unittest.TestCase):

    @patch("serial.Serial")
    def setUp(self, serial_mock):
        self._serial_port_mock = self._create_serial_port_mock()
        serial_mock.return_value = self._serial_port_mock
        self._serial_port = SerialPort(None)

    def _create_serial_port_mock(self):
        serial_mock = MagicMock()
        serial_mock.write = Mock()
        serial_mock.readline = Mock()

        return serial_mock

    def test_when_send_string_with_data_should_call_write_with_encoded_data(self):
        self._serial_port.send_string(DATA)

        self._serial_port_mock.write.assert_called_with(ENCODED_DATA)

    def test_when_send_array_of_ints_with_array_should_call_write_with_encoded_array(self):
        self._serial_port.send_array_of_ints(ARRAY)

        self._serial_port_mock.write.assert_called_with(ENCODED_ARRAY)

    def test_when_wait_for_read_line_with_readline_returning_something_on_third_call_should_call_readline_three_times(self):
        self._serial_port_mock.readline.side_effect = [b"", b"", b"data"]

        self._serial_port.wait_for_read_line()

        self.assertEqual(self._serial_port_mock.readline.call_count, 3)
