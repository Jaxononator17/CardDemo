import unittest
from deck import Deck
from playing_card import PlayingCard

class TestDeck(unittest.TestCase):
    
    def test_generate_full_deck(self):
        deck = Deck()
        self.assertEqual(len(deck.cards), 52)

    def test_shuffle(self):
        deck = Deck()
        original_deck = deck.cards.copy()
        deck.shuffle()
        self.assertNotEqual(deck.cards, original_deck)
    
    def test_draw_card(self):
        deck = Deck()
        card = deck.draw_card()
        self.assertIsInstance(card, PlayingCard)
        self.assertEqual(len(deck.cards), 51)
    
    def test_draw_card_empty_deck(self):
        deck = Deck()
        while deck.cards:
            deck.draw_card()
        card = deck.draw_card()
        self.assertIsNone(card)

if __name__ == "__main__":
    unittest.main()
