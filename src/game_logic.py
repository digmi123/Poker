import src.player
import src.deck


# TODO : comparison between two players if they returned the same thing


def flush(cards):
    sorter = {"Diamonds": [], "Clubs": [], "Spades": [], "Hearts": []}

    for card in cards:
        sorter[card.suit_type].append(card)
    for suit_arr in sorter.values():
        if len(suit_arr) >= 5:
            suit_arr.sort()
            return suit_arr[-5:]
    return None


def straight(cards):
    cards.sort()
    for i in range(len(cards), 4, -1):
        if is_straight(cards[i - 5:i]):
            return cards[i - 5:i]
    return None


def is_straight(cards):
    for i in range(4):
        if cards[i + 1].card_value - cards[i].card_value != 1:
            return False
    return True


def card_counter(cards):
    counts = same_card_counter(cards)
    max, second_max = max_list_in_dict(counts)
    # FOUR OF A KIND
    if len(counts[max]) == 4:
        return counts[max]
    # FULL HOUSE
    if len(counts[max] == 3) and len(counts[second_max] >= 2):
        return counts[max] + counts[second_max][:2]
    # THREE OF A KIND
    if len(counts[max] == 3):
        return counts[max]
    # TWO PAIRS
    if len(counts[max] == 2) and len(counts[second_max] == 2):
        return counts[max], counts[second_max]
    # PAIR
    if len(counts[max] == 2):
        return counts[max]
    # HIGH CARD
    if len(counts[max] == 1):
        return counts[max]


def same_card_counter(cards):
    counts = {i: [] for i in range(2, 15)}
    for card in cards:
        counts[card.card_value].append(card)
    return counts


def max_list_in_dict(cards_dict):
    max = 2
    second_max = 2
    for i in cards_dict.keys():
        if len(cards_dict[i]) >= len(cards_dict[max]):
            max = i
        elif len(cards_dict[i]) >= len(cards_dict[second_max]):
            second_max = i

    return max, second_max


def compare_flush(player1, player2, board):
    player1_total = player1.hand + board
    player2_total = player2.hand + board

    player1_flush = flush(player1_total)
    if player1_flush is not None:

        player1_flush = set(player1_flush)
    player2_flush = flush(player2_total)
    if player2_flush is not None:
        player2_flush = set(player2_flush)
    if player1_flush is not None and player2_flush is not None:
        if len(player1_flush.difference(player2_flush)) == 0:
            print(f"Draw between {player1.name} and {player2.name} with the flash : {board}")
            return [player1, player2]
        p1_selected_card = max(player1_flush.difference(player2_flush))
        p2_selected_card = max(player2_flush.difference(player1_flush))
        if p1_selected_card > p2_selected_card:
            print(f"{player1.name} wins with flash : {player1_flush}")
            return [player1]
        print(f"{player2.name} wins with flash : {player2_flush}")
        return [player2]

    if player1_flush is not None:
        print(f"{player1.name} wins with flash : {player1_flush}")
        return [player1]
    if player2_flush is not None:
        print(f"{player2.name} wins with flash : {player2_flush}")
        return [player2]
    return None


def compare_straight(player1, player2, board):
    player1_total = player1.hand + board
    player2_total = player2.hand + board

    player1_straight = straight(player1_total)
    player2_straight = straight(player2_total)
    if player1_straight is not None and player2_straight is not None:
        if player1_straight[0].card_value == player2_straight[0].card_value:
            print(
                f"Draw between {player1.name} and {player2.name}\n {player1.name} straight is : {player1_straight}\n {player2.name} straight is : {player2_straight} ")
            return [player1, player2]
        if player1_straight[0] > player2_straight[0]:
            print(f"{player1.name} wins with straight : {player1_straight}")
            return [player1]
        print(f"{player2.name} wins with straight : {player2_straight}")
        return [player2]
    if player1_straight is not None:
        print(f"{player1.name} wins with straight : {player1_straight}")
        return [player1]
    if player2_straight is not None:
        print(f"{player2.name} wins with straight : {player2_straight}")
        return [player2]
    return None


def compare_hands(player1, player2, board):
    res = compare_flush(player1, player2, board)
    if res is not None:
        return res
    res = compare_straight(player1, player2, board)
    if res is not None:
        return res
