current_state = [
    ["X", "X", "X", " "],
    ["", "O", "O", " "],
    ["O", " ", "X", " "],
    [" ", " ", " ", " "],
]

TO_WIN = 3


def check_is_over():
    for line in current_state:
        string = "".join(line)
        if string.count("X")==3:
            print ("X")
        elif string.count("O")==3:
            print("O")
        else:
            print(" ")
    for column in current_state:

        # TODO: Найти в ней ^ три крестика, вернуть "X"(ok)


#          TODO: если O, то вернуть "O" (ok)
#             Если в итоге _никто_, вернуть " "(ok)

#     сделать аналогичную проверку на столбцы
#     * аналогичное на диагонали


def green(s):
    pict = str(s).replace(", ", "|").replace("'", "")
    return "|" + pict[1:-1] + "|"


def print_filed(field):
    for item in field:
        print(green(item))


def check_possible_move(x, y, letter):
    if current_state[x][y] == " ":
        if letter == "X" or letter == "O":
            return True

    return False


def move(x, y, letter):
    current_state[x][y] = letter


def make_move(x, y, letter):
    if check_possible_move(x, y, letter):
        move(x, y, letter)
    else:
        print("Forbidden action {} {} {}".format(x, y, letter))


if __name__ == '__main__':
    print_filed(current_state)
    check_is_over()
    print()
    make_move(0, 3, "O")
    print_filed(current_state)
    check_is_over()
    print()
    make_move(2, 1, 'X')
    print_filed(current_state)
    check_is_over()
    # */2 реализовать последовательную игру с компьютером

