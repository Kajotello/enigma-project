from enigma_classes.functions import dict_from_str_with_pairs


class Plugboard:

    """Represent plugboard of machine"""

    def __init__(self, connections: str) -> None:
        validate_plugboard(connections)
        self._connections = connections
        if len(connections) == 0:
            self._plugboard_dict = {}
        else:
            self._plugboard_dict = dict_from_str_with_pairs(connections)

    @property
    def plugboard_dict(self) -> dict:

        """Dictionary use to code letter.
        (for example {'A': 'B'} means that A letter is code to B)
        Dictionary is symmetrical, so if A match to B, B match to A"""

        return self._plugboard_dict

    @property
    def connections(self) -> str:

        """Connections in string format which is given to constructor
        Useless in coding meaning, but needed to display connections in GUI"""

        return self._connections

    def code(self, ASCII_letter: int) -> int:

        """Code one letter given as number"""

        return self.plugboard_dict.get(ASCII_letter, ASCII_letter)


def validate_plugboard(connections: str) -> None:

    """Check the data passed as Plugboard Object property
    wiring: have to be a string with uppercase letters of english alphabet
    grouped in pairs and separated with spaces. Not every letter have to be
    included but letter cannot appear more than one time"""

    # list of allowed signs
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    # counter of letters in current group seprate by spaces
    letters_in_group = 0

    # table of lettrs which alreade apear
    check_table = []

    for position, letter in enumerate(connections, 1):

        # check if letter is a space
        if letter == " ":

            # check, if space apear after group of two signs
            if letters_in_group == 2:

                # if yes, format is ok for now
                letters_in_group = 0
            else:

                # if not, format is invalid
                raise PlugboardInvalidFormatError

        # check if the last group also have two signs
        # (spcial condition because there is no space after it)
        elif position == len(connections) and letters_in_group != 1:
            raise PlugboardInvalidFormatError

        # check if letter is in alphabet
        # (we have checked the space before so there is no problem with it)
        elif letter not in alphabet:

            # if not that sign is invalid
            raise PlugboardInvalidSignError

        # check if letter is in check table
        # (was there the same letter before?)
        elif letter in check_table:

            # if yes letter is duplicated
            raise PlugboardDuplicatedLetterError

        else:

            # if go here, the format is ok for now
            letters_in_group += 1
            check_table.append(letter)


class PlugboardInvalidFormatError(Exception):
    pass


class PlugboardInvalidSignError(Exception):
    pass


class PlugboardDuplicatedLetterError(Exception):
    pass
