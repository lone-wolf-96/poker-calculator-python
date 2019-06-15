from enum import Enum, unique


@unique
class Suit(Enum):

    SPADES = 'S'
    HEARTS = 'H'
    CLUBS = 'C'
    DIAMONDS = 'D'

    def __init__(self, suit_value):
        self.__suit_value = suit_value

    @property
    def suit_value(self):
        return self.__suit_value

    @classmethod
    def get_suit_by_suit_value(cls, suit_value):
        return next(suit for suit in cls if suit.suit_value == suit_value)
