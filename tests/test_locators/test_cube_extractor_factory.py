from unittest.mock import patch
import unittest

from Robot.cycle.objects.color import Color
from Robot.locators.extractors.cube_extractor_factory import create_cube_extractor


class TestCubeExtractor(unittest.TestCase):

    @patch("Robot.locators.extractors.cube_extractor_factory.black_cube_extractor.BlackCubeExtractor")
    def test_create_black_cube_extractor(self, SegmentatorMock):
        create_cube_extractor(Color.BLACK)
        assert SegmentatorMock.called

    @patch("Robot.locators.extractors.cube_extractor_factory.red_cube_extractor.RedCubeExtractor")
    def test_create_red_cube_extractor(self, SegmentatorMock):
        create_cube_extractor(Color.RED)
        assert SegmentatorMock.called

    @patch("Robot.locators.extractors.cube_extractor_factory.yellow_cube_extractor.YellowCubeExtractor")
    def test_create_yellow_cube_extractor(self, SegmentatorMock):
        create_cube_extractor(Color.YELLOW)
        assert SegmentatorMock.called

    @patch("Robot.locators.extractors.cube_extractor_factory.green_cube_extractor.GreenCubeExtractor")
    def test_create_green_cube_extractor(self, SegmentatorMock):
        create_cube_extractor(Color.GREEN)
        assert SegmentatorMock.called

    @patch("Robot.locators.extractors.cube_extractor_factory.blue_cube_extractor.BlueCubeExtractor")
    def test_create_blue_cube_extractor(self, SegmentatorMock):
        create_cube_extractor(Color.BLUE)
        assert SegmentatorMock.called

    @patch("Robot.locators.extractors.cube_extractor_factory.white_cube_extractor.WhiteCubeExtractor")
    def test_create_white_cube_segmentor(self, SegmentatorMock):
        create_cube_extractor(Color.WHITE)
        assert SegmentatorMock.called

    def test_create_exception_for_cube_without_color(self):
        self.assertRaises(Exception, create_cube_extractor, Color.NONE)

    def test_create_exception_for_pink_cube(self):
        self.assertRaises(Exception, create_cube_extractor, Color.PINK)
