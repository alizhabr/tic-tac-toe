import random
import os

CURRENT_STATE = [
    [" ", " ", " ", " "],
    [" ", " ", " ", " "],
    [" ", " ", " ", " "],
    [" ", " ", " ", " "],
    [" ", " ", " ", " "],
]

TO_WIN = 3
ROWS = len(CURRENT_STATE)
COLS = len(CURRENT_STATE[0])
COMP_LETTER = "O"


def check_is_over():
    def column():
        for y in range(COLS):
            k = 1
            best_letter = CURRENT_STATE[0][y]
            best_letter_len = 1
            for x in range(1, ROWS):
                if (CURRENT_STATE[x][y] == CURRENT_STATE[x - 1][y]) and CURRENT_STATE[x][y] != " ":
                    k += 1
                else:
                    if k > best_letter_len:
                        best_letter_len = k
                        best_letter = CURRENT_STATE[x - 1][y]
                    k = 1

            if k > best_letter_len:
                best_letter_len = k
                best_letter = CURRENT_STATE[x - 1][y]

            if best_letter_len >= TO_WIN:
                return best_letter

        return "no"

    def row():
        for x in range(ROWS):
            k = 1
            best_letter = CURRENT_STATE[x][0]
            best_letter_len = 1
            for y in range(1, COLS):
                if (CURRENT_STATE[x][y] == CURRENT_STATE[x][y-1]) and CURRENT_STATE[x][y] != " ":
                    k += 1
                else:
                    if k > best_letter_len:
                        best_letter_len = k
                        best_letter = CURRENT_STATE[x][y-1]
                    k = 1

            if k > best_letter_len:
                best_letter_len = k
                best_letter = CURRENT_STATE[x][y-1]

            if best_letter_len >= TO_WIN:
                return best_letter
        return "no"

    if column() != "no":
        return column()

    if row() != "no":
        return row()

    return "no"


def print_field():
    def green(s):
        pict = str(s).replace(", ", "|").replace("'", "")
        return "|" + pict[1:-1] + "|"

    for item in CURRENT_STATE:
        print(green(item))


def check_possible_move(x, y, letter):
    if CURRENT_STATE[x][y] == " ":
        if letter == "X" or letter == "O":
            return True
    return False


def make_move(x, y, letter):
    def move(x, y, letter):
        CURRENT_STATE[x][y] = letter

    if check_possible_move(x, y, letter):
        move(x, y, letter)
    else:
        print("Forbidden action {} {} {}".format(x, y, letter))

def get_possible_moves():
    listt=[]
    for x in range(ROWS):
        for y in range(COLS):
            if check_possible_move(x,y, COMP_LETTER):
                listt += [(x, y)]
    return listt


def comp_make_action():
    moves = get_possible_moves()
    x, y = random.choice(moves)
    make_move(x, y, COMP_LETTER)


if __name__ == '__main__':
    print_field()

    for turn in range(4):
        print("\n" * 10)
        comp_make_action()
        print_field()
    """
        ввести координаты
        проверить, что они валидны (потом)
        сделать ход за комп. просматривает все поля, сохраняет себе те, в которые он может ходить
            possible_moves = [(0, 0), (1, 2) ... ]
        после этого делает ход.
        def choose_action(possible_moves):
            chosen_action = random.choice(possible_moves)
    #         do action
    """

