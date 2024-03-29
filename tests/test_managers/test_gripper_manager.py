from unittest.mock import MagicMock, Mock, patch, call
import unittest


from Robot.managers.gripper_manager import GripperManager

TAKE_CUBE_VALUES = [0, 1, 2, 3, 1]
TAKE_CUBE_SENT_VALUES = [0, 1, 2, 3]
TAKE_CUBE_ADJUSTMENT_VALUES = [0, 1, 2, 4]
RELEASE_CUBE_VALUES = [1, 2, 3, 4, -2]
RELEASE_CUBE_SENT_VALUES = [1, 2, 3, 4]
RELEASE_CUBE_ADJUSTMENT_VALUES = [1, 2, 3, 2]
LIFT_GRIPPER_VALUES = [2, 3, 4, 5, 6]
LIFT_GRIPPER_SENT_VALUES = [2, 3, 4, 5]
LIFT_GRIPPER_ADJUSTMENT_VALUES = [2, 3, 4, 11]
LOWER_GRIPPER_VALUES = [3, 4, 5, 6, -5]
LOWER_GRIPPER_SENT_VALUES = [3, 4, 5, 6]
LOWER_GRIPPER_ADJUSTMENT_VALUES = [3, 4, 5, 1]
WIDEST_GRIPPER_VALUES = [4, 5, 6, 7, 0]
WIDEST_GRIPPER_SENT_VALUES = [4, 5, 6, 7]


@patch("time.sleep")
@patch("Robot.configuration.config.Config")
class GripperManagerTest(unittest.TestCase):

    def setUp(self):
        self.serial_mock = self.create_serial_mock()
        self.gripper_manager = GripperManager(self.serial_mock)

    def create_serial_mock(self):
        serial_mock = MagicMock()
        serial_mock.send_array_of_ints = Mock()
        return serial_mock

    def test_when_take_cube_should_call_serial_with_config_take_cube_values_with_its_adjustment(self, config_mock, time_mock):
        custom_config_mock = MagicMock()
        custom_config_mock.get_take_cube_gripper_values = Mock(
            return_value=TAKE_CUBE_VALUES)
        config_mock.return_value = custom_config_mock

        self.gripper_manager.take_cube()

        calls = [call.send_array_of_ints(TAKE_CUBE_SENT_VALUES),
                 call.send_array_of_ints(TAKE_CUBE_ADJUSTMENT_VALUES)]

        self.serial_mock.send_array_of_ints.assert_has_calls(calls)

    def test_when_release_cube_should_call_serial_with_config_release_cube_values_with_its_adjustment(self, config_mock, time_mock):
        custom_config_mock = MagicMock()
        custom_config_mock.get_release_cube_gripper_values = Mock(
            return_value=RELEASE_CUBE_VALUES)
        config_mock.return_value = custom_config_mock

        self.gripper_manager.release_cube()

        calls = [call.send_array_of_ints(RELEASE_CUBE_SENT_VALUES),
                 call.send_array_of_ints(RELEASE_CUBE_ADJUSTMENT_VALUES)]

        self.serial_mock.send_array_of_ints.assert_has_calls(calls)

    def test_when_lift_gripper_should_call_serial_with_config_lift_gripper_values_with_its_adjustment(self, config_mock, time_mock):
        custom_config_mock = MagicMock()
        custom_config_mock.get_lift_gripper_values = Mock(
            return_value=LIFT_GRIPPER_VALUES)
        config_mock.return_value = custom_config_mock

        self.gripper_manager.lift_gripper()

        calls = [call.send_array_of_ints(LIFT_GRIPPER_SENT_VALUES),
                 call.send_array_of_ints(LIFT_GRIPPER_ADJUSTMENT_VALUES)]

        self.serial_mock.send_array_of_ints.assert_has_calls(calls)

    def test_when_lower_gripper_should_call_serial_with_config_lower_gripper_values_with_its_adjustment(self, config_mock, time_mock):
        custom_config_mock = MagicMock()
        custom_config_mock.get_lower_gripper_values = Mock(
            return_value=LOWER_GRIPPER_VALUES)
        config_mock.return_value = custom_config_mock

        self.gripper_manager.lower_gripper()

        calls = [call.send_array_of_ints(LOWER_GRIPPER_SENT_VALUES),
                 call.send_array_of_ints(LOWER_GRIPPER_ADJUSTMENT_VALUES)]

        self.serial_mock.send_array_of_ints.assert_has_calls(calls)

    def test_when_widest_gripper_should_call_serial_with_config_widest_gripper_values_with_its_adjustment(self, config_mock, time_mock):
        custom_config_mock = MagicMock()
        custom_config_mock.get_widest_gripper_values = Mock(
            return_value=WIDEST_GRIPPER_VALUES)
        config_mock.return_value = custom_config_mock

        self.gripper_manager.widest_gripper()

        self.serial_mock.send_array_of_ints.assert_called_once_with(
            WIDEST_GRIPPER_SENT_VALUES)
