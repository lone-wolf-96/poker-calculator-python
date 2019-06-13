from final_class import final


@final
class Calculator:

    def __init__(self, filePath):
        self.__winners = [0, 0, 0]
        self.__games = 0
        self.calculate(filePath)

    @property
    def winners(self):
        return self.__winners

    @property
    def games(self):
        return self.__games

    def calculate(self, filePath):
        print(f"{filePath}\n")

    def print_results(self, filePath):
        print(f"{filePath}\n")
        return True

    def __check_winners_helper(self, num1, num2):
        comparer = (num1 > num2) - (num1 < num2)
        return (comparer + 2) % 3

    def __str__(self):
        winners = self.winners
        games = self.games

        return f"""Total Games: {games}\n
            Player 1: {winners[0]}\n
            Player 2: {winners[1]}\n
            Tie: {winners[2]}"""
