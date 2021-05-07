import src.deck
import src.player
from enum import IntEnum


class Match(IntEnum):

    High_card = 1
    Pair = 2
    Two_pair = 3
    Three_of_a_kind = 4
    Straight = 5
    Flush = 6
    Full_house = 7
    Four_of_a_kind = 8
    Straight_flash = 9
    Royal_flush = 10


def same_card_counter(cards):
    counts = {i: [] for i in range(1, 15)}
    for card in cards:
        counts[card.card_value].append(card)
    return counts


def rank_type_counter(cards):
    counts = same_card_counter(cards)
    first_max, second_max = significant_cards(counts)
    kickers = list(set(cards) - set(counts[first_max]) - set(counts[second_max]))
    kickers.sort(reverse=True)
    final_cards = counts[first_max] + counts[second_max] + kickers
    final_cards = final_cards[:5]
    rank = rank_counter(len(counts[first_max]), len(counts[second_max]))
    return final_cards, rank


def rank_decider(player, board):
    cards = player.hand + board
    flush_hand, flush_rank = flush(cards)
    if flush_rank in [Match.Straight_flash, Match.Royal_flush]:
        return flush_hand, flush_rank
    counter_hand, counter_rank = rank_type_counter(cards)
    if counter_rank in [Match.Four_of_a_kind, Match.Full_house]:
        return counter_hand, counter_rank
    if flush_rank in [Match.Flush]:
        return flush_hand, flush_rank
    straight_hand, straight_rank = straight(cards)
    if straight_rank in [Match.Straight]:
        return straight_hand, straight_rank
    return counter_hand, counter_rank


def significant_cards(counts):
    first_max = 1
    second_max = 1
    for i in counts.keys():
        if len(counts[i]) >= len(counts[first_max]):
            second_max = first_max
            first_max = i
        elif len(counts[i]) >= len(counts[second_max]):
            second_max = i
    return first_max, second_max


def rank_counter(first_max_len, second_max_len):
    if first_max_len == 1:
        return Match.High_card
    if first_max_len == 2:
        if second_max_len == 2:
            return Match.Two_pair
        return Match.Pair
    if first_max_len == 3:
        if second_max_len == 2:
            return Match.Full_house
        return Match.Three_of_a_kind
    if first_max_len == 4:
        return Match.Four_of_a_kind


def is_straight(cards):
    for i in range(4):
        if cards[i].card_value - cards[i + 1].card_value != 1:
            return False
    return True


def straight(cards):
    cards.sort(reverse=True)
    for i in range(len(cards) - 5):
        if is_straight(cards[i:i + 5]):
            return cards[i - 5:i], Match.Straight
    return None, None


def flush(cards):
    sorter = {"Diamonds": [], "Clubs": [], "Spades": [], "Hearts": []}

    for card in cards:
        sorter[card.suit_type].append(card)
    for suit_arr in sorter.values():
        if len(suit_arr) >= 5:
            straight_flush, _ = straight(suit_arr)
            if straight_flush is not None:
                if straight_flush[0].card_value == 10:
                    return straight_flush, Match.Royal_flush
                return straight_flush, Match.Straight_flash
            return suit_arr[:5], Match.Flush
    return None, None


def compare_hands(player1, player2, board):
    player1_hand, player1_rank = rank_decider(player1, board)
    player2_hand, player2_rank = rank_decider(player2, board)
    if player1_rank > player2_rank:
        return [player1], player1_rank, [player1_hand]
    if player1_rank < player2_rank:
        return [player2], player2_rank, [player2_hand]
    for card1, card2 in zip(player1_hand, player2_hand):
        if card1 > card2:
            return [player1], player1_rank, [player1_hand]
        if card1 < card2:
            return [player2], player2_rank, [player2_hand]
    return [player1, player2], player1_rank, [player1_hand, player2_hand]
