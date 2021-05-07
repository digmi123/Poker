import src.deck as d
import src.player as p
import src.card as c
from game_logic import *


def main():
    # d = d.Deck()
    p1 = p.player(3000, "Adir")
    p2 = p.player(3000, "Tomer")
    p1.add_card(c.Card(11, "Hearts"))
    p1.add_card(c.Card(13, "Clubs"))
    p2.add_card(c.Card(9, "Spades"))
    p2.add_card(c.Card(5, "Spades"))
    board = [c.Card(9, "Hearts"), c.Card(3, "Spades"), c.Card(6, "Spades"), c.Card(10, "Spades"),
             c.Card(12, "Spades")]
    print(p1)
    print(p2)
    print(f"The board is : {board}")
    winners, rank, hands = compare_hands(p1, p2, board)
    if len(winners) >= 2:
        print(f"Its a draw between {[player.name for player in winners]} , with rank : {rank} ",
              [player.name + 'hand :' + hands for player, hand in zip(winners, hands)])
    else:
        print(f"The winner is {winners[0].name} with rank : {rank.name}, {winners[0].name} hand : {hands[0]} ")

    # for _ in range(3):
    #     P.get_card(D.draw_card())
    # D.cards.sort()
    # print(D)
    # C = D.draw_card()
    # print("______________")
    # print(C.suit + C.value + ".png")
    # list1.sort()
    # print(list1[-5:])


if __name__ == '__main__':
    main()
