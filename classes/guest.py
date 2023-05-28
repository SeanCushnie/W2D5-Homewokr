from classes.drink import *
from classes.room import *

class Guest:
    def __init__(self, name, wallet, favourite_song):
        self.name = name
        self.wallet = wallet
        self.favourite_song = favourite_song
        
    def reduce_wallet(self, amount):
        self.wallet -= amount


    def can_afford_item(self, item):
        return True if self.wallet >= item.price else False
    
    def buy_drink(self,drink):
        self.reduce_wallet(drink.price)
