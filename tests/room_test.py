import unittest
from classes.room import Room
from classes.guest import Guest
from classes.song import Song

class TestRoom(unittest.TestCase):
    def setUp(self):
        self.guest1 = Guest("Michael", 120, "Iron Man")
        self.guest2 = Guest("Barry", 60, "Spanish Flea")
        self.guest3 = Guest("Peter", 30, "Waltz Across Texas")
        self.guest4 = Guest("Charlie", 30, "The Wanderer")
        self.guest5 = Guest("Manfred", 15, "Through the Fire and Flames")
        guestList = [self.guest1, self.guest2, self.guest3]
        self.room = Room("One", 10, 5, guestList)
        self.room2 = Room("Two", 10, 2, ["Boaby", "Jane", "Derik"])
        self.room.playList = ["Through the Fire and Flames", "Iron Man", "Jolene", "Waltz Across Texas"]
        self.new_guest = Guest("Rachel", 20, "Sweet Caroline")
        # self.new_song = Song("Iron Man")

    def test_room_has_name(self):
        self.assertEqual("One", self.room.name)
    
    def test_room_has_fee(self):
        self.assertEqual(10, self.room.fee)
    
    def test_room_has_capacity(self):
        self.assertEqual(5, self.room.room_capacity)
    
    def test_room_has_guest_list(self):
        self.assertEqual(3, len(self.room.guestList))

    def test_room_has_playlist(self):
       self.assertEqual(4, len(self.room.playList))

    def test_add_guest_success(self):
        self.room.add_guest(self.new_guest)
        self.assertEqual(4, len(self.room.guestList))

    def test_add_guest_failure(self):
        guestList = [self.guest1, self.guest2, self.guest3, self.guest4, self.guest5]
        self.assertEqual(None, self.room.add_guest(self.new_guest))

    def test_add_song_to_playlist(self):
        self.room.add_song_to_playlist("Dancing in the Dark", self.guest1)
        self.assertIn("Dancing in the Dark", self.room.playList)

    def test_check_if_favourite_song_in_playlist(self):
        self.assertEqual(self.room.check_if_favourite_song(Song("Iron Man")), "Woohoo")

    def test_check_add_room(self):
        self.assertEqual("Two", self.room2.name)