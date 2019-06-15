from os import getcwd
from final_class import final
from .calculator import Calculator


@final
class App:

    @staticmethod
    def main():
        try:
            next_line = input(
                "Enter the pokerdata.txt source directory" +
                "(Press Enter for default):\n")
            source_path = App.__get_folder(next_line, "pokerdata.txt")

            next_line = input(
                "Enter the poker_results.txt target directory" +
                "(Press Enter for default):\n")
            target_path = App.__get_folder(next_line, "poker_results.txt")

            if (Calculator(source_path).print_results(target_path)):
                print("Successful results in your folder.\n")
            else:
                print("There's been an error processing the information.\n")
        except Exception as e:
            print(str(e))

    @staticmethod
    def __get_folder(line, file_name):
        return (line if len(line) > 0 else getcwd()) + "\\" + file_name
