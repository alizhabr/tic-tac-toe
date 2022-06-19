import random
import os
import time
from copy import deepcopy

CURRENT_STATE = [
    [" ", " ", " ", " "],
    [" ", "X", " ", " "],
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

    def diagonals_backslash():
        # diag = row_number - col_number
        for diag in range(0 - COLS + 1, ROWS - 0):
            min_row = max(diag, 0)
            x = min_row
            y = x - diag

            while (x < ROWS - 1) and (y < COLS - 1):
                x += 1
                y += 1
            max_row = x

            k = 1
            best_letter_len = 1

            for x in range(min_row + 1, max_row + 1):
                y_new = x - diag

                if (CURRENT_STATE[x][y_new] == CURRENT_STATE[x - 1][y_new - 1]) and CURRENT_STATE[x][y_new] != " ":
                    k += 1
                else:
                    if k > best_letter_len:
                        best_letter_len = k
                        best_letter = CURRENT_STATE[x - 1][y_new - 1]
                    k = 1

            if k > best_letter_len:
                best_letter_len = k
                best_letter = CURRENT_STATE[x - 1][y_new - 1]

            if best_letter_len >= TO_WIN:
                return best_letter
        return "no"

    def diagonals_slash():
        # переписать, не обращаясь к полю.
        for i in range(COLS):
            CURRENT_STATE[i] = CURRENT_STATE[i][::-1]

        answer = diagonals_backslash()

        for i in range(COLS):
            CURRENT_STATE[i] = CURRENT_STATE[i][::-1]

        return answer

    if column() != "no":
        return column()

    if row() != "no":
        return row()

    if diagonals_slash() != "no":
        return diagonals_slash()

    if diagonals_backslash() != "no":
        return diagonals_backslash()

    return "no"



#  max row
# best_letter = CURRENT_STATE[x][0]
# best_letter_len = 1


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

    # смотрит все ходы ^
    # пробует сходить в каждый
    #  копирует поле.
    global CURRENT_STATE

    random.shuffle(moves)
    dump_big = deepcopy(CURRENT_STATE)

    for move in moves:
        CURRENT_STATE = deepcopy(dump_big)

        x, y = move
        make_move(x, y, COMP_LETTER)
        # /////
        # победа за 1 ход
        if check_is_over() != "no":
            return
        # /////
        CURRENT_STATE = deepcopy(dump_big)
        make_move(x, y, "X")
        if check_is_over() != "no":
            CURRENT_STATE = deepcopy(dump_big)
            x, y = move
            make_move(x, y, COMP_LETTER)
            return

        # цикл по ходам Крестика.
        # ... continue


    # x, y = random.choice(moves)



if __name__ == '__main__':
    print_field()

    for turn in range(5):
        x=int(input())
        y=int(input())
        letter="X"
        make_move(x,y,letter)
        print_field()

        if check_is_over() != "no":
            print("X wins")
            quit()

        time.sleep(1)
        print("\n" * 2)
        comp_make_action()
        print_field()
        if check_is_over()!="no":
            print("O wins")
            quit()

    """
        ввести координаты
        после этого делает ход.
        def choose_action(possible_moves):
            chosen_action = random.choice(possible_moves)
    #         do action
    """
