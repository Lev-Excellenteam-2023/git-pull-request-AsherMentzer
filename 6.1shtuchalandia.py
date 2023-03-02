def find_special_state(file_name):
    """
    find the state that can written with letters in the sane row in the keyboard
    :param file_name: the file of state
    :return: the special state
    """
    states = set()
    with open(file_name, 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]
        states = set(lines)
    r1 = "q w e r t y u i o p"
    r2 = "a s d f g h j k l"
    r3 = "z x c v b n m"
    row1 = set(r1.split(" "))
    row2 = set(r2.split(" "))
    row3 = set(r3.split(" "))
    is_in_one_row = set()
    for state in states:
        first_letter = state[0]
        row = 0
        if first_letter in row1:
            row = row1
        elif first_letter in row2:
            row = row2
        else:
            row = row3
        same_row = True
        for letter in state:
            if letter not in row:
                same_row = False
                break
        if same_row:
            is_in_one_row.add(state)
    return is_in_one_row


def main():
    print(find_special_state("states.txt"))


if __name__ == '__main__':
    main()
