from collections import Counter
from .hand_rank import HandRank
from .card import Card
from .rank import Rank
from .utility import Utility


class Hand:

    HAND_SIZE = 5

    def __init__(self, cards):
        self.__cards = cards
        self.__hand_rank = self.__evaluate()

    @property
    def cards(self):
        return self.__cards

    @property
    def hand_rank(self):
        return self.__hand_rank

    @staticmethod
    def from_string(input):
        parts = input.split(" ")
        cards = list(map(lambda part: Card.from_string(part), parts))
        return cards

    def to_string_name(self):
        cards = self.cards
        return "\n".join(card.to_string_name() for card in cards)

    def __evaluate(self):
        cards_in_hand = self.cards
        is_flush = len(set(map(
            lambda card: card.suit.suit_value, cards_in_hand))) == 1

        rank_numbers = [card.rank.rank_number for card in cards_in_hand]
        rank_numbers.sort()
        is_straight = self.__is_straight(rank_numbers)

        if (is_flush and is_straight):
            if (self.__is_royal(cards_in_hand)):
                return HandRank.ROYAL_FLUSH
            return HandRank.STRAIGHT_FLUSH

        frequency_dict = Counter(rank_numbers)
        rank_number_count = (frequency_dict.most_common(1)[0])[1]

        if(rank_number_count == 4):
            return HandRank.FOUR_OF_A_KIND

        is_three_of_a_kind = rank_number_count == 3
        is_one_pair = rank_number_count == 2

        if (is_three_of_a_kind and is_one_pair):
            return HandRank.FULL_HOUSE
        if (is_flush):
            return HandRank.FLUSH
        if (is_straight):
            return HandRank.STRAIGHT
        if (is_three_of_a_kind):
            return HandRank.THREE_OF_A_KIND

        most_commons_pairs = frequency_dict.most_common(2)

        if (is_one_pair):
            if(all(freq[1] == 2 for freq in most_commons_pairs)):
                return HandRank.TWO_PAIRS
            return HandRank.ONE_PAIR

        return HandRank.HIGH_CARD

    def __is_straight(self, rank_numbers):
        rank_numbers = Utility.replace_ace_for_one_if(rank_numbers)
        sequential_ranks = list(
            range(rank_numbers[0], rank_numbers[0] + self.HAND_SIZE))

        return rank_numbers == sequential_ranks

    def __is_royal(self, cards_in_hand):
        ten = Rank.TEN.rank_number
        ace = Rank.ACE.rank_number

        return (all(ten <= card.rank.rank_number and
                    card.rank.rank_number <= ace
                    for card in cards_in_hand))

    def __str__(self):
        cards = self.cards
        return " ".join(str(card) for card in cards)
