from unittest.mock import patch, Mock
import unittest

from Robot.communication.dtos.cube_order_dto import create_cube_order_dto
from Robot.cycle.objects.color import Color
from Robot.cycle.objects.cube import Cube
from Robot.path_finding.point import Point


@patch("Robot.communication.dtos.cube_order_dto.json")
class TestCubeOrderDto(unittest.TestCase):

    CUBE_ORDER = [Cube(Color.BLACK, Point(1, 1)),
                  Cube(Color.RED, Point(2, 2))]
    EXPECTED_CUBE_ORDER_DTO = {"cubes": [{"cube position": [1, 1],
                                          "cube color": 6},
                                         {"cube position": [2, 2],
                                          "cube color": 1}]}

    def test_create_cube_order_dto_with_cube_order(self, json_mock):
        json_mock.dumps = Mock()

        create_cube_order_dto(self.CUBE_ORDER)

        json_mock.dumps.assert_called_with(self.EXPECTED_CUBE_ORDER_DTO)
