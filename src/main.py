import src.deck as d
import src.player as p
import src.card as c
from game_logic import *


def main():

    #d = d.Deck()
    p1 = p.player(3000,"Adir")
    p2 = p.player(3000, "Tomer")
    p1.add_card(c.Card(9, "Clubs"))
    p1.add_card(c.Card(3, "Clubs"))
    p2.add_card(c.Card(8, "Diamonds"))
    p2.add_card(c.Card(9, "Clubs"))
    board = [c.Card(10, "Clubs"), c.Card(11, "Clubs"), c.Card(12, "Clubs"), c.Card(14, "Diamonds"), c.Card(5, "Hearts")]
    print(p1)
    print(p2)
    print(f"The board is : {board}")
    compare_hands(p1, p2, board)

    # for _ in range(3):
    #     P.get_card(D.draw_card())
    #D.cards.sort()
    #print(D)
    # C = D.draw_card()
    # print("______________")
    # print(C.suit + C.value + ".png")
    #list1.sort()
    #print(list1[-5:])


if __name__ == '__main__':
    main()
