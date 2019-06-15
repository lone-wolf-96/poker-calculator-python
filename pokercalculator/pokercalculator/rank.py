from enum import Enum, unique


@unique
class Rank(Enum):

    TWO = (2, '2')
    THREE = (3, '3')
    FOUR = (4, '4')
    FIVE = (5, '5')
    SIX = (6, '6')
    SEVEN = (7, '7')
    EIGHT = (8, '8')
    NINE = (9, '9')
    TEN = (10, 'T')
    JACK = (11, 'J')
    QUEEN = (12, 'Q')
    KING = (13, 'K')
    ACE = (14, 'A')

    def __init__(self, rank_number, rank_value):
        self.__rank_number = rank_number
        self.__rank_value = rank_value

    @property
    def rank_number(self):
        return self.__rank_number

    @property
    def rank_value(self):
        return self.__rank_value

    @classmethod
    def get_rank_by_rank_value(cls, rank_value):
        return next(rank for rank in cls if rank.rank_value == rank_value)
