import unittest
from hand import Hand
from playing_card import PlayingCard

class TestHand(unittest.TestCase):

    def test_add_card(self):
        hand = Hand()
        card = PlayingCard("A", "Hearts")
        hand.add_card(card)
        self.assertEqual(len(hand.cards), 1)
    
    def test_display_hand(self):
        hand = Hand()
        card1 = PlayingCard("A", "Hearts")
        card2 = PlayingCard("10", "Diamonds")
        hand.add_card(card1)
        hand.add_card(card2)
        self.assertEqual(hand.display_hand(), ["A of Hearts", "10 of Diamonds"])
    
    def test_number_of_cards(self):
        hand = Hand()
        card = PlayingCard("A", "Hearts")
        hand.add_card(card)
        self.assertEqual(hand.number_of_cards(), 1)

if __name__ == "__main__":
    unittest.main()
