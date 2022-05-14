current_state = [
    ["X", " ", "O"],
    ["O", "X", "X"],
    ["X", " ", "O"]
]




def green(s):
    pict=str(s).replace(", ","|").replace("'", "")
    return "|"+pict[1:-1]+"|"


def print_filed(field):
    for item in field:
        print(green(item))


if __name__ == '__main__':
    print_filed(current_state)

