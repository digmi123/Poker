
class Card:
    def __init__(self, card_value, suit_type):
        self.card_value = card_value
        self.suit_type = suit_type

    def __repr__(self):
        dict_color = {"Hearts": "\033[0:31m", "Spades": "\033[0:30m", "Clubs": "\033[0:30m", "Diamonds": "\033[0:31m"}
        dict_suit = {"Hearts": "♥", "Spades": "♠", "Clubs": "♣", "Diamonds": "♦"}
        dict_value = {2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: '10', 11: 'j', 12: 'Q',
                      13: 'K',
                      14: 'A'}
        return dict_color[self.suit_type] + dict_value[self.card_value] + dict_suit[self.suit_type]+"\033[0:20m"

    def __lt__(self, other):
        return self.card_value < other.card_value

