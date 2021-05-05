class player:
    def __init__(self, balance, name):
        self.name = name
        self.state = True
        self.hand = []
        self.balance = balance

    def add_card(self, card):
        self.hand.append(card)

    def bet(self, bet_amount):
        if self.balance >= bet_amount:
            self.balance -= bet_amount
            return True
        return False

    def throw_cards(self):
        self.hand = []

    def __repr__(self):
        return f" Name :  {self.name} \n hand : {self.hand} \n balance:{self.balance}"
