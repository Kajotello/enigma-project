
alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def validate_input(str):
    if len(str) == 1 and str in alphabet:
        return 0
    else:
        return 1


def validate_plugboard(str):
    i = 0
    check_table = []

    for j, letter in enumerate(str, 1):

        if letter == " ":
            if i == 2:
                i = 0
            else:
                return (1, None)

        elif letter not in alphabet:
            return (2, letter)

        elif letter not in check_table:
            if j == len(str) and i != 1:
                return (3, None)
            i += 1
            check_table.append(letter)

        else:
            return (4, letter)

    return (0, None)


def validate_new_rotor(wiring, name, elements, old_name=None):

    # need to add inedntation check

    check_table = []

    if len(wiring) != 26:
        return (1, None)

    for letter in wiring:
        if letter not in alphabet:
            return (2, letter)
        if letter in check_table:
            return (3, letter)
        else:
            check_table.append(letter)

    if name in elements.rotors.keys() and name != old_name:
        return (4, None)

    if len(name) == 0:
        return (5, None)

    return (0, None)


def validate_new_reflector(wiring, name, elements, old_name=None):

    i = 0
    check_table = []

    if len(wiring) != 38:
        return(1, None)

    for j, letter in enumerate(wiring, 1):

        if letter == " ":
            if i == 2:
                i = 0
            else:
                return (2, None)

        elif letter not in alphabet:
            return (3, letter)

        elif letter not in check_table:
            if j == len(wiring) and i != 1:
                return (4, None)
            i += 1
            check_table.append(letter)

        else:
            return (5, letter)

    if name in elements.reflectors.keys() and name != old_name:
        return (6, None)

    if len(name) == 0:
        return(7, None)

    return (0, None)
