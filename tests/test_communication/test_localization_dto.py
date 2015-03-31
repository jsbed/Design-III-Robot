from unittest.mock import patch, Mock
import unittest

from Robot.communication.localization.localization_dto import create_localization_dto,\
    create_localization_from_localization_dto
from Robot.locators.localization import Localization
from Robot.path_finding.point import Point


@patch("Robot.communication.localization.localization_dto.json")
class TestLocalizationDto(unittest.TestCase):

    UNKNOWN_LOCALIZATION = Localization(None, None, unknown=True)
    KNOWN_LOCALIZATION = Localization(Point(1, 1), 90)
    UNKNOWN_LOCALIZATION_DTO = {"unknown": True,
                                "orientation": 0,
                                "position": (0, 0)}
    KNOWN_LOCALIZATION_DTO = {"unknown": False,
                              "orientation": 90,
                              "position": (1, 1)}

    def test_create_localization_dto_with_unknown_localization(self, json_mock):
        json_mock.dumps = Mock()

        create_localization_dto(self.UNKNOWN_LOCALIZATION)

        json_mock.dumps.assert_called_with(
            self.UNKNOWN_LOCALIZATION_DTO, "utf-8")

    def test_create_localization_dto_with_known_localization(self, json_mock):
        json_mock.dumps = Mock()

        create_localization_dto(self.KNOWN_LOCALIZATION)

        json_mock.dumps.assert_called_with(
            self.KNOWN_LOCALIZATION_DTO, "utf-8")

    def test_create_localization_from_localization_dto_with_unknown_localization_dto(self, json_mock):
        json_mock.loads = Mock(return_value=self.UNKNOWN_LOCALIZATION_DTO)

        actual_localization = create_localization_from_localization_dto(
            self.UNKNOWN_LOCALIZATION_DTO)

        self._assert_localization(actual_localization,
                                  self.UNKNOWN_LOCALIZATION)

    def test_create_localization_from_localization_dto_with_known_localization_dto(self, json_mock):
        json_mock.loads = Mock(return_value=self.KNOWN_LOCALIZATION_DTO)

        actual_localization = create_localization_from_localization_dto(
            self.KNOWN_LOCALIZATION_DTO)

        self._assert_localization(actual_localization,
                                  self.KNOWN_LOCALIZATION)

    def _assert_localization(self, actual_localization, expected_localization):
        self.assertEqual(actual_localization.position,
                         expected_localization.position)
        self.assertEqual(actual_localization.orientation,
                         expected_localization.orientation)
        self.assertEqual(actual_localization.unknown,
                         expected_localization.unknown)
