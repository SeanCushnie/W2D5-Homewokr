from classes.guest import *
from classes.song import *
from classes.guest import *
from classes.caraoke import *
class Room:
    def __init__(self, name, fee, capacity, guestList):
        self.name = name
        self.fee = fee
        self.room_capacity = capacity
        self.guestList = guestList
        self.playList = []

    def add_guest(self, guest):
        if len(self.guestList) < self.room_capacity:
            self.guestList.append(guest)
            guest.reduce_wallet(self.fee)
        else:
            return None 
    def remove_guest(self, guest):
        if guest in self.guestList:
            self.guestList.remove(guest)
    #Jukebox function. Guest can add a song for £10
    def add_song_to_playlist(self, song, guest):
        amount = 10
        self.playList.append(song)
        guest.reduce_wallet(amount)
    
    def check_if_favourite_song(self, song):
        for guest in self.guestList:
            if guest.favourite_song == song.name:
                return "Woohoo"
        return None
    
    
    