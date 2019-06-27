from os import getcwd
import traceback
from .calculator import Calculator


class App:

    @staticmethod
    def main():
        try:
            next_line = input(
                "Enter the pokerdata.txt source directory " +
                "(Press Enter for default):\n")
            source_path = App.__get_folder(next_line) + "pokerdata.txt"

            next_line = input(
                "Enter the target directory " +
                "(Press Enter for default):\n")
            target_path = App.__get_folder(next_line)

            if (Calculator(source_path).print_results(target_path)):
                print("Successful results in your folder.\n")
            else:
                print("There's been an error processing the information.\n")
        except Exception as e:
            traceback.print_exc()
            print(e)

    @staticmethod
    def __get_folder(line):
        if (len(line) > 0):
            return line + ("" if line[len(line) - 1] == "\\" else "\\")
        return getcwd() + "\\"
