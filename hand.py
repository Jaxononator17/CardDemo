import random
from playing_card import PlayingCard

class Hand:
    def __init__(self):
        self.cards = []
    
    def add_card(self, card):
        self.cards.append(card)
    
    def display_hand(self):
        return [str(card) for card in self.cards]
    
    def number_of_cards(self):
        return len(self.cards)
