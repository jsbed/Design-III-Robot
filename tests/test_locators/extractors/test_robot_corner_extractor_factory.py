from unittest.mock import patch
import unittest

from Robot.cycle.objects.color import Color
from Robot.locators.extractors.robot_corner.robot_corner_extractor_factory import create_robot_corner_extractor


class TestCubeExtractor(unittest.TestCase):

    @patch("Robot.locators.extractors.robot_corner.pink_robot_corner_extractor.PinkRobotCornerExtractor")
    def test_create_pink_robot_corner_extractor(self, SegmentatorMock):
        create_robot_corner_extractor(Color.PINK)
        assert SegmentatorMock.called

    @patch("Robot.locators.extractors.robot_corner.blue_robot_corner_extractor.BlueRobotCornerExtractor")
    def test_create_blue_robot_corner_extractor(self, SegmentatorMock):
        create_robot_corner_extractor(Color.BLUE)
        assert SegmentatorMock.called

    @patch("Robot.locators.extractors.robot_corner.orange_robot_corner_extractor.OrangeRobotCornerExtractor")
    def test_create_orange_robot_corner_extractor(self, SegmentatorMock):
        create_robot_corner_extractor(Color.ORANGE)
        assert SegmentatorMock.called

    def test_create_exception_for_robot_corner_without_color(self):
        self.assertRaises(Exception, create_robot_corner_extractor,
                          Color.NONE)

    def test_create_exception_for_red_robot_corner(self):
        self.assertRaises(Exception, create_robot_corner_extractor,
                          Color.RED)

    def test_create_exception_for_green_robot_corner(self):
        self.assertRaises(Exception, create_robot_corner_extractor,
                          Color.GREEN)

    def test_create_exception_for_yellow_robot_corner(self):
        self.assertRaises(Exception, create_robot_corner_extractor,
                          Color.YELLOW)

    def test_create_exception_for_white_robot_corner(self):
        self.assertRaises(Exception, create_robot_corner_extractor,
                          Color.WHITE)

    def test_create_exception_for_black_robot_corner(self):
        self.assertRaises(Exception, create_robot_corner_extractor,
                          Color.BLACK)
