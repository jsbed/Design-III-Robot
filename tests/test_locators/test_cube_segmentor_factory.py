from unittest.mock import patch
import unittest

from Robot.game_cycle.objects.color import Color
from Robot.locators.segmentation.cube_segmentor_factory import create_cube_segmentor


class TestCubeFactory(unittest.TestCase):

    @patch("Robot.locators.segmentation.cube_segmentor_factory.red_cube_segmentor.RedCubeSegmentor")
    def test_create_red_cube_segmentor(self, SegmentatorMock):
        create_cube_segmentor(Color.RED)
        assert SegmentatorMock.called

    @patch("Robot.locators.segmentation.cube_segmentor_factory.cube_segmentation.CubeSegmentor")
    def test_create_yellow_cube_segmentor(self, SegmentatorMock):
        create_cube_segmentor(Color.YELLOW)
        assert SegmentatorMock.called

    @patch("Robot.locators.segmentation.cube_segmentor_factory.cube_segmentation.CubeSegmentor")
    def test_create_green_cube_segmentor(self, SegmentatorMock):
        create_cube_segmentor(Color.GREEN)
        assert SegmentatorMock.called

    @patch("Robot.locators.segmentation.cube_segmentor_factory.cube_segmentation.CubeSegmentor")
    def test_create_blue_cube_segmentor(self, SegmentatorMock):
        create_cube_segmentor(Color.BLUE)
        assert SegmentatorMock.called

    def test_create_exception_for_white_cube(self):
        self.assertRaises(Exception, create_cube_segmentor, Color.WHITE)

    def test_create_exception_for_black_cube(self):
        self.assertRaises(Exception, create_cube_segmentor, Color.BLACK)

    def test_create_exception_for_cube_without_color(self):
        self.assertRaises(Exception, create_cube_segmentor, Color.NONE)
