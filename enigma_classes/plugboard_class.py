from enigma_classes.functions import dict_from_str_with_pairs


class Plugboard:

    """Represent plugboard of machine"""

    def __init__(self, connections: str) -> None:
        validate_plugboard(connections)
        self._connections_str = connections
        if len(connections) == 0:
            self._connections = {}
        else:
            self._connections = dict_from_str_with_pairs(connections)

    @property
    def connections(self) -> dict:
        return self._connections

    @property
    def connections_str(self) -> str:
        return self._connections_str

    def code(self, ASCII_letter: int) -> int:
        return self.connections.get(ASCII_letter, ASCII_letter)


def validate_plugboard(connections: str) -> None:

    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J',
                'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    i = 0
    check_table = []

    for position, letter in enumerate(connections, 1):

        if letter == " ":
            if i == 2:
                i = 0
            else:
                raise InvalidPlugboardFormatError

        elif letter not in alphabet:
            raise PlugboardInvalidSignError

        elif letter not in check_table:
            if position == len(connections) and i != 1:
                raise InvalidPlugboardFormatError
            i += 1
            check_table.append(letter)

        else:
            raise PlugboardDuplicatedLetterError


class InvalidPlugboardFormatError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class PlugboardInvalidSignError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)


class PlugboardDuplicatedLetterError(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
