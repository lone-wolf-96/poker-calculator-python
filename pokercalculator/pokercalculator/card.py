from .suit import Suit
from .rank import Rank


class Card:

    def __init__(self, rank, suit):
        self.__rank = rank
        self.__suit = suit

    @property
    def rank(self):
        return self.__rank

    @property
    def suit(self):
        return self.__suit

    @staticmethod
    def from_string(input):
        rank = Rank.get_rank_by_rank_value(input[0])
        suit = Suit(input[1])  # or Suit.get_suit_by_suit_value(input[1])

        return Card(rank, suit)

    def to_string_name(self):
        rank_name = self.rank.name
        suit_name = self.suit.name

        return rank_name + " OF " + suit_name

    def __str__(self):
        rank_char = self.rank.rank_value
        suit_char = self.suit.suit_value

        return rank_char + "" + suit_char
