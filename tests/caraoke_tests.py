import unittest
from classes.caraoke import Caraoke
from classes.guest import Guest
from classes.drink import Drink

class TestCaraoke(unittest.TestCase):
    def setUp(self):
        self.bob = Guest("Bob", 50, "Angels")
        self.guest1 = Guest("Michael", 120, "Iron Man")
        self.guest2 = Guest("Barry", 60, "Spanish Flea")
        self.guest3 = Guest("Peter", 30, "Waltz Across Texas")
        guestList = [self.guest1, self.guest2, self.guest3]
        self.venue = Caraoke("Karaoed Away", 100)

        self.diet_coke = Drink("Diet_Coke", 2.5)
        self.full_sugar_coke = Drink("Full_Sugar_Coke", 5000)

    def test_till_has_value(self):
        self.assertEqual(100, self.venue.till)

    def test_sell_drink_sufficient_funds(self):
        self.venue.sell_drink(self.bob, self.diet_coke)
        self.assertEqual(102.5, self.venue.till)
    
    def test_sell_drink_insufficient_funds(self):
        self.assertEqual(False, self.venue.sell_drink(self.bob, self.full_sugar_coke))

