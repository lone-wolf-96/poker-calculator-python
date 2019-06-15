from pokercalculator.pokercalculator.hand import Hand
from pokercalculator.pokercalculator.hand_rank import HandRank
from pokercalculator.pokercalculator.card import Card
from pokercalculator.pokercalculator.rank import Rank
from pokercalculator.pokercalculator.suit import Suit


def test_hand():
    Hand([Card(Rank.JACK, Suit.SPADES),
          Card(Rank.FOUR, Suit.HEARTS),
          Card(Rank.FIVE, Suit.DIAMONDS),
          Card(Rank.NINE, Suit.DIAMONDS),
          Card(Rank.JACK, Suit.CLUBS)])


def test_cards():
    cards1 = [Card(Rank.JACK, Suit.SPADES),
              Card(Rank.FOUR, Suit.HEARTS),
              Card(Rank.FIVE, Suit.DIAMONDS),
              Card(Rank.NINE, Suit.DIAMONDS),
              Card(Rank.JACK, Suit.CLUBS)]
    assert cards1 == Hand(cards1).cards

    cards2 = [Card(Rank.QUEEN, Suit.CLUBS),
              Card(Rank.TEN, Suit.CLUBS),
              Card(Rank.SIX, Suit.HEARTS),
              Card(Rank.FIVE, Suit.SPADES),
              Card(Rank.THREE, Suit.HEARTS)]
    assert cards2 == Hand(cards2).cards


def test_hand_rank():
    cards1 = [Card(Rank.JACK, Suit.SPADES),
              Card(Rank.FOUR, Suit.HEARTS),
              Card(Rank.FIVE, Suit.DIAMONDS),
              Card(Rank.NINE, Suit.DIAMONDS),
              Card(Rank.JACK, Suit.CLUBS)]
    assert HandRank.ONE_PAIR == Hand(cards1).hand_rank

    cards2 = [Card(Rank.QUEEN, Suit.CLUBS),
              Card(Rank.TEN, Suit.CLUBS),
              Card(Rank.SIX, Suit.HEARTS),
              Card(Rank.FIVE, Suit.SPADES),
              Card(Rank.THREE, Suit.HEARTS)]
    assert HandRank.HIGH_CARD == Hand(cards2).hand_rank


def test_from_string():
    cards = Hand.from_string("6C 3D TH KC 4S")

    six_of_clubs = cards[0]
    three_of_diamonds = cards[1]
    ten_of_hearts = cards[2]
    king_of_clubs = cards[3]
    four_of_spades = cards[4]

    assert Rank.SIX == six_of_clubs.rank
    assert Suit.CLUBS == six_of_clubs.suit

    assert Rank.THREE == three_of_diamonds.rank
    assert Suit.DIAMONDS == three_of_diamonds.suit

    assert Rank.TEN == ten_of_hearts.rank
    assert Suit.HEARTS == ten_of_hearts.suit

    assert Rank.KING == king_of_clubs.rank
    assert Suit.CLUBS == king_of_clubs.suit

    assert Rank.FOUR == four_of_spades.rank
    assert Suit.SPADES == four_of_spades.suit


def test_to_string_name():
    cards1 = [Card(Rank.JACK, Suit.SPADES),
              Card(Rank.FOUR, Suit.HEARTS),
              Card(Rank.FIVE, Suit.DIAMONDS),
              Card(Rank.NINE, Suit.DIAMONDS),
              Card(Rank.JACK, Suit.CLUBS)]
    assert ("JACK OF SPADES\n" +
            "FOUR OF HEARTS\n" +
            "FIVE OF DIAMONDS\n" +
            "NINE OF DIAMONDS\n" +
            "JACK OF CLUBS" == Hand(cards1).to_string_name())

    cards2 = [Card(Rank.QUEEN, Suit.CLUBS),
              Card(Rank.TEN, Suit.CLUBS),
              Card(Rank.SIX, Suit.HEARTS),
              Card(Rank.FIVE, Suit.SPADES),
              Card(Rank.THREE, Suit.HEARTS)]
    assert ("QUEEN OF CLUBS\n" +
            "TEN OF CLUBS\n" +
            "SIX OF HEARTS\n" +
            "FIVE OF SPADES\n" +
            "THREE OF HEARTS" == Hand(cards2).to_string_name())


def test_str():
    cards1 = [Card(Rank.JACK, Suit.SPADES),
              Card(Rank.FOUR, Suit.HEARTS),
              Card(Rank.FIVE, Suit.DIAMONDS),
              Card(Rank.NINE, Suit.DIAMONDS),
              Card(Rank.JACK, Suit.CLUBS)]
    assert "JS 4H 5D 9D JC" == str(Hand(cards1))

    cards2 = [Card(Rank.QUEEN, Suit.CLUBS),
              Card(Rank.TEN, Suit.CLUBS),
              Card(Rank.SIX, Suit.HEARTS),
              Card(Rank.FIVE, Suit.SPADES),
              Card(Rank.THREE, Suit.HEARTS)]
    assert "QC TC 6H 5S 3H" == str(Hand(cards2))
