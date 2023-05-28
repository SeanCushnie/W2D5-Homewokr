import unittest
from classes.drink import Drink

class TestDrink(unittest.TestCase):

    def setUp(self):
        self.drink = Drink("Coke", 2,5)

    def test_drink_has_name(self):
        self.assertEqual("Coke", self.drink.name)

    def test_drink_has_price(self):
        self.assertEqual(2.5, self.drink.price)