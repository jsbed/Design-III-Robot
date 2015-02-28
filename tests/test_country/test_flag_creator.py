import unittest

from Robot.country.country import Country
from Robot.country.flag_creator import FlagCreator
from Robot.game_cycle.objects.color import Color


class FlagCreatorTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._country_canada = Country("Canada", [Color.NONE,
                                                 Color.NONE,
                                                 Color.NONE,
                                                 Color.RED,
                                                 Color.WHITE,
                                                 Color.RED,
                                                 Color.NONE,
                                                 Color.NONE,
                                                 Color.NONE])

    def setUp(self):
        self.flag_creator = FlagCreator(self._country_canada)

    def test_cube_order(self):
        test_cube_order = [Color.RED, Color.WHITE, Color.RED]
        self.assertEqual(test_cube_order, self.flag_creator.get_cube_order())

    def test_next_cube_for_canada(self):
        self.assertEqual(self.flag_creator.next_cube(), Color.RED)
        self.assertEqual(self.flag_creator.next_cube(), Color.WHITE)
        self.assertEqual(self.flag_creator.next_cube(), Color.RED)
        self.assertRaises(IndexError, self.flag_creator.next_cube())
