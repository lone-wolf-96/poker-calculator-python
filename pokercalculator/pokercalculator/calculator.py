from datetime import datetime
from final_class import final


@final
class Calculator:

    def __init__(self, filePath):
        self.__winners = [0, 0, 0]
        self.__games = 0
        self.__calculate(filePath)

    @property
    def winners(self):
        return self.__winners

    @property
    def games(self):
        return self.__games

    def print_results(self, file_path):
        try:
            file = open(file_path, "w")

            winners = self.winners
            games = self.games

            lines = [f"Total Games: {games}\n"]

            for i in range(3):
                s = f"{(i + 1)}: {winners[i]}\n"
                lines.append(s)

            p1_percentage = "%.2f" % ((winners[0] / games) * 100)
            p2_percentage = "%.2f" % ((winners[1] / games) * 100)
            lines.append(["4:\n",
                          "--------- PLAYER 1 --------- |" +
                          " --------- PLAYER 2 ---------\n",
                          f"           {p1_percentage}%            |" +
                          f"             {p2_percentage}%          \n",
                          "---------------------------- |" +
                          " ----------------------------"])

            now = datetime.now().strftime("%d-%m-%Y, %H:%M:%S")
            lines.append(now)

            file.writelines(lines)
            return True
        except (FileNotFoundError, TypeError) as e:
            print(str(e))
            return False
        finally:
            file.close()

    def __calculate(self, file_path):
        poker_data = self.__get_poker_data(file_path)

        if (poker_data is None):
            return

        poker_array = poker_data.split("-")
        self.__games = len(poker_array)

        for game in poker_array:
            game_array = game.replace("\n", "").split(" ")
            n = len(game_array) + 1

            handString1 = game_array[:n // 2]
            handString2 = game_array[n // 2:]

            hand1 = 1  # Hand(Hand.from_string(handString1))
            hand2 = 2  # Hand(Hand.from_string(handString2))

            print(str(handString1) + " - " + str(handString2))

            self.__winners[self.__check_winners(hand1, hand2)] += 1

    def __get_poker_data(self, file_path):
        try:
            file = open(file_path, "r")
            return '-'.join(file)
        except (FileNotFoundError, TypeError) as e:
            print(str(e))
            return None
        finally:
            file.close()

    def __break_tie(self, hand1, hand2):
        pass

    def __break_tie_rest_helper(self, ranks):
        pass

    def __break_tie_rest(self):
        pass

    def __break_tie_straight(self):
        pass

    def __break_tie_high_card(self):
        pass

    def __check_winners(self, hand1, hand2):
        hand1Rank = 1  # hand1.get_hand_rank().ordinal()
        hand2Rank = 2  # hand2.get_hand_rank().ordinal()

        winners = self.__check_winners_helper(hand1Rank, hand2Rank)
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
