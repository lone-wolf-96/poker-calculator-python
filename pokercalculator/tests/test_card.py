from pokercalculator.pokercalculator.card import Card
from pokercalculator.pokercalculator.rank import Rank
from pokercalculator.pokercalculator.suit import Suit


def test_card():
    Card(Rank.JACK, Suit.SPADES)


def test_get_rank():
    assert Rank.TWO == Card(Rank.TWO, Suit.DIAMONDS).rank
    assert Rank.FIVE == Card(Rank.FIVE, Suit.SPADES).rank
    assert Rank.TEN == Card(Rank.TEN, Suit.CLUBS).rank
    assert Rank.SIX == Card(Rank.SIX, Suit.HEARTS).rank
    assert Rank.SEVEN == Card(Rank.SEVEN, Suit.DIAMONDS).rank


def test_get_suit():
    assert Suit.DIAMONDS == Card(Rank.SIX, Suit.DIAMONDS).suit
    assert Suit.SPADES == Card(Rank.ACE, Suit.SPADES).suit
    assert Suit.CLUBS == Card(Rank.QUEEN, Suit.CLUBS).suit
    assert Suit.HEARTS == Card(Rank.THREE, Suit.HEARTS).suit


def test_from_string():
    ten_of_clubs = Card.from_string("TC")
    assert Rank.TEN == ten_of_clubs.rank
    assert Suit.CLUBS == ten_of_clubs.suit

    jack_of_hearts = Card.from_string("JH")
    assert Rank.JACK == jack_of_hearts.rank
    assert Suit.HEARTS == jack_of_hearts.suit

    eight_of_diamonds = Card.from_string("8D")
    assert Rank.EIGHT == eight_of_diamonds.rank
    assert Suit.DIAMONDS == eight_of_diamonds.suit


def test_to_string_name():
    assert "TWO OF CLUBS" == Card(Rank.TWO, Suit.CLUBS).to_string_name()
    assert "ACE OF SPADES" == Card(Rank.ACE, Suit.SPADES).to_string_name()


def test_str():
    assert "7D" == str(Card(Rank.SEVEN, Suit.DIAMONDS))
    assert "KH" == str(Card(Rank.KING, Suit.HEARTS))
