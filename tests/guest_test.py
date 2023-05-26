import unittest
from classes.guest import Guest

class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Bob", 50, "Angels")

    def test_guest_has_name(self):
        self.assertEqual("Bob", self.guest.name)
    
    def test_guest_has_wallet(self):
        self.assertEqual(50, self.guest.wallet)

    def test_guest_has_favourite_song(self):
        self.assertEqual("Angels", self.guest.favourite_song)
    
    def test_reduce_wallet(self):
        self.guest.reduce_wallet(5)
        self.assertEqual(45, self.guest.wallet)
    

