from os import getcwd
from pokercalculator.pokercalculator.calculator import Calculator


FILE_PATH_SOURCE = getcwd() + "\\" + "pokerdata.txt"
CALCULATOR = Calculator(FILE_PATH_SOURCE)


def test_calculator():
    Calculator(FILE_PATH_SOURCE)


def test_get_winners():
    winners = [376, 624, 0]
    assert CALCULATOR.winners == winners


def test_get_games():
    games = 1000
    assert CALCULATOR.games == games


def test_print_results():
    file_path_target = getcwd() + "\\"
    assert CALCULATOR.print_results(file_path_target) is True


def test_str():
    assert "Total Games: 1000\nPlayer 1: 376\nPlayer 2: 624\nTie: 0" == str(
        CALCULATOR)
