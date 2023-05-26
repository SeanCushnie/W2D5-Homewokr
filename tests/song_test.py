import unittest
from classes.song import Song
from classes.room import Room



class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Iron Man")

    def test_song_has_name(self):
        self.assertEqual("Iron Man", self.song.name)