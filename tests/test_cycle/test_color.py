import unittest

from Robot.cycle.objects.color import Color


class TestColor(unittest.TestCase):

    def test_is_red_segmentable_should_be_true(self):
        segmentable = Color.is_segmentable(Color.RED)

        self.assertTrue(segmentable)

    def test_is_green_segmentable_should_be_true(self):
        segmentable = Color.is_segmentable(Color.GREEN)

        self.assertTrue(segmentable)

    def test_is_blue_segmentable_should_be_true(self):
        segmentable = Color.is_segmentable(Color.BLUE)

        self.assertTrue(segmentable)

    def test_is_yellow_segmentable_should_be_true(self):
        segmentable = Color.is_segmentable(Color.YELLOW)

        self.assertTrue(segmentable)

    def test_is_pink_segmentable_should_be_true(self):
        segmentable = Color.is_segmentable(Color.PINK)

        self.assertTrue(segmentable)

    def test_is_orange_segmentable_should_be_true(self):
        segmentable = Color.is_segmentable(Color.ORANGE)

        self.assertTrue(segmentable)

    def test_is_white_segmentable_should_be_false(self):
        segmentable = Color.is_segmentable(Color.WHITE)

        self.assertFalse(segmentable)

    def test_is_black_segmentable_should_be_false(self):
        segmentable = Color.is_segmentable(Color.BLACK)

        self.assertFalse(segmentable)

    def test_is_none_segmentable_should_be_false(self):
        segmentable = Color.is_segmentable(Color.NONE)

        self.assertFalse(segmentable)
