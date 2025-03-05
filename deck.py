import random
from playing_card import PlayingCard

class Deck:
    def __init__(self):
        self.cards = self.generate_full_deck()
    
    def generate_full_deck(self):
        return [PlayingCard(rank, suit) for suit in PlayingCard.SUITS for rank in PlayingCard.RANKS]
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw_card(self):
        return self.cards.pop() if self.cards else None
