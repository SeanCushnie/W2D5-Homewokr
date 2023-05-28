import unittest
from classes.guest import Guest
from classes.drink import Drink

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Bob", 50, "Angels")
        self.diet_coke = Drink("Diet Coke", 2.5)
        self.full_sugar_coke = Drink("Full Sugar Coke", 500)

    def test_guest_has_name(self):
        self.assertEqual("Bob", self.guest.name)
    
    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Angels", self.guest.favourite_song)
    
    def test_reduce_wallet(self):
        self.guest.reduce_wallet(5)
        self.assertEqual(45, self.guest.wallet)

    def test_can_afford_item_sufficient_funds(self):
        self.assertEqual(True, self.guest.can_afford_item(self.diet_coke))

    def test_can_afford_item_insufficient_funds(self):
        self.assertEqual(False, self.guest.can_afford_item(self.full_sugar_coke))

    def test_buy_drink(self):
        self.guest.buy_drink(self.diet_coke)
        self.assertEqual(47.5, self.guest.wallet)
    

