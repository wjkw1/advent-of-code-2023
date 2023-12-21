from src import utils
from enum import Enum, auto


CARD_RANKS = {
    "2": 2,
    "3": 3,
    "4": 4,
    "5": 5,
    "6": 6,
    "7": 7,
    "8": 8,
    "9": 9,
    "T": 10,
    "J": 11,
    "Q": 12,
    "K": 13,
    "A": 14,
}

HAND_STRENGTHS = {
    "Five of a Kind": 6,
    "Four of a Kind": 5,
    "Full House": 4,
    "Three of a Kind": 3,
    "Two Pair": 2,
    "One Pair": 1,
    "High Card": 0,
}


class Hand:
    def __init__(self, cards, bid):
        self.cards = cards
        self.bid = int(bid)
        self.hand_type = self._get_hand_type()
        self.hand_strength = self._get_hand_strength()

    def _get_hand_value(self):
        value = 0
        for card in self.cards:
            value += CARD_RANKS[card]
        return value

    def _get_hand_strength(self):
        """Multiply the card value by hand type value."""
        return HAND_STRENGTHS[self.hand_type]

    def cards_sort_by_rank(self):
        cards_as_list = list(self.cards)
        return sorted(cards_as_list, key=lambda card: CARD_RANKS[card])

    def _get_hand_type(self):
        # sorted_cards = self.cards_sort_by_rank()
        rank_counts = {rank: self.cards.count(rank) for rank in self.cards}

        # Check for each hand type
        if 5 in rank_counts.values():
            return "Five of a Kind"
        if 4 in rank_counts.values():
            return "Four of a Kind"
        if 3 in rank_counts.values() and 2 in rank_counts.values():
            return "Full House"
        if 3 in rank_counts.values():
            return "Three of a Kind"

        hand_type = "High Card"
        # Count the number of pairs
        pair_count = 0
        for count in rank_counts.values():
            if count == 2:
                pair_count += 1
        if pair_count == 2:
            hand_type = "Two Pair"
        if pair_count == 1:
            hand_type = "One Pair"
        return hand_type

    def __repr__(self):
        return f"{self.__class__.__name__}(hand_strength={self.hand_strength}, cards={self.cards}, bid={self.bid}, hand_type={self.hand_type})"


def compare_hands(hand: Hand):
    return (
        hand.hand_strength,
        CARD_RANKS[hand.cards[0]],
        CARD_RANKS[hand.cards[1]],
        CARD_RANKS[hand.cards[2]],
        CARD_RANKS[hand.cards[3]],
        CARD_RANKS[hand.cards[4]],
    )


if __name__ == "__main__":
    # inputs = utils.read_file("src/day07/input-mini.txt")
    inputs = utils.read_file("src/day07/input.txt")

    hands = []
    for hand in inputs:
        cards, bid = hand.split()
        hand = Hand(cards, bid)
        sorted_hand = hand.cards_sort_by_rank()
        hand_value = hand._get_hand_value()
        hand_strength = hand._get_hand_strength()
        hands.append(hand)

    # find the rank of our set using sorted
    hands_by_strength = sorted(hands, key=compare_hands)

    winnings = 0
    for rank, hand in enumerate(hands_by_strength, start=1):
        winnings = winnings + (hand.bid * rank)

    print(winnings)
