from src.deck import Deck
from src.player import player
from src.game_logic import *


def get_move(player):
    print(player.name)
    return input()


class table:
    def __init__(self):
        self.pot = {"money": [], "players": []}
        self.waiting_list = []
        self.players = []
        self.board = []
        self.deck = None

    def actions(self):
        num_players = len(self.players)
        i = 0
        last_player = num_players - 1
        while True:
            if self.players[i].state:
                player_action = get_move(self.players[i])
                if player_action.startswith("Raise"):
                    player_action_string = player_action.split()
                    if int(player_action_string[1]) < self.players[i].balance:
                        self.players[i].balance -= int(player_action_string[1])
                        self.players[i].total_bet_per_round += int(player_action_string[1])
                        last_player = (i - 1) % num_players
                if player_action == "Fold":
                    self.players[i].state = False
                if player_action == "Check":
                    pass
                if last_player == i:
                    break
            i = (i + 1) % num_players

    def game_start(self):
        waiting_for_res = []
        self.deck = Deck()
        for player in self.waiting_list:
            self.players.append(player)
        self.waiting_list = []
        for player in self.players:
            for _ in range(2):
                player.add_card(self.deck.draw_card())
        self.actions()
        for _ in range(3):
            self.board.append(self.deck.draw_card())
        self.actions()
        self.board.append(self.deck.draw_card())
        self.actions()
        self.board.append(self.deck.draw_card())
        self.split_jackpot()

    def split_jackpot(self):
        while self.players_total_bets_validation():
            waiting_for_res = []
            for player in self.players:
                if player.state and player.total_bet_per_round > 0:
                    waiting_for_res.append(player)
            winners = who_wins(waiting_for_res, self.board)
            winners.sort(key=lambda player: player.total_bet_per_round)  # sort by total bet per round
            temp = winners[0].total_bet_per_round
            num_winners = len(winners)
            for s_player in winners:
                for player in self.players:
                    s_player.balance += min(temp / len(winners), player.total_bet_per_round / num_winners)
                    player.total_bet_per_round -= min(temp / len(winners), player.total_bet_per_round / num_winners)
                num_winners -= 1

    def players_total_bets_validation(self):
        for player in self.players:
            if player.total_bet_per_round > 0:
                return True
        return False

