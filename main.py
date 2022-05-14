current_state = [
    ["X", " ", "O"],
    ["O", "X", "O"],
    ["X", " ", "X"]
]


def green(s):
    pict=str(s).replace(", ","|").replace("'", "")
    return "|"+pict[1:-1]+"|"


def print_filed(field):
    for item in field:
        print(green(item))


def check_possible_move(x, y, letter):
#     if field is empty -> return True
#     else False
#     also check letter TODO
    if current_state[x][y] == " ":
        return True
    else:
        return False


def move(x, y, letter):
    current_state[x][y]=letter


if __name__ == '__main__':
    print_filed(current_state)
    print()
    move(0, 1, "O")
    print_filed(current_state)
    print()
    x, y, letter = 0, 0, "X"

    # обурнуть в ф-ю TODO
    if check_possible_move(x, y, letter):
        move(x, y, letter)
    else:
        print("Forbidden action {} {} {}".format(x, y, letter))

