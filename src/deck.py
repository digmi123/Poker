from random import randint
import src.card as c


class Deck:
    def __init__(self):
        self.cards = []
        for suit in ["Hearts", "Spades", "Clubs", "Diamonds"]:
            for value in range(2, 15):
                self.cards.append(c.Card(value, suit))
        self.shuffle_deck()

    def shuffle_deck(self):
        for i in range(len(self.cards)):
            r = randint(0, len(self.cards) - 1)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def __repr__(self):
        for card in self.cards:
            print(card)
        return ""

    def draw_card(self):
        return self.cards.pop()
