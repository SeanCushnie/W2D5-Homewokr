from classes.guest import *
from classes.room import *

class Caraoke:
    def __init__(self, name, cash):
        self.name = name
        self.till = cash

    def increase_till(self, amount):
        self.till += amount

    def sell_drink(self, guest, drink):
        if guest.can_afford_item(drink):
            self.increase_till(drink.price)
            guest.buy_drink(drink)
        else:
            return False