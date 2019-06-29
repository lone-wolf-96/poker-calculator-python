import traceback
from datetime import datetime
from collections import Counter
from .hand import Hand
from .hand_rank import HandRank
from .utility import Utility


class Calculator:

    def __init__(self, file_path):
        self.__winners = [0, 0, 0]
        self.__games = 0
        self.__messages = []
        self.__calculate(file_path)

    @property
    def winners(self):
        return self.__winners

    @property
    def games(self):
        return self.__games

    def print_results(self, file_path):
        try:
            with open(file_path +
                      "poker_results_report.txt", "w") as fileReport, \
                open(file_path +
                     "poker_results.txt", "w") as fileResult:
                dateFormat = ("Date and Time: " +
                              datetime.now().strftime("%d-%m-%Y %H:%M:%S"))

                winners = self.winners
                games = self.games

                lines = []

                for i in range(3):
                    lines.append(f"{(i + 1)}: {winners[i]}")

                p1_percentage = "%.2f" % ((winners[0] / games) * 100)
                p2_percentage = "%.2f" % ((winners[1] / games) * 100)
                lines.extend(["4:",
                              "--------- PLAYER 1 --------- |" +
                              " --------- PLAYER 2 ---------",
                              f"           {p1_percentage}%            |" +
                              f"             {p2_percentage}%          ",
                              "---------------------------- |" +
                              " ----------------------------"])

                lines.append(f"Total Games: {games}")

                lines.append(dateFormat)
                self.__messages.append(dateFormat)

                fileReport.writelines("\n".join(lines))
                fileResult.writelines("\n".join(self.__messages))

                return True
        except Exception as e:
            traceback.print_exc()
            print(e)
            return False

    def __calculate(self, file_path):
        poker_data = self.__get_poker_data(file_path)

        if (poker_data is None):
            return

        poker_array = poker_data.split("-")
        self.__games = len(poker_array)

        for game in poker_array:
            game_array = game.replace("\n", "").split(" ")

            n = (len(game_array) + 1) // 2

            handString1 = " ".join(game_array[:n])
            handString2 = " ".join(game_array[n:])

            hand1 = Hand(Hand.from_string(handString1))
            hand2 = Hand(Hand.from_string(handString2))

            winnerIndex = self.__check_winners(hand1, hand2)
            winnerMessage = ("Winner " + str(winnerIndex + 1)
                             if winnerIndex < 2 else "Draw")

            self.__messages.append(winnerMessage + " : " +
                                   hand1.hand_rank.name.replace('_', ' ') +
                                   " - " +
                                   hand2.hand_rank.name.replace('_', ' '))

            self.__winners[winnerIndex] += 1

    def __get_poker_data(self, file_path):
        try:
            with open(file_path, "r") as file:
                return '-'.join(file)
        except Exception as e:
            traceback.print_exc()
            print(e)
            return None

    def __break_tie(self, hand1, hand2):
        rank = hand1.hand_rank

        if (rank is HandRank.ROYAL_FLUSH):
            return 2

        rank_numbers_1 = list(card.rank.rank_number
                              for card in hand1.cards)
        rank_numbers_1.sort()
        rank_numbers_2 = list(card.rank.rank_number
                              for card in hand2.cards)
        rank_numbers_2.sort()

        if (rank in [HandRank.STRAIGHT_FLUSH, HandRank.STRAIGHT]):
            return self.__break_tie_straight(rank_numbers_1, rank_numbers_2)

        if (rank in [HandRank.FLUSH, HandRank.HIGH_CARD]):
            return self.__break_tie_high_card(rank_numbers_1, rank_numbers_2)

        tie_breaker = self.__break_tie_rest_helper(rank)

        if (tie_breaker == -1):
            return 2

        return self.__break_tie_rest(rank_numbers_1,
                                     rank_numbers_2, tie_breaker)

    def __break_tie_rest_helper(self, rank):
        # replacement for switch
        return {
            HandRank.FOUR_OF_A_KIND: 4,
            HandRank.FULL_HOUSE: 3,
            HandRank.THREE_OF_A_KIND: 3,
            HandRank.TWO_PAIRS: 2,
            HandRank.ONE_PAIR: 2
        }.get(rank, -1)

    def __break_tie_rest(self, rank_numbers_1, rank_numbers_2, tie_breaker):
        frequency_tuple_1 = Counter(rank_numbers_1).most_common(1)[0]
        frequency_tuple_2 = Counter(rank_numbers_2).most_common(1)[0]

        winners = self.__check_winners_helper(
            frequency_tuple_1[0], frequency_tuple_2[0])

        if (winners != 2):
            return winners

        rank_numbers_1 = list(
            filter(lambda r: r != frequency_tuple_1[0], rank_numbers_1))
        rank_numbers_2 = list(
            filter(lambda r: r != frequency_tuple_2[0], rank_numbers_2))

        return self.__break_tie_straight(rank_numbers_1, rank_numbers_2)

    def __break_tie_straight(self, rank_numbers_1, rank_numbers_2):
        rank_numbers_1 = Utility.replace_ace_for_one_if(rank_numbers_1)
        rank_numbers_2 = Utility.replace_ace_for_one_if(rank_numbers_2)

        return self.__check_winners_helper(
            max(rank_numbers_1), max(rank_numbers_2))

    def __break_tie_high_card(self, rank_numbers_1, rank_numbers_2):
        reversed_range = range(len(rank_numbers_1))[::-1]
        winners = 2

        for i in reversed_range:
            winners = self.__check_winners_helper(
                rank_numbers_1[i], rank_numbers_2[i])
            if (winners != 2):
                return winners

        return 2

    def __check_winners(self, hand1, hand2):
        winners = self.__check_winners_helper(hand1.hand_rank, hand2.hand_rank)
        return winners if winners != 2 else self.__break_tie(hand1, hand2)

    def __check_winners_helper(self, num1, num2):
        comparer = (num1 > num2) - (num1 < num2)
        return (comparer + 2) % 3

    def __str__(self):
        winners = self.winners
        games = self.games

        return (f"Total Games: {games}\n" +
                f"Player 1: {winners[0]}\n" +
                f"Player 2: {winners[1]}\n"
                f"Tie: {winners[2]}")
