import unittest
from unittest.mock import patch

from Robot.game_cycle.objects.color import Color
from Robot.locators.segmentation.cube_segmentor_factory import create_cube_segmentor


class CubeFactoryTest(unittest.TestCase):

    @patch("Robot.locators.segmentation.cube_segmentor_factory.black_cube_segmentor.BlackCubeSegmentor")
    def test_create_black_cube_segmentor(self, SegmentatorMock):
        create_cube_segmentor(Color.BLACK)
        assert SegmentatorMock.called

    @patch("Robot.locators.segmentation.cube_segmentor_factory.red_cube_segmentor.RedCubeSegmentor")
    def test_create_red_cube_segmentor(self, SegmentatorMock):
        create_cube_segmentor(Color.RED)
        assert SegmentatorMock.called


    @patch("Robot.locators.segmentation.cube_segmentor_factory.yellow_cube_segmentor.YellowCubeSegmentor")
    def test_create_yellow_cube_segmentor(self, SegmentatorMock):
        create_cube_segmentor(Color.YELLOW)
        assert SegmentatorMock.called


    @patch("Robot.locators.segmentation.cube_segmentor_factory.green_cube_segmentor.GreenCubeSegmentor")
    def test_create_green_cube_segmentor(self, SegmentatorMock):
        create_cube_segmentor(Color.GREEN)
        assert SegmentatorMock.called


    @patch("Robot.locators.segmentation.cube_segmentor_factory.blue_cube_segmentor.BlueCubeSegmentor")
    def test_create_blue_cube_segmentor(self, SegmentatorMock):
        create_cube_segmentor(Color.BLUE)
        assert SegmentatorMock.called


    @patch("Robot.locators.segmentation.cube_segmentor_factory.white_cube_segmentor.WhiteCubeSegmentor")
    def test_create_white_cube_segmentor(self, SegmentatorMock):
        create_cube_segmentor(Color.WHITE)
        assert SegmentatorMock.called

    def test_create_exception_for_cube_without_color(self):
        self.assertRaises(Exception, create_cube_segmentor, Color.NONE)
