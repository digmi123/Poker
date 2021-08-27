import src.deck as d
import src.player as p
import src.card as c
from game_logic import *
import table


def round(players):
    deck = d.Deck()
    for player in players:
        for _ in range(2):
            player.add_card(deck.draw_card())
    board = [deck.draw_card() for _ in range(5)]
    for player in players:
        print(player, "\n")
    winners = who_wins(players, board)
    print(f"The board is : {board}")
    if len(winners) >= 2:
        print(f"Its a draw between {[player.name for player in winners]} , with rank : {winners[0].player_rank} ",
              [winner.player.name + 'hand :' + winner.player_hand for winner in winners])
    else:
        print(
            f"The winner is {winners[0].player.name} with rank : {winners[0].player_rank.name}, {winners[0].player.name} hand : {winners[0].player_hand} ")
    for player in players:
        player.throw_cards()


def main():
    players = [p.player(0, "Adir"),
               p.player(0, "Tomer"),
               p.player(0, "Idan"),
               p.player(0, "Safi")]

    players[0].total_bet_per_round = 30
    players[1].total_bet_per_round = 50
    players[2].total_bet_per_round = 100
    players[3].total_bet_per_round = 100

    t = table.table()

    # p1 = p.player(3000, "Adir")
    # p2 = p.player(3000, "Daniel")
    players[0].add_card(c.Card(2, "Hearts"))
    players[0].add_card(c.Card(2, "Hearts"))
    players[1].add_card(c.Card(2, "Hearts"))
    players[1].add_card(c.Card(14, "Hearts"))
    players[2].add_card(c.Card(12, "Hearts"))
    players[2].add_card(c.Card(6, "Hearts"))
    players[3].add_card(c.Card(11, "Hearts"))
    players[3].add_card(c.Card(4, "Hearts"))
    t.players = players
    t.board = [c.Card(2, "Spades"), c.Card(14, "Diamonds"), c.Card(13, "Hearts"), c.Card(12, "Diamonds"), c.Card(11, "Clubs")]
    # winners, rank, hands = compare_hands(p1, p2, board)
    # print(f"The winner is {winners[0].name} with rank : {rank.name}, {winners[0].name} hand : {hands[0]} ")
    t.split_jackpot()
    for player in players:
        print(player)

if __name__ == '__main__':
    main()
