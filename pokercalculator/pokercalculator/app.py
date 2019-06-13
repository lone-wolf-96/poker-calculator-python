import os
from .calculator import Calculator


class App:

    @staticmethod
    def main():
        try:
            nextLine = input(
                "Enter the pokerdata.txt source directory" +
                "(Press Enter for default):\n")
            sourcePath = App.__get_folder(nextLine, "pokerdata.txt")

            nextLine = input(
                "Enter the poker_results.txt target directory" +
                "(Press Enter for default):\n")
            targetPath = App.__get_folder(nextLine, "poker_results.txt")

            if Calculator(sourcePath).print_results(targetPath):
                print("Successful results in your folder.\n")
            else:
                print("There's been an error processing the information.\n")

        except Exception as e:
            print(str(e))

    @staticmethod
    def __get_folder(line, fileName):
        return (line + "\\" if len(line) > 0 else os.getcwd() + "/") + fileName
