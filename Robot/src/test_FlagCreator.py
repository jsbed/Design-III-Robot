import unittest
from FlagCreator import FlagCreator
from Color import Color


class FlagCreatorTest(unittest.TestCase):
    def test_cube_order(self):
        test_cube_order = [Color.GREEN, Color.RED, Color.WHITE]
        test_FlagCreator = FlagCreator("Algerie")
        self.assertEqual(test_cube_order, test_FlagCreator._cube_order)

    def test_country_name_match(self):
        test_country_name = "Canada"
        test_FlagCreator = FlagCreator("Canada")
        self.assertEqual(test_country_name, test_FlagCreator._country.name)

    def test_flag_width(self):
        test_creation_zone_width = 2
        test_FlagCreator = FlagCreator("Bahamas")
        self.assertEqual(test_FlagCreator._creation_zone_width,
                         test_creation_zone_width)

    def test_flag_height(self):
        test_creation_zone_height = 3
        test_FlagCreator = FlagCreator("Bahamas")
        self.assertEqual(test_FlagCreator._creation_zone_height,
                         test_creation_zone_height)

    def test_next_cube(self):
        test_FlagCreator = FlagCreator("Cameroun")
        self.assertEqual(test_FlagCreator.next_cube(), Color.YELLOW)

    def test_cube_list_empty_exception(self):
        test_FlagCreator = FlagCreator("Canada")
        test_FlagCreator._cube_order.clear()
        self.assertRaises(IndexError, test_FlagCreator.next_cube())
